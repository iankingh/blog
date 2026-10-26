/* Verify the shipped library, article sources, and failure isolation without npm ci. */
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const root = path.resolve(__dirname, '../..');
const read = name => fs.readFileSync(path.join(root, name), 'utf8');
const bundle = read('static/lib/pele/pele.global.js');
const runtime = vm.createContext({});
vm.runInContext(bundle, runtime, { timeout: 5000 });
const pele = runtime.pele;
const initializer = read('static/js/rpg-diagrams.js');

function articleDiagrams() {
  const diagrams = [];
  function visit(dir) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const name = path.join(dir, entry.name);
      if (entry.isDirectory()) visit(name);
      else if (entry.name.endsWith('.md')) {
        let fence;
        for (const line of fs.readFileSync(name, 'utf8').split('\n')) {
          if (fence) {
            if (line.trim() === fence.token) {
              if (fence.language === 'mermaid') diagrams.push({ name, source: fence.lines.join('\n') });
              fence = undefined;
            } else fence.lines.push(line);
          } else {
            const match = line.match(/^(`{3,}|~{3,})(\S*)\s*$/);
            if (match) fence = { token: match[1], language: match[2], lines: [] };
          }
        }
      }
    }
  }
  visit(path.join(root, 'content/post'));
  return diagrams;
}

function fixture(source) {
  const canvas = { hidden: true };
  const status = { hidden: true, textContent: '' };
  Object.defineProperty(status, 'innerHTML', { set() { throw new Error('Errors must be text'); } });
  const details = { open: true, querySelector: () => ({ textContent: source }) };
  const figure = {
    dataset: {},
    querySelector: selector => ({ '[data-diagram-canvas]': canvas, '[data-diagram-status]': status, '.diagram-source': details })[selector]
  };
  return { figure, canvas, status, details, source };
}

function initialize(items, library) {
  vm.runInNewContext(initializer, {
    document: { querySelectorAll: () => items.map(item => item.figure) },
    window: { pele: library }
  });
}

test('the self-hosted bundle matches the exact npm lock and retained MIT license', () => {
  const metadata = JSON.parse(read('static/lib/pele/version.json'));
  const version = JSON.parse(read('package.json')).dependencies.pele;
  const locked = JSON.parse(read('package-lock.json')).packages['node_modules/pele'];
  assert.equal(metadata.version, version);
  assert.equal(locked.version, version);
  assert.match(locked.resolved, /^https:\/\/registry\.npmjs\.org\/pele\//);
  assert.equal(metadata.sha256, crypto.createHash('sha256').update(bundle).digest('hex'));
  assert.match(read('static/lib/pele/LICENSE'), /MIT License/);
});

test('every actual Mermaid article fence renders at desktop and narrow widths', () => {
  const diagrams = articleDiagrams();
  assert(diagrams.some(d => d.name.endsWith('obsidian-pele.md')));
  assert(diagrams.some(d => d.name.endsWith('畫流程圖的工具.md')));
  diagrams.forEach((diagram, index) => {
    for (const width of [320, 960]) {
      const result = pele.render(diagram.source, { links: false, images: false, maxWidth: width, idPrefix: `note-${index}-${width}` });
      assert.match(result.svg, /^<svg /, diagram.name);
      assert(result.width > 0 && result.height > 0, diagram.name);
    }
  });
});

test('SVG IDs are distinct for multiple diagrams and accessibility text is retained', () => {
  const source = 'flowchart LR\n accTitle: 圖表名稱\n accDescr: 開始至完成\n A[開始] --> B[完成]';
  const a = pele.render(source, { idPrefix: 'first' }).svg;
  const b = pele.render(source, { idPrefix: 'second' }).svg;
  assert.match(a, /<title[^>]*>圖表名稱<\/title>/);
  assert.match(a, /<desc[^>]*>開始至完成<\/desc>/);
  const ids = html => [...html.matchAll(/\sid="([^"]+)"/g)].map(m => m[1]);
  assert(ids(a).every(id => !ids(b).includes(id)));
});

test('diagram source cannot create scripts, links, images or event attributes', () => {
  const svg = pele.render('flowchart TD\n A["<script>alert(1)</script>"] --> B[完成]\n click A "javascript:alert(1)"', { links: false, images: false }).svg;
  assert(!/<(?:script|a|image)\b/i.test(svg));
  assert(!/<[^>]+\son\w+\s*=/i.test(svg));
  assert(!/href="(?:javascript|data|vbscript):/i.test(svg));
  assert.throws(() => pele.render('flowchart TD\n A['), error => error.code === 'syntax');
});

test('successful mounts collapse source once, retain user choice, and initialize once', () => {
  const item = fixture('flowchart TD\n A --> B');
  let options, calls = 0;
  const library = { mount(canvas, source, opts) {
    calls += 1; options = opts;
    assert.equal(source, item.source);
    assert.equal(opts.links, false);
    assert.equal(opts.images, false);
    assert.equal(opts.zoom, false);
    opts.onRender(pele.render(source, { links: opts.links, images: opts.images }));
  } };
  initialize([item], library);
  assert.equal(item.figure.dataset.diagramState, 'rendered');
  assert.equal(item.details.open, false);
  assert.equal(item.canvas.hidden, false);
  assert.equal(item.status.hidden, true);
  item.details.open = true;
  options.onRender({});
  assert.equal(item.details.open, true, 'Resizing must not close source the reader opened');
  initialize([item], library);
  assert.equal(calls, 1);
});

test('a syntax error opens its source without preventing later diagrams', () => {
  const items = ['flowchart TD\n A --> B', 'flowchart TD\n A[', 'flowchart LR\n C --> D'].map(fixture);
  initialize(items, { mount(canvas, source, options) {
    try { options.onRender(pele.render(source)); }
    catch (error) { options.onError(error); }
  } });
  assert.deepEqual(items.map(i => i.figure.dataset.diagramState), ['rendered', 'error', 'rendered']);
  assert.equal(items[1].details.open, true);
  assert.equal(items[1].canvas.hidden, true);
  assert.match(items[1].status.textContent, /仍可閱讀/);
});

test('missing library or unexpected mount failure preserves a readable source', () => {
  for (const library of [undefined, { mount() { throw new Error('<img onerror=alert(1)>'); } }]) {
    const item = fixture('flowchart TD\n A --> B');
    initialize([item], library);
    assert.equal(item.details.open, true);
    assert.equal(item.canvas.hidden, true);
    assert.equal(item.status.hidden, false);
    assert(!item.status.textContent.includes('<img'));
  }
});
