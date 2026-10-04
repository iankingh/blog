(() => {
  document.querySelectorAll('.article-body .highlight').forEach(block => {
    const code = block.querySelector('pre code');
    if (!code || !navigator.clipboard) return;
    const button = document.createElement('button');
    button.className = 'copy-code';
    button.type = 'button';
    button.textContent = '複製程式碼';
    button.setAttribute('aria-label', '複製此段程式碼');
    button.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(code.textContent);
        button.textContent = '已複製';
      } catch {
        button.textContent = '請選取程式碼複製';
      }
      window.setTimeout(() => { button.textContent = '複製程式碼'; }, 2000);
    });
    block.append(button);
  });
})();
