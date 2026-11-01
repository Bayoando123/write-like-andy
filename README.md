# write-like-andy

> Parody side project. Not written, endorsed or affiliated with Andy Burnham in any way.

A toolkit for writing LinkedIn posts with the rhetorical structure Andy Burnham uses: plainspoken, fairness-driven, short-lined, number-backed and honest about limits.

**This kit copies a writing *technique*. It does not impersonate a person.** Use it to write your own posts, in your own name, about your own work.

## What's inside

| Path | What it is |
|---|---|
| `STYLE_GUIDE.md` | The full breakdown: hooks, sentence mechanics, vocabulary, numbers, closers, and 5 post formats |
| `prompts/system-prompt.md` | Drop-in system prompt for Claude or any LLM to rewrite *your* drafts in this style |
| `templates/` | Fill-in-the-blank skeletons for each of the 5 post formats |
| `examples/` | Original example posts written in the style (property / founder topics) |
| `tools/style_check.py` | A zero-dependency linter that scores a draft against the style rules |

## Quick start

```bash
git clone https://github.com/Bayoando123/write-like-andy.git
cd write-like-andy
python tools/style_check.py examples/01-unfairness-fix.md
```

To rewrite a draft with an LLM, paste `prompts/system-prompt.md` as the system prompt, then send your draft as the user message.

## Ground rules

- Don't publish output that is attributed to Andy Burnham, or that could pass as a statement from him.
- Don't invent quotes for him or any other real person.
- Posts written with this kit are yours: your name, your facts, your numbers.

## Licence

MIT for the code and the guide. The analysis references short phrases for commentary purposes. No full posts are reproduced in this repo.
