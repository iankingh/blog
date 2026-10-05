// Run with: node .github/scripts/check-search.cjs
// Exercise the shipped search script with deferred fetches and a small DOM harness.
// Browser layout/dialog behavior is checked separately in the local preview.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const repoRoot = path.resolve(__dirname, '../..');
const source = fs.readFileSync(path.join(repoRoot, 'static/js/rpg-home.js'), 'utf8');

class Element {
  constructor(tag = 'div') {
    this.tagName = tag.toUpperCase();
    this.children = [];
    this.listeners = {};
    this.attributes = {};
    this.hidden = false;
    this.isConnected = true;
    this.dataset = {};
    this.value = '';
    this.textContent = '';
    const values = new Set();
    this.classList = { remove: name => values.delete(name), toggle: (name, enabled) => enabled ? values.add(name) : values.delete(name), contains: name => values.has(name) };
  }
  addEventListener(type, callback) { (this.listeners[type] ||= []).push(callback); }
  dispatch(type, props = {}) {
    const event = { target: this, defaultPrevented: false, preventDefault() { this.defaultPrevented = true; }, ...props };
    for (const callback of this.listeners[type] || []) callback(event);
    return event;
  }
  setAttribute(name, value) { this.attributes[name] = String(value); }
  getAttribute(name) { return this.attributes[name]; }
  append(...children) { children.forEach(child => { child.parent = this; this.children.push(child); }); }
  replaceChildren(...children) { this.children = []; this.append(...children); }
  contains(other) { return other === this || this.children.some(child => child.contains(other)); }
  closest() { return ['INPUT', 'TEXTAREA', 'SELECT'].includes(this.tagName) ? this : null; }
  getBoundingClientRect() { return { left: 0, right: 100, top: 0, bottom: 100 }; }
  set innerHTML(_) { throw new Error('HTML injection is not allowed'); }
}

function harness() {
  const document = new Element();
  const dialog = new Element('dialog');
  dialog.open = false;
  dialog.dataset.indexUrl = '/blog/search-index.json';
  dialog.showModal = () => { dialog.open = true; };
  dialog.close = () => {
    dialog.open = false;
    setImmediate(() => dialog.dispatch('close'));
  };
  const input = new Element('input');
  const results = new Element();
  const status = new Element('p');
  const retry = new Element('button');
  retry.hidden = true;
  const close = new Element('button');
  const opener = new Element('button');
  const menu = new Element('button');
  menu.setAttribute('aria-expanded', 'false');
  const sidebar = new Element('aside');
  const sideLink = new Element('a');
  sidebar.append(sideLink);
  sidebar.querySelectorAll = () => [sideLink];
  const bySelector = { '#search-dialog': dialog, '#quest-search': input, '.search-results': results, '.search-status': status, '.search-retry': retry, '.search-close': close, '.menu-toggle': menu, '#sidebar': sidebar };
  document.querySelector = selector => bySelector[selector];
  document.querySelectorAll = selector => selector === '[data-search-open]' ? [opener] : [];
  document.createElement = tag => {
    const element = new Element(tag);
    element.focus = () => { document.activeElement = element; };
    return element;
  };
  for (const element of Object.values(bySelector).concat(opener, sideLink)) element.focus = () => { document.activeElement = element; };
  document.activeElement = opener;
  const requests = [];
  const fetch = url => {
    assert.equal(url, '/blog/search-index.json');
    return new Promise((resolve, reject) => requests.push({ resolve, reject }));
  };
  vm.runInNewContext(source, { document, fetch, Promise, Error });
  return { document, dialog, input, results, status, retry, close, opener, menu, sidebar, sideLink, requests };
}
const tick = () => new Promise(resolve => setImmediate(resolve));
const fixture = [
  { title: '<img src=x onerror=alert(1)> Hikari', url: '/blog/hikari/', tags: ['Java'], summary: 'Short excerpt', content: 'connectionTimeout FULLTEXT_ONLY', date: '2026.10.05' },
  { title: 'Other', url: '/blog/other/', tags: [], summary: 'Other summary', content: 'Other body', date: '2026.10.04' }
];
const respond = (h, data = fixture) => h.requests.at(-1).resolve({ ok: true, json: async () => data });
const type = (h, value) => { h.input.value = value; h.input.dispatch('input'); };

