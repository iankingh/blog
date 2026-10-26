/* Copy the locked npm distribution for Hugo; deployment needs no npm or CDN. */
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

const root = path.resolve(__dirname, '../..');
const installed = path.join(root, 'node_modules/pele');
const pkg = JSON.parse(fs.readFileSync(path.join(installed, 'package.json'), 'utf8'));
const expected = JSON.parse(fs.readFileSync(path.join(root, 'package.json'), 'utf8')).dependencies.pele;
if (pkg.version !== expected) throw new Error('Run npm ci to install the locked Pele version');
const output = path.join(root, 'static/lib/pele');
fs.mkdirSync(output, { recursive: true });
for (const [source, destination] of [['dist/pele.global.js', 'pele.global.js'], ['LICENSE', 'LICENSE']]) {
  fs.copyFileSync(path.join(installed, source), path.join(output, destination));
}
const bundle = fs.readFileSync(path.join(output, 'pele.global.js'));
fs.writeFileSync(path.join(output, 'version.json'), JSON.stringify({
  package: 'pele', version: pkg.version, license: pkg.license,
  source: 'https://github.com/obsidianmd/pele',
  sha256: crypto.createHash('sha256').update(bundle).digest('hex')
}, null, 2) + '\n');
console.log(`Vendored Pele ${pkg.version}: ${bundle.length} bytes`);
