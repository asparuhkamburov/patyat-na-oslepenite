const menu = document.querySelector('.menu');
const nav = document.querySelector('.navlinks');
if (menu && nav) {
  const close = () => { nav.classList.remove('open'); menu.setAttribute('aria-expanded', 'false'); };
  menu.addEventListener('click', () => { const open = nav.classList.toggle('open'); menu.setAttribute('aria-expanded', String(open)); });
  nav.addEventListener('click', e => { if(e.target.closest('a')) close(); });
  document.addEventListener('keydown', e => { if(e.key === 'Escape' && nav.classList.contains('open')) { close(); menu.focus(); } });
}
const rows = [...document.querySelectorAll('.book-row')];
const filters = [...document.querySelectorAll('.filter')];
const search = document.querySelector('#book-search');
let genre = 'all';
function updateCatalog() {
  const term = (search?.value || '').toLocaleLowerCase('bg').trim();
  let count = 0;
  for (const row of rows) { const show = (genre === 'all' || row.dataset.genre === genre) && row.textContent.toLocaleLowerCase('bg').includes(term); row.hidden = !show; if(show) count++; }
  const countEl = document.querySelector('#catalog-count');
  if(countEl) countEl.textContent = count === 1 ? '1 заглавие' : `${count} заглавия`;
  const empty = document.querySelector('#no-results'); if(empty) empty.hidden = count > 0;
}
filters.forEach(button => button.addEventListener('click', () => { genre = button.dataset.genre; filters.forEach(b => b.setAttribute('aria-pressed', String(b === button))); updateCatalog(); }));
search?.addEventListener('input', updateCatalog);
if(rows.length) updateCatalog();
// Preserve links shared before the author homepage replaced the single-book page.
if(document.body.dataset.page === 'home' && ['#book','#award','#context'].includes(location.hash)) {
  location.replace(`books/patyat-na-oslepenite/${location.hash}`);
}
