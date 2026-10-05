// Usage: node .github/scripts/create-share-card.mjs [path-to-sharp-package]
// Rebuilds the social card from the site's existing vector artwork.
import fs from 'node:fs/promises';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const require = createRequire(import.meta.url);
const sharp = require(process.argv[2] || 'sharp');
const root = fileURLToPath(new URL('../../', import.meta.url));
const directory = path.join(root, 'static/images');
const art = (await fs.readFile(path.join(directory, 'rpg-camp.svg'), 'utf8'))
  .replace(/<svg[^>]*>/, '<svg x="550" y="0" width="650" height="630" viewBox="0 0 600 390" preserveAspectRatio="xMidYMid slice" shape-rendering="crispEdges">');
const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<defs><linearGradient id="card-fade"><stop stop-color="#141916"/><stop offset="1" stop-color="#141916" stop-opacity="0"/></linearGradient></defs>
<rect width="1200" height="630" fill="#141916"/>${art}
<rect x="550" width="300" height="630" fill="url(#card-fade)"/>
<rect x="56" y="58" width="50" height="50" fill="none" stroke="#d6b577"/>
<path d="m81 67 7 14 14 7-14 7-7 14-7-14-14-7 14-7Z" fill="none" stroke="#d6b577" stroke-width="2"/>
<text x="125" y="92" fill="#d6b577" font-family="monospace" font-size="20" letter-spacing="2">THE ADVENTURER'S JOURNAL</text>
<text x="56" y="254" fill="#ece8dc" font-family="Georgia,serif" font-size="78">Ian Huang</text>
<text x="59" y="322" fill="#d6b577" font-family="sans-serif" font-size="34">Full Stack Engineer</text>
<text x="59" y="369" fill="#d6b577" font-family="sans-serif" font-size="30">AI Planner</text>
<text x="59" y="428" fill="#b3bbac" font-family="sans-serif" font-size="23">Build. Learn. Share.</text>
<line x1="59" y1="472" x2="380" y2="472" stroke="#56634e"/>
<text x="59" y="520" fill="#b3bbac" font-family="monospace" font-size="19">iankingh.github.io/blog</text>
</svg>`;
await fs.writeFile(path.join(directory, 'ian-java-share.svg'), svg);
await sharp(Buffer.from(svg)).png().toFile(path.join(directory, 'ian-java-share.png'));
console.log('Generated 1200 × 630 social card.');
