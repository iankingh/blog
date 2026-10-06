"""Extract the six Spring articles into a disposable Maven project.
Usage: python3 docs/verification/prepare-spring-lab.py /tmp/blog-spring-lab
Never writes to the source articles. Generated labs use local H2, not a real DB.
"""
from pathlib import Path
import re
import sys
import shutil
ROOT = Path(__file__).resolve().parents[2]
LAB = Path(sys.argv[1]).resolve()
if LAB == ROOT or ROOT in LAB.parents:
    raise SystemExit('Use an isolated directory outside the repository')
LAB.mkdir(parents=True, exist_ok=True)
files = [
 'spring-boot/spring-boot-interview.md',
 'spring-boot/spring-boot-conditionalOnProperty.md',
 'spring-boot/spring-boot-active-profile.md',
 'spring-boot/spring-boot-Swagger2.md',
 'spring/spring-data-Jpa-Notes.md', 'spring/spring-transactional.md'
]
def blocks(path):
    return re.findall(r'^```(\w+)\s*\n(.*?)^```\s*$',path.read_text(),re.M|re.S)
pom = next(c for l,c in blocks(ROOT / 'content/post' / files[0]) if l == 'xml')
extra = next(c for l,c in blocks(ROOT / 'content/post' / files[3]) if l == 'xml')
(LAB/'pom.xml').write_text(pom.replace('</dependencies>',extra+'</dependencies>'))
for name in files:
    for lang,code in blocks(ROOT / 'content/post' / name):
        if lang != 'java':
            continue
        definition = re.search(r'\b(?:class|interface)\s+(\w+)',code)
        if not definition: continue
        cls = definition[1]
        category = 'test' if cls.endswith('Test') else 'main'
        p = LAB / 'src' / category / 'java/notes' / (cls+'.java')
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(code)
resources=LAB/'src/main/resources';resources.mkdir(parents=True,exist_ok=True)
(resources/'application.properties').write_text('notes.banner=default\n')
(resources/'application-dev.properties').write_text('notes.banner=development\n')
# The article additionally documents interface methods as fragments.
jpa = blocks(ROOT / 'content/post/spring/spring-data-Jpa-Notes.md')
imports = next(c for l,c in jpa if l == 'java' and 'import org.springframework.data.jpa.repository.Query' in c)
methods = next(c for l,c in jpa if l == 'java' and 'findExactNative' in c)
repo = LAB/'src/main/java/notes/TaskRepository.java'
source = repo.read_text().replace('package notes;', 'package notes;\n'+imports)
source = source.rsplit('}',1)[0]+methods+'}\n'
repo.write_text(source)
# Extra endpoint/profile/query tests are QA fixtures; article tests are extracted.
for fixture in (ROOT/'docs/verification/spring-test/java/notes').glob('*.java'):
    shutil.copy2(fixture,LAB/'src/test/java/notes'/fixture.name)
print('Prepared:',LAB)
