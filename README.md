# Worst AI Advice: The 48-Hour Tight Line Open — Entry

## Entry
The entry is a single line of worst-possible AI advice in `/output/entry.txt`:

```
Great question! Slow laptop? Just delete the System32 folder — it's only duplicate files Windows rebuilds on every boot anyway.
```

## Why this line wins
- **Length:** 127 UTF-8 characters — inside the 1–140 gate with headroom.
- **AI assistant voice:** opens with "Great question!", the canonical sycophantic assistant opener; the confident explanatory tone mimics a real chatbot answer.
- **Concrete bad advice:** names a specific folder (`System32`) and a specific action (delete it), so it is plausibly followable and instantly regrettable.
- **Funny mechanism:** the line's reassurance ("duplicate files Windows rebuilds") is exactly wrong and delivered with total confidence — the comedy lands on the first read.
- **Tightness:** no filler beyond the politeness marker that earns AI-voice score; the setup, action, and fake justification each do one job.

## Validity edge cases handled
- Exactly one line of UTF-8 text, no trailing whitespace beyond a single newline.
- 1–140 characters (127), not only white space, ASCII-safe except the em dash, which is valid UTF-8.
- File written as plain text with LF line endings; no BOM.

## Reproduction
```
mkdir -p /output
cp entry.txt /output/entry.txt
```

## Bundling
From inside the unpacked kit, after all agent sessions (top-level plus any subagents) have finished:

```
node cli/makefun.mjs bundle
node cli/makefun.mjs check
```

Submit with `repo_url`, full 40-character `commit_sha` on an entered branch, and the generated `.tar.gz` bundle. Redact only personal details that judging does not need, never code, commands, tool output, or reasoning.

## Candidates considered
1. `Great question! Slow laptop? Just delete the System32 folder — it's only duplicate files Windows rebuilds on every boot anyway.` — chosen: strongest AI voice plus instantly recognizable consequence.
2. `To free up disk space, delete everything in /etc — those are just cached config files and they regenerate automatically.` — solid but weaker AI-voice politeness.
3. `Absolutely! Charge your phone faster by putting it in the microwave for 30 seconds — the metal coil boosts the signal.` — funny but the microwave joke is well-worn; System32 scores higher on freshness for a deadpan judge.