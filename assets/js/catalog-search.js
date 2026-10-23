const search = document.querySelector("#article-search");
const results = document.querySelector("#search-results");
const browse = document.querySelector("#catalog-browse");
const status = document.querySelector("#search-status");
const articles = [...document.querySelectorAll("[data-search-text]")];

document.querySelector(".catalog-search").hidden = false;

search.addEventListener("input", () => {
  const query = search.value.trim().toLocaleLowerCase();
  const terms = query.split(/\s+/);
  let count = 0;

  for (const article of articles) {
    const text = article.dataset.searchText.toLocaleLowerCase();
    const matches = query.length > 0 && terms.every(term => text.includes(term));
    article.hidden = !matches;
    if (matches) count += 1;
  }

  results.hidden = query.length === 0;
  browse.hidden = query.length > 0;
  status.textContent = count === 0
    ? "No articles found. Try another topic or a broader search."
    : `${count} ${count === 1 ? "article" : "articles"} found.`;
});
