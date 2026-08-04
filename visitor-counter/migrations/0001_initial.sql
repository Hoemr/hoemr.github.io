CREATE TABLE IF NOT EXISTS visitors (
  visitor_id TEXT PRIMARY KEY,
  first_seen TEXT NOT NULL,
  last_seen TEXT NOT NULL,
  page_views INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS daily_visitors (
  day TEXT NOT NULL,
  visitor_id TEXT NOT NULL,
  PRIMARY KEY (day, visitor_id)
) WITHOUT ROWID;

CREATE TABLE IF NOT EXISTS daily_stats (
  day TEXT PRIMARY KEY,
  page_views INTEGER NOT NULL DEFAULT 0
);
