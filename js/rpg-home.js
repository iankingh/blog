(() => {
  const dialog = document.querySelector('#search-dialog');
  const input = document.querySelector('#quest-search');
  const results = document.querySelector('.search-results');
  const status = document.querySelector('.search-status');
  const posts = JSON.parse(document.querySelector('#quest-index').textContent);
  const menu = document.querySelector('.menu-toggle');
  const sidebar = document.querySelector('#sidebar');

  const openSearch = () => {
    if (!dialog.open) dialog.showModal();
    input.focus();
  };
  document.querySelectorAll('[data-search-open]').forEach(button => button.addEventListener('click', openSearch));
  document.querySelector('.search-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const rect = dialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && dialog.open) {
      event.preventDefault();
      dialog.close();
      return;
    }
    if (event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey && !event.target.closest('input, textarea, select, [contenteditable]')) {
      event.preventDefault();
      openSearch();
    }
  });
  input.addEventListener('input', () => {
    const words = input.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    results.replaceChildren();
    if (!words.length) {
      status.textContent = '輸入關鍵字，探索所有筆記。';
      return;
    }
    const matches = posts.filter(post => {
      const text = `${post.title} ${post.tags.join(' ')} ${post.summary}`.toLocaleLowerCase();
      return words.every(word => text.includes(word));
    });
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
  });
  const closeMenu = () => {
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
  sidebar.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
  document.addEventListener('click', event => {
    if (!sidebar.contains(event.target) && !menu.contains(event.target)) closeMenu();
  });
})();
