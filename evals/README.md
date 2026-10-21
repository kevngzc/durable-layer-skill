# Evals

One prompt per mode. Run each in a fresh session with the skill installed and check the answer against its list. A miss is a skill bug: fix the reference, not the prompt.

```bash
claude -p "$(sed -n '/^> /s/^> //p' evals/01-assess.md)" --output-format json | jq -r .result
```

| File | Mode | Language |
|---|---|---|
| `01-assess.md` | Assess | EN |
| `02-template.md` | Fill a template | EN |
| `03-review.md` | Review | EN |
| `04-roadmap.md` | Roadmap | EN |
| `05-french.md` | Assess (short) | FR |
