(() => {
  const key = 'rpg-color-theme';
  const root = document.documentElement;
  let saved;
  try { saved = localStorage.getItem(key); } catch { /* Reading remains available when storage is disabled. */ }

  const apply = (value, persist = false) => {
    const selected = value === 'dark' ? 'dark' : 'light';
    root.dataset.theme = selected;
    document.querySelectorAll('[data-theme-toggle]').forEach(button => {
      const label = selected === 'dark' ? '切換為白色版' : '切換為黑色版';
      button.setAttribute('aria-label', label);
      button.setAttribute('title', label);
      button.setAttribute('aria-pressed', String(selected === 'dark'));
      button.querySelector('[data-theme-label]').textContent = selected === 'dark' ? '白色版' : '黑色版';
    });
    if (persist) {
      try { localStorage.setItem(key, selected); } catch { /* The switch also works without persistence. */ }
    }
    const commentFrame = document.querySelector('iframe.giscus-frame');
    if (commentFrame) commentFrame.contentWindow.postMessage({ giscus: { setConfig: { theme: selected } } }, 'https://giscus.app');
  };

  // Apply before the stylesheet renders to avoid flashing the wrong theme.
  apply(saved);
  document.addEventListener('DOMContentLoaded', () => {
    apply(root.dataset.theme);
    // Keep the existing NexT appearance control in sync with the shared preference.
    if (window.theme) window.theme.toggle = value => apply(value, true);
    document.querySelectorAll('[data-theme-toggle]').forEach(button => button.addEventListener('click', () => {
      apply(root.dataset.theme === 'dark' ? 'light' : 'dark', true);
    }));
  });
  window.addEventListener('storage', event => {
    if (event.key === key) apply(event.newValue);
  });
})();
