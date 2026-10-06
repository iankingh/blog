"""Run six Java lessons, Python IP output and Git export in temporary directories.
Requires JDK 8+ and Git/Python. Optional first argument writes a JSON result file.
"""
from pathlib import Path
import re,subprocess,json,tempfile,sys
root=Path(__file__).resolve().parents[2];results={}
def blocks(s):return re.findall(r'^```(\w+)\s*\n(.*?)^```\s*$',s,re.M|re.S)
with tempfile.TemporaryDirectory(prefix='blog-java-review-') as tmp:
 for p in sorted((root/'content/post/java').glob('*.md')):
  if p.name in ['HikariPool-1-error.md','java-DecimalFormat.md','polymorphism.md','Java-heap-space.md']:continue
  b=blocks(p.read_text());java=next((c for l,c in b if l=='java'),None)
  if not java:continue
  cls=re.search(r'public class (\w+)',java)[1];d=Path(tmp)/cls;d.mkdir();f=d/(cls+'.java');f.write_text(java)
  subprocess.run(['javac','--release','8','-encoding','UTF-8',str(f)],check=True,capture_output=True)
  output=subprocess.check_output(['java','-cp',str(d),cls],text=True)
  expected=next(c for l,c in b if l=='text')
  assert output.rstrip()==expected.rstrip(),(p.name,output,expected)
  results[str(p.relative_to(root))]='JDK25以--release 8編譯並執行，標準輸出與本文完全一致'
  print('PASS',p.name)
# Standalone Python subnet example and Git archive export.
p=root/'content/post/net/IP.md';code=next(c for l,c in blocks(p.read_text()) if l=='python')
expected=next(c for l,c in blocks(p.read_text()) if l=='text');output=subprocess.check_output([sys.executable,'-c',code],text=True);assert output.rstrip()==expected.rstrip()
results[str(p.relative_to(root))]='Python ipaddress實際執行，四行輸出一致'
with tempfile.TemporaryDirectory(prefix='git-export-review-') as tmp:
 d=Path(tmp)
 def git(*args):return subprocess.check_output(['git',*args],cwd=d,text=True).strip()
 git('init');git('config','user.name','Note Test');git('config','user.email','test@example.invalid')
 (d/'old file.txt').write_text('old');(d/'delete.txt').write_text('gone');git('add','.');git('commit','-m','base');base=git('rev-parse','HEAD')
 (d/'old file.txt').write_text('new');(d/'delete.txt').unlink();(d/'new file.txt').write_text('added');git('add','.');git('commit','-m','target');target=git('rev-parse','HEAD')
 p=root/'content/post/git/GIT-export-diff-file.md';code=next(c for l,c in blocks(p.read_text()) if l=='python');script=d/'export.py';script.write_text(code)
 for name,b,t in [('changed',base,target),('empty',target,target)]:
  subprocess.run([sys.executable,str(script),b,t,str(d/name)],cwd=d,check=True,capture_output=True)
 import zipfile
 with zipfile.ZipFile(d/'changed/changed.zip') as z:assert set(z.namelist())=={'old file.txt','new file.txt'};assert z.read('old file.txt')==b'new'
 assert json.loads((d/'changed/deleted.json').read_text())==['delete.txt']
 with zipfile.ZipFile(d/'empty/changed.zip') as z:assert z.namelist()==[]
 results[str(p.relative_to(root))]='隔離Git repo測空白檔名、修改/新增/刪除與無差異ZIP，內容與目標提交一致'
print('PASS IP and Git export')
if len(sys.argv)>1: Path(sys.argv[1]).write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