(async () => {
  const h = harness();
  assert.equal(h.requests.length, 0, 'Loading page must not fetch the index');
  h.opener.dispatch('click');
  assert(h.dialog.open);
  assert.equal(h.document.activeElement, h.input);
  assert.equal(h.requests.length, 1);
  assert(h.status.textContent.includes('載入'));
  type(h, 'notfound');
  type(h, 'connectionTimeout');
  assert.equal(h.requests.length, 1, 'Rapid input must share the pending request');
  respond(h);
  await tick();
  assert.equal(h.results.children.length, 1);
  assert.equal(h.results.children[0].children[0].textContent, fixture[0].title);
  assert.equal(h.results.children[0].children[1].textContent, 'Short excerpt');
  assert.equal(h.results.getAttribute('aria-busy'), 'false');
  type(h, 'JAvA FULLTEXT_ONLY');
  await tick();
  assert.equal(h.results.children.length, 1, 'All words must match case-insensitively across title/tags/full text');
  type(h, 'no-result');
  await tick();
  assert.equal(h.results.children.length, 0);
  assert(h.status.textContent.includes('尚未找到'));
  h.document.dispatch('keydown', { key: 'Escape', target: h.input });
  assert(!h.dialog.open);
  assert.equal(h.document.activeElement, h.opener);
  await tick();
  h.opener.dispatch('click');
  await tick();
  assert.equal(h.requests.length, 1, 'A loaded index must be cached across reopening');
  type(h, '   ');
  await tick();
  assert.equal(h.results.children.length, 0);
  assert(h.status.textContent.includes('輸入關鍵字'));

  const race = harness();
  race.opener.dispatch('click');
  type(race, 'Other');
  race.close.dispatch('click');
  race.opener.dispatch('click');
  type(race, 'FULLTEXT_ONLY');
  respond(race);
  await tick();
  assert(race.dialog.open);
  assert.equal(race.results.children.length, 1);
  assert.equal(race.results.children[0].href, '/blog/hikari/');
  assert.equal(race.requests.length, 1, 'Close/reopen must share the pending request and show only the latest input');

  const closed = harness();
  closed.opener.dispatch('click');
  type(closed, 'Other');
  closed.close.dispatch('click');
  respond(closed);
  await tick();
  assert.equal(closed.results.children.length, 0, 'A response must not repopulate a closed dialog');
  closed.opener.dispatch('click');
  await tick();
  assert.equal(closed.results.children.length, 1);
  assert.equal(closed.requests.length, 1);

  const failure = harness();
  failure.opener.dispatch('click');
  type(failure, 'connectionTimeout');
  failure.requests[0].resolve({ ok: false });
  await tick();
  assert(!failure.retry.hidden);
  assert(failure.status.textContent.includes('無法載入'));
  assert.equal(failure.results.getAttribute('aria-busy'), 'false');
  failure.retry.dispatch('click');
  assert.equal(failure.requests.length, 2);
  assert(failure.retry.hidden);
  assert.equal(failure.document.activeElement, failure.input, 'Retry must move focus to the input before hiding its button');
  respond(failure);
  await tick();
  assert.equal(failure.results.children.length, 1);

  const invalid = harness();
  invalid.opener.dispatch('click');
  respond(invalid, [{ ...fixture[0], url: 'javascript:alert(1)' }]);
  await tick();
  assert(!invalid.retry.hidden);
  invalid.retry.dispatch('click');
  invalid.requests[1].reject(new Error('Network unavailable'));
  await tick();
  assert(!invalid.retry.hidden);
  invalid.retry.dispatch('click');
  respond(invalid);
  await tick();
  assert(invalid.retry.hidden);

  const malformed = harness();
  malformed.opener.dispatch('click');
  malformed.requests[0].resolve({ ok: true, json: async () => { throw new SyntaxError('Broken JSON'); } });
  await tick();
  assert(!malformed.retry.hidden);
  malformed.retry.dispatch('click');
  respond(malformed, { unexpected: 'object instead of posts array' });
  await tick();
  assert(!malformed.retry.hidden);
  malformed.retry.dispatch('click');
  respond(malformed, []);
  await tick();
  type(malformed, 'Java');
  await tick();
  assert.equal(malformed.results.children.length, 0);
  assert(malformed.status.textContent.includes('尚未找到'));

  const mobile = harness();
  mobile.menu.dispatch('click');
  mobile.sideLink.focus();
  mobile.document.dispatch('keydown', { key: 'Escape', target: mobile.sideLink });
  assert.equal(mobile.document.activeElement, mobile.menu);
  assert.equal(mobile.menu.getAttribute('aria-expanded'), 'false');
  assert(!mobile.sidebar.classList.contains('is-open'));
  mobile.menu.dispatch('click');
  mobile.sideLink.focus();
  mobile.document.dispatch('keydown', { key: '/', target: mobile.sideLink });
  mobile.document.dispatch('keydown', { key: 'Escape', target: mobile.input });
  assert.equal(mobile.document.activeElement, mobile.sideLink);
  assert(mobile.sidebar.classList.contains('is-open'), 'Closing search must not also close the menu underneath');
  respond(mobile);
  await tick();
  console.log('PASS: lazy load/cache, full text, rapid input and close/reopen races, HTTP/network/malformed retry, safe text rendering, and search/mobile focus.');
})().catch(error => { console.error(error); process.exitCode = 1; });
