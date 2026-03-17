// TOC active section highlight via IntersectionObserver
(function () {
  const toc = document.getElementById('TOC');
  if (!toc) return;

  const tocLinks = Array.from(toc.querySelectorAll('a[href^="#"]'));
  if (tocLinks.length === 0) return;

  let activeLink = null;

  function setActive(link) {
    if (activeLink === link) return;

    if (activeLink) {
      activeLink.classList.remove('active', 'toc-active-indicator');
    }

    activeLink = link;

    if (activeLink) {
      activeLink.classList.add('active', 'toc-active-indicator');
    }
  }

  // Build a map of id -> tocLink
  const idToLink = new Map();
  tocLinks.forEach(link => {
    const id = link.getAttribute('href').slice(1);
    idToLink.set(id, link);
  });

  // Observe all headings that have a corresponding TOC entry
  const headings = Array.from(document.querySelectorAll('h1[id],h2[id],h3[id],h4[id],h5[id],h6[id]'))
    .filter(h => idToLink.has(h.id));

  if (headings.length === 0) return;

  // Use a small top margin so the heading is "active" when it's near the top
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          setActive(idToLink.get(entry.target.id));
        }
      });
    },
    {
      rootMargin: '-10% 0px -80% 0px',
      threshold: 0,
    }
  );

  headings.forEach(h => observer.observe(h));

  // Fallback: on scroll, find the heading closest to the top of the viewport
  window.addEventListener('scroll', function () {
    if (activeLink) return; // observer is handling it
    const scrollTop = window.scrollY + window.innerHeight * 0.15;
    let closest = headings[0];
    for (const h of headings) {
      if (h.offsetTop <= scrollTop) closest = h;
      else break;
    }
    setActive(idToLink.get(closest.id));
  }, { passive: true });
})();
