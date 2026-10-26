(() => {
  document.querySelectorAll('[data-mermaid-diagram]').forEach(figure => {
    if (figure.dataset.diagramState) return;
    const canvas = figure.querySelector('[data-diagram-canvas]');
    const status = figure.querySelector('[data-diagram-status]');
    const details = figure.querySelector('.diagram-source');
    const source = details.querySelector('code').textContent;
    const fail = state => {
      figure.dataset.diagramState = state;
      canvas.hidden = true;
      details.open = true;
      status.textContent = '圖表暫時無法顯示，仍可閱讀下方原始碼。';
      status.hidden = false;
    };
    if (typeof window.pele?.mount !== 'function') {
      fail('unavailable');
      return;
    }
    figure.dataset.diagramState = 'loading';
    canvas.hidden = false;
    let rendered = false;
    try {
      window.pele.mount(canvas, source, {
        links: false,
        images: false,
        zoom: false,
        onRender: () => {
          figure.dataset.diagramState = 'rendered';
          canvas.hidden = false;
          status.hidden = true;
          if (!rendered) details.open = false;
          rendered = true;
        },
        onError: () => fail('error')
      });
    } catch {
      fail('error');
    }
  });
})();
