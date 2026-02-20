// Wait for page to fully load before executing
window.addEventListener('load', () => {
    console.log('GitHub stars script running on URL:', window.location.href);

    // Find all links that point to GitHub repositories
    const githubLinks = document.querySelectorAll('a[href^="https://github.com/"]');
    console.log(`Found ${githubLinks.length} GitHub links:`,
                Array.from(githubLinks).map(link => link.href));

    // Process each GitHub link
    githubLinks.forEach((link, index) => {
      const href = link.getAttribute('href');
      console.log(`[${index}] Processing link: ${href}`);

      try {
        // Extract owner and repo from GitHub URL
        // First, remove any query parameters or hash
        const urlWithoutParams = href.split(/[?#]/)[0];
        // Remove trailing slashes
        const cleanHref = urlWithoutParams.replace(/\/+$/, '');

        // Extract path components
        const parts = cleanHref.replace('https://github.com/', '').split('/');
        console.log(`[${index}] URL parts:`, parts);

        if (parts.length < 2) {
          console.log(`[${index}] Not enough URL parts for a repository`);
          return;
        }

        const owner = parts[0];
        const repo = parts[1];

        // Skip non-repository URLs
        if (href.includes('/blob/') || href.includes('/tree/') || href.includes('/issues/') ||
            href.includes('/pull/') || href.includes('/releases/') ||
            owner === 'orgs' || owner === 'search') {
          console.log(`[${index}] Skipping non-repo URL: ${href}`);
          return;
        }

        console.log(`[${index}] Adding stars badge for ${owner}/${repo}`);

        // Create a direct shields.io badge with cache busting parameter to avoid caching issues
        const timestamp = new Date().getTime();
        const badgeImg = document.createElement('img');
        badgeImg.className = 'github-stars';
        badgeImg.alt = 'GitHub stars';
        badgeImg.src = `https://img.shields.io/github/stars/${owner}/${repo}?style=social&_=${timestamp}`;
        badgeImg.style.marginLeft = '4px';
        badgeImg.style.verticalAlign = 'middle';
        badgeImg.style.height = '20px'; // Explicit height to ensure it loads properly

        // Set loading attribute to eager to prioritize loading
        badgeImg.loading = 'eager';

        // Add event listeners for debugging
        badgeImg.addEventListener('load', () => {
          console.log(`[${index}] Badge loaded for ${owner}/${repo}`);
        });

        badgeImg.addEventListener('error', (err) => {
          console.error(`[${index}] Badge failed to load for ${owner}/${repo}:`, err);
        });

        // Append badge to the link
        link.appendChild(badgeImg);

      } catch (error) {
        console.error(`[${index}] Error processing GitHub link:`, error);
      }
    });
  });
