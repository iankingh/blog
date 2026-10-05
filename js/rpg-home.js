(() => {
  const dialog = document.querySelector('#search-dialog');
  const input = document.querySelector('#quest-search');
  const results = document.querySelector('.search-results');
  const status = document.querySelector('.search-status');
  const retry = document.querySelector('.search-retry');
  const menu = document.querySelector('.menu-toggle');
  const sidebar = document.querySelector('#sidebar');
  let posts;
  let indexRequest;
  let searchRevision = 0;
  let searchOpener;

  const loadIndex = () => {
    if (posts) return Promise.resolve(posts);
    if (!indexRequest) {
      indexRequest = fetch(dialog.dataset.indexUrl).then(response => {
        if (!response.ok) throw new Error('Search index unavailable');
        return response.json();
      }).then(data => {
        if (!Array.isArray(data) || data.some(post => !post ||
          ['title', 'url', 'summary', 'content', 'date'].some(key => typeof post[key] !== 'string') ||
          !post.url.startsWith('/') || post.url.startsWith('//') ||
          !Array.isArray(post.tags) || post.tags.some(tag => typeof tag !== 'string'))) {
          throw new Error('Invalid search index');
        }
        posts = data.map(post => ({ ...post, searchText: `${post.title} ${post.tags.join(' ')} ${post.summary} ${post.content}`.toLocaleLowerCase() }));
        return posts;
      }).finally(() => { indexRequest = undefined; });
    }
    return indexRequest;
  };

  const renderMatches = loadedPosts => {
    const words = input.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    results.replaceChildren();
    if (!words.length) {
      status.textContent = '輸入關鍵字，探索所有筆記。';
      return;
    }
    const matches = loadedPosts.filter(post => words.every(word => post.searchText.includes(word)));
    status.textContent = matches.length ? `找到 ${matches.length} 個任務` : '尚未找到任務，試試其他技能或關鍵字。';
    matches.forEach(post => {
      const link = document.createElement('a');
      link.className = 'search-result';
      link.href = post.url;
      const title = document.createElement('strong');
      title.textContent = post.title;
      const description = document.createElement('span');
      description.textContent = post.summary;
      const meta = document.createElement('small');
      meta.textContent = `${post.date} · ${post.tags.join(' / ')}`;
      link.append(title, description, meta);
      results.append(link);
    });
  };

  const updateSearch = async () => {
    const revision = ++searchRevision;
    results.replaceChildren();
    results.setAttribute('aria-busy', 'true');
    retry.hidden = true;
    status.textContent = '正在載入筆記…';
    try {
      const loadedPosts = await loadIndex();
      if (revision !== searchRevision || !dialog.open) return;
      renderMatches(loadedPosts);
    } catch {
      if (revision !== searchRevision || !dialog.open) return;
      status.textContent = '筆記暫時無法載入，請再試一次。';
      retry.hidden = false;
    } finally {
      if (revision === searchRevision) results.setAttribute('aria-busy', 'false');
    }
  };

  const openSearch = trigger => {
    if (!dialog.open) {
      searchOpener = trigger || document.activeElement;
      dialog.showModal();
    }
    input.focus();
    updateSearch();
  };
  const restoreSearchFocus = () => {
    ++searchRevision;
    results.setAttribute('aria-busy', 'false');
    if (searchOpener?.isConnected) searchOpener.focus({ preventScroll: true });
    searchOpener = undefined;
  };
  const closeSearch = () => {
    if (!dialog.open) return;
    dialog.close();
    restoreSearchFocus();
  };
  document.querySelectorAll('[data-search-open]').forEach(button => button.addEventListener('click', () => openSearch(button)));
  document.querySelector('.search-close').addEventListener('click', closeSearch);
  dialog.addEventListener('close', () => { if (!dialog.open) restoreSearchFocus(); });
  dialog.addEventListener('cancel', event => { event.preventDefault(); closeSearch(); });
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const rect = dialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) closeSearch();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && dialog.open) {
      event.preventDefault();
      closeSearch();
      return;
    }
    if (event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey && !event.target.closest('input, textarea, select, [contenteditable]')) {
      event.preventDefault();
      openSearch();
    }
  });
  input.addEventListener('input', updateSearch);
  retry.addEventListener('click', () => { input.focus(); updateSearch(); });

  const closeMenu = (restoreFocus = false) => {
    if (restoreFocus && sidebar.contains(document.activeElement)) menu.focus({ preventScroll: true });
    menu.setAttribute('aria-expanded', 'false');
    menu.setAttribute('aria-label', '開啟冒險選單');
    sidebar.classList.remove('is-open');
  };
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    menu.setAttribute('aria-label', open ? '關閉冒險選單' : '開啟冒險選單');
    sidebar.classList.toggle('is-open', open);
  });
  sidebar.querySelectorAll('a').forEach(link => link.addEventListener('click', () => closeMenu()));
  document.addEventListener('keydown', event => { if (event.key === 'Escape' && !event.defaultPrevented && !dialog.open) closeMenu(true); });
  document.addEventListener('click', event => {
    if (!sidebar.contains(event.target) && !menu.contains(event.target)) closeMenu();
  });
})();
