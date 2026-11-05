const fs=require('fs'),vm=require('vm'),assert=require('assert');
const bank=JSON.parse(fs.readFileSync('work/qbank-data.json','utf8'));
class El{constructor(){this.value='20';this.classList={toggle(){}};this.hidden=false;this.textContent='';this.innerHTML='';}querySelector(){return new El()}addEventListener(){}replaceChildren(){this.innerHTML=''}showModal(){this.open=true}close(){this.open=false}click(){}remove(){}}
const els=new Map(),el=s=>{if(!els.has(s))els.set(s,new El());return els.get(s)};
let download=null,blob=null,failWrite=false;
const document={getElementById:id=>({textContent:id==='question-data'?JSON.stringify(bank):'{}'}),querySelector:el,body:{appendChild(a){download=a}},createElement:()=>new El()};
const store={},localStorage={getItem:k=>store[k]||null,setItem(k,v){if(failWrite)throw Error('quota');store[k]=v}};
const URL={createObjectURL(b){blob=b;return 'blob:test'},revokeObjectURL(){}};
const c=vm.createContext({document,localStorage,console,Set,Math,Date,Blob,URL,setTimeout:f=>f()});
vm.runInContext(fs.readFileSync('work/qbank-app.js','utf8')+'\n'+fs.readFileSync('work/qbank-progress.js','utf8'),c);
const run=s=>vm.runInContext(s,c),id=bank[0].id;
(async()=>{
run(`state.history[${JSON.stringify(id)}]={latestCorrect:false,everMissed:true,attempts:2};state.source='nbme';state.session={ids:[${JSON.stringify(id)}],answers:{[${JSON.stringify(id)}]:{choice:${(bank[0].correct+1)%4},correct:false}},index:0}`);
const original=run('JSON.stringify(state)');run('exportProgress()');assert.match(download.download,/becky-qbank-progress-.*\.json/);const exported=JSON.parse(await blob.text());assert.equal(exported.format,'becky-qbank-progress');assert.equal(JSON.stringify(exported.state),original);assert(!('questions' in exported));
run('state={version:1,history:{},session:null}');
await run(`prepareImport({size:100,text:async()=>${JSON.stringify(JSON.stringify(exported))}})`);
assert(el('#import-dialog').open);assert.equal(run('Object.keys(state.history).length'),0); // Preview must not change state.
assert(run('applyImport()'));assert.equal(run('JSON.stringify(state)'),original);assert.equal(run('source'),'nbme');
const valid=JSON.stringify(exported);
for(const bad of [{}, {...exported,version:99},{...exported,state:{...exported.state,history:{bad:{latestCorrect:'yes',everMissed:false,attempts:0}}}}]){assert.throws(()=>run(`validateBackup(${JSON.stringify(bad)})`));}
await run("prepareImport({size:2,text:async()=>'{x'})");assert.match(el('#backup-status').textContent,/Could not read/);assert.equal(run('JSON.stringify(state)'),original);
await run("prepareImport({size:20000000,text:async()=>''})");assert.match(el('#backup-status').textContent,/too large/);
const unknown=JSON.parse(valid);unknown.state.session.ids.push('future-question');unknown.state.history['future-question']={latestCorrect:true,everMissed:false,attempts:1};
const clean=run(`validateBackup(${JSON.stringify(unknown)})`);assert(clean.sessionSkipped);assert.equal(clean.state.session,null);assert(clean.state.history['future-question']);
await run(`prepareImport({size:100,text:async()=>${JSON.stringify(valid)}})`);run("$('#cancel-import').onclick()");assert.equal(run('pendingImport'),null);assert.equal(run('JSON.stringify(state)'),original);
await run(`prepareImport({size:100,text:async()=>${JSON.stringify(valid)}})`);failWrite=true;assert.equal(run('applyImport()'),false);failWrite=false;assert.equal(run('JSON.stringify(state)'),original);
const corrupt=JSON.parse(valid);corrupt.state.session.answers[id].correct=true;assert.throws(()=>run(`validateBackup(${JSON.stringify(corrupt)})`));
console.log('Passed: backup download/content, preview-before-replacement, round-trip history/session/source, malformed and oversized files, cancellation, unknown question IDs, inconsistent answers, and storage-failure preservation.');
})().catch(e=>{console.error(e);process.exit(1)});
