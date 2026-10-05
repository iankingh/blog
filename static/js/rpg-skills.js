(() => {
  const radar = document.querySelector('[data-skill-radar]');
  if (!radar) return;
  const buttons = [...radar.querySelectorAll('[data-skill-select]')];
  const select = id => {
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.skillSelect === id)));
    radar.querySelectorAll('[data-skill-detail]').forEach(detail => { detail.hidden = detail.dataset.skillDetail !== id; });
    radar.querySelectorAll('[data-skill-node]').forEach(node => node.classList.toggle('is-selected', node.dataset.skillNode === id));
  };
  buttons.forEach((button, index) => {
    button.addEventListener('click', () => select(button.dataset.skillSelect));
    button.addEventListener('keydown', event => {
      const move = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[event.key];
      if (!move && !['Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      const target = event.key === 'Home' ? 0 : event.key === 'End' ? buttons.length - 1 : (index + move + buttons.length) % buttons.length;
      buttons[target].focus();
      select(buttons[target].dataset.skillSelect);
    });
  });
})();
