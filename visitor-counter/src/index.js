const ALLOWED_ORIGINS = new Set([
  "https://hoemr.github.io",
  "http://localhost:4000",
]);

const UUID_V4_PATTERN =
  /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

export function isValidVisitorId(value) {
  return typeof value === "string" && UUID_V4_PATTERN.test(value);
}

function headersFor(origin) {
  return {
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Origin": origin,
    "Cache-Control": "no-store",
    "Content-Type": "application/json; charset=utf-8",
    Vary: "Origin",
    "X-Content-Type-Options": "nosniff",
    "X-Robots-Tag": "noindex",
  };
}

function json(body, status, headers) {
  return new Response(JSON.stringify(body), { status, headers });
}

async function recordVisit(request, env, headers) {
  let body;

  try {
    body = await request.json();
  } catch {
    return json({ error: "Invalid JSON" }, 400, headers);
  }

  if (!isValidVisitorId(body.visitorId)) {
    return json({ error: "Invalid visitor ID" }, 400, headers);
  }

  const now = new Date().toISOString();
  const day = now.slice(0, 10);

  const results = await env.DB.batch([
    env.DB.prepare(`
      INSERT INTO visitors (visitor_id, first_seen, last_seen, page_views)
      VALUES (?1, ?2, ?2, 1)
      ON CONFLICT(visitor_id) DO UPDATE SET
        last_seen = excluded.last_seen,
        page_views = visitors.page_views + 1
    `).bind(body.visitorId, now),

    env.DB.prepare(`
      INSERT OR IGNORE INTO daily_visitors (day, visitor_id)
      VALUES (?1, ?2)
    `).bind(day, body.visitorId),

    env.DB.prepare(`
      INSERT INTO daily_stats (day, page_views)
      VALUES (?1, 1)
      ON CONFLICT(day) DO UPDATE SET
        page_views = daily_stats.page_views + 1
    `).bind(day),

    env.DB.prepare(`
      SELECT
        (SELECT COALESCE(SUM(page_views), 0) FROM daily_stats) AS total_views,
        (SELECT COUNT(*) FROM visitors) AS unique_visitors,
        (SELECT COALESCE(page_views, 0) FROM daily_stats WHERE day = ?1) AS today_views,
        (SELECT COUNT(*) FROM daily_visitors WHERE day = ?1) AS today_unique
    `).bind(day),
  ]);

  const stats = results[3]?.results?.[0];

  if (!stats) {
    return json({ error: "Statistics unavailable" }, 500, headers);
  }

  return json(stats, 200, headers);
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";

    if (!ALLOWED_ORIGINS.has(origin)) {
      return new Response("Forbidden", { status: 403 });
    }

    const headers = headersFor(origin);

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers });
    }

    const url = new URL(request.url);

    if (request.method !== "POST" || url.pathname !== "/visit") {
      return json({ error: "Not found" }, 404, headers);
    }

    return recordVisit(request, env, headers);
  },
};
