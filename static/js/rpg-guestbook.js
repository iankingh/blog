(() => {
  const board = document.querySelector('[data-guestbook]');
  if (!board) return;
  const status = board.querySelector('.guestbook-status');
  const retry = board.querySelector('.guestbook-retry');
  const thread = board.querySelector('#disqus_thread');
  const showMessage = message => {
    status.hidden = false;
    status.textContent = message;
    thread.setAttribute('aria-busy', 'false');
  };

  if (['localhost', '127.0.0.1', '[::1]'].includes(location.hostname)) {
    showMessage('本機預覽顯示留言板版面；請前往公開網站留下想法。');
    board.querySelector('.guestbook-public-link').hidden = false;
    return;
  }

  const { shortname, pageUrl, threadId, pageTitle } = board.dataset;
  if (!/^[a-z0-9-]+$/.test(shortname || '') || !threadId || !/^https:\/\//.test(pageUrl || '')) {
    showMessage('留言區暫時無法使用，請稍後再試。');
    return;
  }

  let timeout;
  let ready = false;
  const failed = () => {
    if (ready) return;
    clearTimeout(timeout);
    showMessage('留言區尚未載入，請重試或稍後再回來。');
    retry.hidden = false;
  };
  // A stable identifier keeps this board independent from article discussions.
  window.disqus_config = function () {
    this.page.identifier = threadId;
    this.page.url = pageUrl;
    this.page.title = pageTitle;
    this.callbacks.onReady = [() => {
      ready = true;
      clearTimeout(timeout);
      status.hidden = true;
      retry.hidden = true;
      thread.setAttribute('aria-busy', 'false');
    }];
  };

  retry.addEventListener('click', () => location.reload());
  const script = document.createElement('script');
  script.async = true;
  script.src = `https://${shortname}.disqus.com/embed.js`;
  script.addEventListener('error', failed);
  timeout = setTimeout(failed, 15000);
  document.head.append(script);
})();
