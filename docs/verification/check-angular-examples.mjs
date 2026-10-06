import fs from 'node:fs';import path from 'node:path';import assert from 'node:assert/strict';import {spawnSync} from 'node:child_process';
import '@angular/compiler';
const root=process.env.BLOG_NOTES_ROOT;const runtime=path.dirname(new URL(import.meta.url).pathname);const dir=runtime+'/angular';fs.mkdirSync(dir,{recursive:true});
const fixtures=[];const results=fs.existsSync(process.env.BLOG_RESULTS || '/tmp/blog-example-results.json') ? JSON.parse(fs.readFileSync(process.env.BLOG_RESULTS || '/tmp/blog-example-results.json','utf8')) : {};
for(const name of fs.readdirSync(root+'/content/post/angular')){
 const text=fs.readFileSync(root+'/content/post/angular/'+name,'utf8');let i=0;
 for(const m of text.matchAll(/^```typescript\s*\n([\s\S]*?)^```\s*$/gm)){
  const f=name.replace('.md','')+'-'+i+++'.ts';fs.writeFileSync(dir+'/'+f,m[1]);fixtures.push({f,name,code:m[1]});
 }
}
fs.writeFileSync(dir+'/home.component.ts',"import {Component} from '@angular/core'; @Component({selector:'app-home',standalone:true,template:'Home'}) export class HomeComponent {}\n");
fs.writeFileSync(dir+'/about.component.ts',"import {Component} from '@angular/core'; @Component({selector:'app-about',standalone:true,template:'About'}) export class AboutComponent {}\n");
const js=fs.readFileSync(root+'/content/post/angular/AngularUseJavaScript.md','utf8').match(/^```javascript\s*\n([\s\S]*?)^```\s*$/m)[1];fs.writeFileSync(dir+'/greeting.js',js);
const types=fs.readFileSync(root+'/content/post/angular/AngularUseJavaScript.md','utf8').match(/^```typescript\s*\n([\s\S]*?)^```\s*$/m)[1];
fs.writeFileSync(dir+'/tsconfig.json',JSON.stringify({compilerOptions:{target:'ES2022',module:'ES2022',moduleResolution:'bundler',strict:true,allowJs:true,checkJs:true,experimentalDecorators:true,skipLibCheck:true,outDir:'dist',lib:['ES2022','DOM']},angularCompilerOptions:{strictTemplates:true},include:['*.ts','*.js']},null,2));
const compile=spawnSync(process.execPath,[runtime+'/node_modules/@angular/compiler-cli/bundles/src/bin/ngc.js','-p',dir+'/tsconfig.json'],{encoding:'utf8',timeout:30000});assert.equal(compile.status,0,compile.stdout+compile.stderr);
for(const row of fixtures)results['content/post/angular/'+row.name]='Angular 20.3 ngc strict／strictTemplates 編譯通過；輔助路由元件為本地最小 fixture，未跑完整 CLI／瀏覽器';
const {AppComponent:Reactive}=await import('./angular/dist/Angular-forms-0.js');const a=new Reactive();a.submit();assert.equal(a.result,'');a.form.setValue({name:'Ian',email:'bad'});assert(a.form.invalid);a.form.setValue({name:'Ian',email:'ian@example.test'});a.submit();assert.deepEqual(JSON.parse(a.result),{name:'Ian',email:'ian@example.test'});a.form.reset();assert.equal(a.form.controls.name.value,'');
const {AppComponent:Template}=await import('./angular/dist/Angular-forms-Template-Driven-Forms-0.js');const b=new Template();b.name='  ';b.submit();assert.equal(b.result,'請輸入有效名稱');b.name=' Ian ';b.submit();assert.equal(b.result,'你好 Ian');
const {PipeDemoComponent,CustomPipe}=await import('./angular/dist/Angular-NullInjectorError-2.js');assert.equal(new PipeDemoComponent(new CustomPipe()).normalized(),'Ian');
const {ImageService}=await import('./angular/dist/angular-resize-base64-image-0.js');await assert.rejects(new ImageService().resize('',0,1),/尺寸必須為正數/);
const {example}=await import('./angular/dist/AngularUseJavaScript-0.js');assert.equal(example,'你好 Ian');
for(const name of ['Angular-forms.md','Angular-forms-Template-Driven-Forms.md','Angular-NullInjectorError.md','angular-resize-base64-image.md','AngularUseJavaScript.md'])results['content/post/angular/'+name]+='；執行表單驗證／提交、pipe 方法、圖片無效尺寸或 JS 匯入對應分支（沒有驗證 Canvas 畫素輸出）';
fs.writeFileSync(process.env.BLOG_RESULTS || '/tmp/blog-example-results.json',JSON.stringify(results,null,2));console.log('PASS',fixtures.length,'Angular TS fences, strict templates and isolated class behavior');
