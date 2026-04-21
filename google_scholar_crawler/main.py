"""
Crawl Google Scholar stats and write:
  - results/gs_data.json          (full author record, used by the home page JS)
  - results/gs_data_shieldsio.json (shields.io dynamic-JSON endpoint payload)

Robustness notes
----------------
Google Scholar aggressively blocks GitHub Actions IPs. We therefore:
  1. Try multiple proxy strategies in order:
       ScraperAPI (if SCRAPER_API_KEY secret is set) -> FreeProxies -> direct
  2. Retry each strategy a few times.
  3. On total failure we *do not* fail the workflow and *do not* overwrite the
     existing gs_data.json, so the badge keeps showing the last known number.
"""

from __future__ import annotations

import json
import os
import sys
import time
import traceback
from datetime import datetime

from scholarly import ProxyGenerator, scholarly


SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID")
SCRAPER_API_KEY = os.environ.get("SCRAPER_API_KEY")

RESULTS_DIR = "results"
DATA_FILE = os.path.join(RESULTS_DIR, "gs_data.json")
SHIELDS_FILE = os.path.join(RESULTS_DIR, "gs_data_shieldsio.json")


def log(msg: str) -> None:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def setup_proxy() -> str:
    """Configure scholarly to route through a proxy pool. Returns strategy name."""
    pg = ProxyGenerator()

    if SCRAPER_API_KEY:
        log("proxy: trying ScraperAPI...")
        try:
            if pg.ScraperAPI(SCRAPER_API_KEY):
                scholarly.use_proxy(pg)
                return "scraperapi"
        except Exception as e:
            log(f"proxy: ScraperAPI setup failed: {e}")

    log("proxy: trying FreeProxies...")
    try:
        if pg.FreeProxies():
            scholarly.use_proxy(pg)
            return "freeproxies"
    except Exception as e:
        log(f"proxy: FreeProxies setup failed: {e}")

    log("proxy: falling back to direct connection (likely to be blocked).")
    return "direct"


def fetch_author() -> dict:
    log(f"fetch: search_author_id({SCHOLAR_ID})")
    author = scholarly.search_author_id(SCHOLAR_ID)
    log("fetch: filling sections (basics / indices / counts / publications)...")
    author = scholarly.fill(
        author, sections=["basics", "indices", "counts", "publications"]
    )
    return author


def fetch_with_retries(max_attempts: int = 4) -> dict | None:
    last_err: Exception | None = None
    for attempt in range(1, max_attempts + 1):
        try:
            log(f"attempt {attempt}/{max_attempts}")
            return fetch_author()
        except Exception as e:  # noqa: BLE001 - we want to catch everything
            last_err = e
            log(f"attempt {attempt} failed: {type(e).__name__}: {e}")
            # Re-setup proxy between attempts in case the previous proxy died.
            time.sleep(3)
            try:
                setup_proxy()
            except Exception as e2:
                log(f"re-setup_proxy failed: {e2}")
    log(f"all attempts failed. Last error: {last_err}")
    if last_err is not None:
        traceback.print_exception(type(last_err), last_err, last_err.__traceback__)
    return None


def write_outputs(author: dict) -> None:
    author["updated"] = str(datetime.now())
    author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}

    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(author, f, ensure_ascii=False)

    shields_payload = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author["citedby"]),
    }
    with open(SHIELDS_FILE, "w", encoding="utf-8") as f:
        json.dump(shields_payload, f, ensure_ascii=False)

    log(f"done. citedby={author['citedby']}, wrote {DATA_FILE} & {SHIELDS_FILE}")


def main() -> int:
    if not SCHOLAR_ID:
        log("ERROR: GOOGLE_SCHOLAR_ID env var is not set.")
        return 1

    os.makedirs(RESULTS_DIR, exist_ok=True)
    setup_proxy()

    author = fetch_with_retries()
    if author is None:
        log("WARN: keeping previous gs_data.json (if any) and exiting gracefully.")
        return 0

    write_outputs(author)
    return 0


if __name__ == "__main__":
    sys.exit(main())
