"""
Fetch Google Scholar author stats via SerpAPI and write:
  - results/gs_data.json            (full author record, used by the home page JS)
  - results/gs_data_shieldsio.json  (shields.io dynamic-JSON endpoint payload)

Why SerpAPI
-----------
Scraping Google Scholar directly from GitHub Actions is unreliable in 2026:
Google aggressively blocks datacenter IPs, and the `scholarly` library plus
its free-proxy strategy times out almost every run. SerpAPI's free tier
(250 successful searches / month) is a stable and officially supported
middleman; at one run every 2 days we use ~15/month, well within quota.

Envs
----
GOOGLE_SCHOLAR_ID  the `user=...` part of your Scholar profile URL
SERPAPI_KEY        your private SerpAPI API key (free plan is fine)
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from typing import Any

import requests

SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID")
SERPAPI_KEY = os.environ.get("SERPAPI_KEY")

RESULTS_DIR = "results"
DATA_FILE = os.path.join(RESULTS_DIR, "gs_data.json")
SHIELDS_FILE = os.path.join(RESULTS_DIR, "gs_data_shieldsio.json")
SERPAPI_ENDPOINT = "https://serpapi.com/search.json"


def log(msg: str) -> None:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def fetch_author_raw() -> dict[str, Any]:
    params = {
        "engine": "google_scholar_author",
        "author_id": SCHOLAR_ID,
        "api_key": SERPAPI_KEY,
        "num": 100,
        "sort": "pubdate",
    }
    log(f"GET google_scholar_author (author_id={SCHOLAR_ID})")
    resp = requests.get(SERPAPI_ENDPOINT, params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


def _lookup_table(table: list[dict[str, Any]], key: str) -> int:
    """Pick `table[*][key]['all']` from SerpAPI's `cited_by.table` layout."""
    for entry in table:
        if key in entry and isinstance(entry[key], dict):
            try:
                return int(entry[key].get("all", 0) or 0)
            except (TypeError, ValueError):
                return 0
    return 0


def transform(raw: dict[str, Any]) -> dict[str, Any]:
    """Normalize SerpAPI response into the shape expected by the homepage JS
    (`fetch_google_scholar_stats.html` reads `citedby` and
    `publications[pub_id].num_citations`)."""
    author = raw.get("author") or {}
    cited_by = raw.get("cited_by") or {}
    articles = raw.get("articles") or []
    table = cited_by.get("table") or []

    citedby = _lookup_table(table, "citations")
    h_index = _lookup_table(table, "h_index")
    i10_index = _lookup_table(table, "i10_index")

    publications: dict[str, dict[str, Any]] = {}
    for art in articles:
        pub_id = art.get("citation_id") or art.get("title", "")
        if not pub_id:
            continue
        cited = art.get("cited_by") or {}
        num_citations = 0
        if isinstance(cited, dict):
            try:
                num_citations = int(cited.get("value") or 0)
            except (TypeError, ValueError):
                num_citations = 0
        publications[pub_id] = {
            "author_pub_id": pub_id,
            "title": art.get("title", ""),
            "authors": art.get("authors", ""),
            "publication": art.get("publication", ""),
            "year": art.get("year", ""),
            "link": art.get("link", ""),
            "num_citations": num_citations,
        }

    return {
        "name": author.get("name", ""),
        "affiliations": author.get("affiliations", ""),
        "email": author.get("email", ""),
        "interests": author.get("interests", []),
        "citedby": citedby,
        "hindex": h_index,
        "i10index": i10_index,
        "publications": publications,
        "updated": str(datetime.now()),
    }


def main() -> int:
    if not SCHOLAR_ID:
        log("ERROR: GOOGLE_SCHOLAR_ID env var is not set.")
        return 1
    if not SERPAPI_KEY:
        log("ERROR: SERPAPI_KEY env var is not set.")
        return 1

    os.makedirs(RESULTS_DIR, exist_ok=True)

    try:
        raw = fetch_author_raw()
    except requests.HTTPError as e:
        log(f"HTTP {e.response.status_code} from SerpAPI: {e.response.text[:300]}")
        return 1
    except requests.RequestException as e:
        log(f"Network error: {e}")
        return 1

    if isinstance(raw, dict) and "error" in raw:
        log(f"SerpAPI returned error: {raw['error']}")
        return 1

    data = transform(raw)
    log(
        f"parsed: name={data['name']!r}, citedby={data['citedby']}, "
        f"h={data['hindex']}, i10={data['i10index']}, "
        f"publications={len(data['publications'])}"
    )

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    shields_payload = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(data["citedby"]),
    }
    with open(SHIELDS_FILE, "w", encoding="utf-8") as f:
        json.dump(shields_payload, f, ensure_ascii=False)

    log(f"done. wrote {DATA_FILE} and {SHIELDS_FILE}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
