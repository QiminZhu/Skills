import asyncio, json
from playwright.async_api import async_playwright

PAGE = 'file:///root/qm-run/app/data-link-quiz.html'
OUT = '/root/qm-run/'

async def answer(page, wrong):
    q = await page.evaluate('state.qs[state.idx].q')
    t, qid = q['type'], q['id']
    if t in ('single', 'multiple', 'boolean'):
        picks = q['correct'] if not wrong else [i for i in range(len(q['answers'])) if i not in q['correct']][:1]
        for o in picks:
            await page.click(f'input[name="c-{qid}"][value="{o}"]')
    elif t == 'two_tier':
        a = q['answerTier']['correct'][0]
        r = q['reasonTier']['correct'][0] if not wrong else (q['reasonTier']['correct'][0] + 1) % 4
        await page.click(f'input[name="a-{qid}"][value="{a}"]')
        await page.click(f'input[name="r-{qid}"][value="{r}"]')
    elif t == 'matching':
        for l, r in q['matches']:
            await page.select_option(f'#m-{qid}-{l}', str(r))
    elif t == 'ordering':
        await page.click('[data-down="0"]')  # exercise the arrow control once
        await page.evaluate('state.qs[state.idx].seq = state.qs[state.idx].q.correctOrder.slice(); drawOrder(state.qs[state.idx])')
    elif t == 'fill_blank':
        for b in q['blanks']:
            await page.fill(f'#b-{qid}-{b["id"]}', str(b['value']))
    elif t == 'self_explain':
        await page.click('#check')
        assert await page.is_visible('#err'), 'short answer should be rejected'
        await page.fill(f'#se-{qid}', 'Each link can use a different frame type and MAC addresses only work on one link while the IP packet stays the same.')
    if t != 'self_explain':
        await page.click('#check')
        assert await page.is_visible('#err'), 'missing confidence should be rejected'
        await page.click('label.pill:has-text("Certain")' if wrong else 'label.pill:has-text("Fairly sure")')
    await page.click('#check')
    assert await page.is_visible('#next')
    if t == 'self_explain':
        await page.click('[data-ck="0"]')
    return t

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        errors = []
        for width, scheme in ((420, 'light'), (900, 'dark')):
            ctx = await b.new_context(viewport={'width': width, 'height': 900}, color_scheme=scheme)
            page = await ctx.new_page()
            page.on('pageerror', lambda e: errors.append(str(e)))
            await page.goto(PAGE)
            n = await page.evaluate('state.qs.length')
            types = []
            for i in range(n):
                types.append(await answer(page, wrong=(i in (0, 3))))
                if i == 2 and width == 420:
                    await page.screenshot(path=OUT + 'shot-question.png', full_page=True)
                await page.click('#next')
            await page.wait_for_selector('.summary')
            score = await page.inner_text('.score')
            wide = await page.evaluate('document.documentElement.scrollWidth > window.innerWidth')
            hist = await page.evaluate('localStorage.getItem("l9-dll-quiz-v1")')
            await page.screenshot(path=OUT + f'shot-summary-{scheme}.png', full_page=True)
            print(width, scheme, 'types', types, 'score', score.replace('\n', ' '), 'horizontal scroll', wide, 'history saved', bool(hist))
            await page.click('#again')
            first = await page.evaluate('state.qs[0].q.id')
            missed = json.loads(hist)['attempts'][-1]['missed']
            print('retake starts with', first, '| last missed', missed)
        print('page errors:', errors or 'none')
        await b.close()

asyncio.run(main())
