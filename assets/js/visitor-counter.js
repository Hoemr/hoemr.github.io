(function () {
  var counter = document.querySelector("[data-visitor-counter]");

  if (!counter) return;

  var endpoint = counter.getAttribute("data-endpoint");
  var status = counter.querySelector("[data-counter-status]");

  if (!endpoint) {
    status.textContent = "Counter is not configured.";
    return;
  }

  var storageKey = "hoemr-visitor-id";
  var visitorId;

  try {
    visitorId = localStorage.getItem(storageKey);

    if (!visitorId) {
      visitorId = crypto.randomUUID();
      localStorage.setItem(storageKey, visitorId);
    }
  } catch (error) {
    visitorId = crypto.randomUUID();
  }

  fetch(endpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ visitorId: visitorId }),
  })
    .then(function (response) {
      if (!response.ok) throw new Error("Counter request failed");
      return response.json();
    })
    .then(function (stats) {
      counter.querySelector("[data-unique-visitors]").textContent =
        Number(stats.unique_visitors).toLocaleString();
      counter.querySelector("[data-today-unique]").textContent =
        Number(stats.today_unique).toLocaleString();
      counter.querySelector("[data-total-views]").textContent =
        Number(stats.total_views).toLocaleString();
      status.textContent = stats.includes_legacy_baseline
        ? "Anonymous first-party count · includes legacy estimate · no IP stored"
        : "Anonymous first-party count · no IP stored";
      counter.classList.add("visitor-counter--ready");
    })
    .catch(function () {
      status.textContent = "Visitor statistics are temporarily unavailable.";
    });
})();
