(() => {
  if (['localhost', '127.0.0.1', '[::1]'].includes(location.hostname)) return;
  const shortname = document.currentScript?.dataset.shortname;
  if (!/^[a-z0-9-]+$/.test(shortname || '')) return;
  const script = document.createElement('script');
  script.async = true;
  script.src = `https://${shortname}.disqus.com/embed.js`;
  document.head.append(script);
})();
