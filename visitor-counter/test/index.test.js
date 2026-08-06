import assert from "node:assert/strict";
import test from "node:test";

import worker, { isValidVisitorId, LEGACY_BASELINE } from "../src/index.js";

const VALID_VISITOR_ID = "123e4567-e89b-42d3-a456-426614174000";

class FakeStatement {
  constructor(sql) {
    this.sql = sql;
    this.params = [];
  }

  bind(...params) {
    this.params = params;
    return this;
  }
}

function fakeDatabase(stats) {
  return {
    prepare(sql) {
      return new FakeStatement(sql);
    },

    async batch(statements) {
      assert.equal(statements.length, 4);
      assert.deepEqual(statements[0].params[0], VALID_VISITOR_ID);
      return [{}, {}, {}, { results: [stats] }];
    },
  };
}

test("validates UUID v4 visitor identifiers", () => {
  assert.equal(isValidVisitorId(VALID_VISITOR_ID), true);
  assert.equal(isValidVisitorId("not-a-uuid"), false);
  assert.equal(isValidVisitorId(null), false);
});

test("rejects requests from other origins", async () => {
  const response = await worker.fetch(
    new Request("https://counter.example/visit", {
      method: "POST",
      headers: { Origin: "https://example.com" },
    }),
    {},
  );

  assert.equal(response.status, 403);
});

test("records a visit and adds the legacy baseline to cumulative statistics", async () => {
  const stats = {
    total_views: 120,
    unique_visitors: 80,
    today_views: 7,
    today_unique: 5,
  };

  const response = await worker.fetch(
    new Request("https://counter.example/visit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Origin: "https://hoemr.github.io",
      },
      body: JSON.stringify({ visitorId: VALID_VISITOR_ID }),
    }),
    { DB: fakeDatabase(stats) },
  );

  assert.equal(response.status, 200);
  assert.equal(
    response.headers.get("Access-Control-Allow-Origin"),
    "https://hoemr.github.io",
  );
  assert.deepEqual(await response.json(), {
    ...stats,
    total_views: stats.total_views + LEGACY_BASELINE.pageViews,
    unique_visitors: stats.unique_visitors + LEGACY_BASELINE.uniqueVisitors,
    includes_legacy_baseline: true,
  });
});
