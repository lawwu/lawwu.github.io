// Reading progress bar — injected on post pages only
(function () {
  // Only run on post/article pages
  if (!document.querySelector('article, .quarto-article')) return;

  const bar = document.createElement('div');
  bar.id = 'reading-progress';
  document.body.prepend(bar);

  function updateProgress() {
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrolled = window.scrollY;
    const pct = docHeight > 0 ? Math.min((scrolled / docHeight) * 100, 100) : 0;
    bar.style.width = pct + '%';
  }

  window.addEventListener('scroll', updateProgress, { passive: true });
  updateProgress();
})();
