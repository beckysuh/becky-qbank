// Portable progress backup. Question content and resource images are not exported.
const BACKUP_FORMAT='becky-qbank-progress';
let pendingImport=null;
function validateBackup(value){
 if(!value||value.format!==BACKUP_FORMAT||value.version!==1)throw Error('This is not a supported Becky Qbank backup.');
 const incoming=value.state;
 if(!incoming||incoming.version!==1||!incoming.history||typeof incoming.history!=='object'||Array.isArray(incoming.history))throw Error('The backup has invalid progress data.');
 const history={};
 for(const [id,h] of Object.entries(incoming.history)){
  if(!/^[a-zA-Z0-9_.:-]{1,150}$/.test(id)||!h||typeof h.latestCorrect!=='boolean'||typeof h.everMissed!=='boolean'||!Number.isSafeInteger(h.attempts)||h.attempts<1||(!h.latestCorrect&&!h.everMissed))throw Error('The backup contains an invalid answer record.');
  Object.defineProperty(history,id,{value:{latestCorrect:h.latestCorrect,everMissed:h.everMissed,attempts:h.attempts},enumerable:true,writable:true,configurable:true});
 }
 let session=null,sessionSkipped=false;
 if(incoming.session!=null){
  const s=incoming.session;
  if(!s||!Array.isArray(s.ids)||!s.ids.length||s.ids.some(id=>typeof id!=='string')||new Set(s.ids).size!==s.ids.length||!s.answers||typeof s.answers!=='object'||Array.isArray(s.answers)||!Number.isInteger(s.index)||s.index<0||s.index>=s.ids.length)throw Error('The backup has an invalid saved test.');
  const answers={};
  for(const [id,a] of Object.entries(s.answers)){
   const q=BANK.find(q=>q.id===id);
   if(!s.ids.includes(id)||!a||!Number.isInteger(a.choice)||a.choice<0||a.choice>3||typeof a.correct!=='boolean'||(q&&a.correct!==(a.choice===q.correct))||!history[id]||history[id].latestCorrect!==a.correct)throw Error('The saved test contains an invalid answer.');
   answers[id]={choice:a.choice,correct:a.correct};
  }
  if(s.ids.every(id=>BANK.some(q=>q.id===id)))session={ids:[...s.ids],answers,index:s.index};else sessionSkipped=true;
 }
 return {state:{version:1,history,session,source:incoming.source==='nbme'?'nbme':'all'},sessionSkipped};
}
function progressBackup(){return {format:BACKUP_FORMAT,version:1,exportedAt:new Date().toISOString(),state:JSON.parse(JSON.stringify(state))};}
function exportProgress(){
 const url=URL.createObjectURL(new Blob([JSON.stringify(progressBackup(),null,2)],{type:'application/json'}));
 const a=document.createElement('a');a.href=url;a.download='becky-qbank-progress-'+new Date().toISOString().slice(0,10)+'.json';document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);
 $('#backup-status').textContent='Backup downloaded. Keep it somewhere you can find again.';
}
async function prepareImport(file){
 pendingImport=null;$('#backup-status').textContent='';if(!file)return;
 try{
  if(file.size>10*1024*1024)throw Error('This file is too large for a progress backup.');
  pendingImport=validateBackup(JSON.parse(await file.text()));
  const n=Object.keys(pendingImport.state.history).length;
  $('#import-summary').textContent=`This backup has ${n} answered questions. Importing replaces your current answer history and saved test.`+(pendingImport.sessionSkipped?' Its saved test uses questions unavailable here and will not be restored.':'');
  $('#import-dialog').showModal();
 }catch(e){$('#backup-status').textContent=e instanceof SyntaxError?'Could not read this JSON backup.':e.message;}
 finally{$('#import-file').value='';}
}
function applyImport(){
 if(!pendingImport)return false;
 // Write first: a quota/storage failure must not replace the current in-memory state.
 try{localStorage.setItem(KEY,JSON.stringify(pendingImport.state));}catch{$('#backup-status').textContent='Import failed: browser storage is unavailable. Your current progress is unchanged.';pendingImport=null;$('#import-dialog').close();return false;}
 state=pendingImport.state;source=state.source;pendingImport=null;pool='all';index=0;selected=new Set(['Cardiovascular']);
 document.querySelector(`input[name="source"][value="${source}"]`).checked=true;document.querySelector('input[name="pool"][value="all"]').checked=true;
 $('#explanation-content').replaceChildren();$('#explanation').hidden=true;$('#import-dialog').close();showCreate();$('#backup-status').textContent='Progress imported.';return true;
}
$('#export-progress').onclick=exportProgress;
$('#import-progress').onclick=()=>$('#import-file').click();
$('#import-file').onchange=e=>prepareImport(e.target.files[0]);
$('#cancel-import').onclick=()=>{pendingImport=null;$('#import-dialog').close();};
$('#import-dialog').addEventListener('cancel',()=>{pendingImport=null;});
$('#confirm-import').onclick=applyImport;
