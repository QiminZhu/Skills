const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const script = html.match(/<script>\n([\s\S]*?)<\/script>/)[1];
function setup(bridge) {
  const fields = {};
  const field = name => fields[name] ||= {hidden: true, disabled: false, value: '', textContent: '', handlers:{},addEventListener(event, fn){this.handlers[event]=fn;}};
  let selected = null;
  const root = {querySelector(selector){return selector==='input:checked' ? selected : field(selector);}};
  const window = bridge ? {openai: {sendFollowUpMessage:bridge}} : {};
  vm.runInNewContext(script, {document:{getElementById(){return root;}}, window});
  return {fields, field, select(id){selected={value:id};field('form').handlers.change();},submit(){field('form').handlers.submit({preventDefault(){}});},next(){return field('[data-next]').handlers.click();},challenge(){return field('[data-challenge]').handlers.click();}};
}
(async () => {
  let calls=[];
  let u=setup(async value=>calls.push(value));
  assert.equal(u.field('[data-explanation]').hidden,true);
  assert.equal(calls.length,0);
  u.submit();assert.match(u.field('[data-status]').textContent,/Choose/);
  u.select('wrong');u.submit();assert.match(u.field('[data-result]').textContent,/^Incorrect/);
  assert.equal(u.field('[data-explanation]').hidden,false);assert.equal(calls.length,0);
  u.select('right');assert.equal(u.field('[data-explanation]').hidden,true);
  u.submit();assert.match(u.field('[data-result]').textContent,/^Correct/);
  assert.equal(calls.length,0);await u.next();await u.next();assert.equal(calls.length,1);
  assert.match(calls[0].prompt,/source|Source/);assert.match(calls[0].prompt,/"correct":true/);
  u=setup();u.select('right');u.submit();await u.next();
  assert.equal(u.field('[data-manual]').hidden,false);assert.match(u.field('[data-status]').textContent,/unavailable/);
  let count=0;
  u=setup(async()=>{if(++count===1)throw Error('unavailable');});
  await u.next();assert.equal(u.field('[data-next]').disabled,false);await u.next();assert.equal(count,2);
  calls=[];u=setup(async v=>calls.push(v));u.select('wrong');u.submit();await u.challenge();
  assert.equal(calls.length,1);assert.match(calls[0].prompt,/recheck/);
  assert(!/localStorage|sessionStorage|fetch\(|XMLHttpRequest|setWidgetState/.test(script));
  console.log('Practice runtime: 20 checks passed (local grading, feedback, separate Next, duplicate prevention, grade challenge, fallback and retry).');
})();
