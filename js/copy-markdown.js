(function () {
  // Only run on post pages
  const path = window.location.pathname;
  const postMatch = path.match(/\/(posts\/[^/]+)\//);
  if (!postMatch) return;

  const postPath = postMatch[1]; // e.g. "posts/2026-03-10-ai-tutorial"
  const rawUrl = `https://raw.githubusercontent.com/lawwu/lawwu.github.io/main/${postPath}/index.qmd`;

  function createButton() {
    const btn = document.createElement('button');
    btn.id = 'copy-markdown-btn';
    btn.innerHTML = '<i class="bi bi-clipboard"></i> Copy Markdown';
    btn.title = 'Copy post source as Markdown (.qmd)';
    btn.style.cssText = [
      'position:fixed',
      'top:4.5rem',
      'right:1rem',
      'z-index:1000',
      'padding:0.35rem 0.85rem',
      'background:transparent',
      'color:#B5621E',
      'border:1px solid rgba(181,98,30,0.35)',
      'border-radius:4px',
      'cursor:pointer',
      'font-family:"JetBrains Mono",monospace',
      'font-size:0.7rem',
      'font-weight:500',
      'letter-spacing:0.05em',
      'text-transform:uppercase',
      'opacity:0.8',
      'transition:opacity 0.2s,background 0.2s,color 0.2s,border-color 0.2s',
      'box-shadow:0 2px 8px rgba(0,0,0,0.08)',
      'backdrop-filter:blur(8px)',
      '-webkit-backdrop-filter:blur(8px)',
    ].join(';');

    btn.addEventListener('mouseenter', () => {
      btn.style.opacity = '1';
      btn.style.background = 'rgba(181,98,30,0.08)';
      btn.style.borderColor = '#B5621E';
    });
    btn.addEventListener('mouseleave', () => {
      btn.style.opacity = '0.8';
      btn.style.background = 'transparent';
      btn.style.borderColor = 'rgba(181,98,30,0.35)';
    });

    btn.addEventListener('click', async () => {
      btn.disabled = true;
      btn.innerHTML = '<i class="bi bi-hourglass-split"></i> Fetching…';
      try {
        const resp = await fetch(rawUrl);
        if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
        const text = await resp.text();
        await navigator.clipboard.writeText(text);
        btn.innerHTML = '<i class="bi bi-check2"></i> Copied!';
        btn.style.color = '#198754';
        btn.style.borderColor = 'rgba(25,135,84,0.4)';
      } catch (err) {
        console.error('copy-markdown: failed', err);
        btn.innerHTML = '<i class="bi bi-x-circle"></i> Failed';
        btn.style.color = '#dc3545';
        btn.style.borderColor = 'rgba(220,53,69,0.4)';
      }
      setTimeout(() => {
        btn.innerHTML = '<i class="bi bi-clipboard"></i> Copy Markdown';
        btn.style.color = '#B5621E';
        btn.style.borderColor = 'rgba(181,98,30,0.35)';
        btn.disabled = false;
      }, 2500);
    });

    return btn;
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => document.body.appendChild(createButton()));
  } else {
    document.body.appendChild(createButton());
  }
})();
