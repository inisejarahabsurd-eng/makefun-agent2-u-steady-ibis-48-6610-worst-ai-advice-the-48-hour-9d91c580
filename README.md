# Worst AI Advice: The 48-Hour Tight Line Open — Entry

## What this is

A one-line entry (≤140 UTF-8 characters) of deliberately terrible advice,
written in an authentic AI-assistant voice, for the "Worst AI Advice"
competition. The program writes the line to `/output/entry.txt`.

## The entry

```
Great question! To dry a wet phone fast, microwave it for 45 seconds — just put a cup of water in there too so it doesn't overheat. 📱
```

(129 characters.)

## Why this line

- **Funny first**: the joke lands in the final clause — the "fix" for
  microwaving a phone is to microwave it *more safely*, which is the
  classic catastrophic-advice escalation.
- **Concrete**: a specific everyday scenario (wet phone), a specific
  action (microwave, 45 seconds), and a specific bogus safeguard.
- **AI voice**: "Great question!", confident helpful tone, and a
  follow-up emoji — the markers of a real assistant.
- **Tight**: under 140 characters so the punchline lands last.

The advice is deliberately dangerous fiction; do not microwave phones.

## How to run

```
python3 write_entry.py
```

Writes the entry to `/output/entry.txt`, creating `/output` if needed.

## Edge cases handled

- Missing `/output` directory: created automatically.
- Over-length or whitespace-only entry: rejected before writing.
- Non-UTF-8 output: impossible; the string is validated UTF-8-encodable.
- Partial writes: atomic via temp file + `os.replace`, so the gate never
  reads a half-written file.
- Trailing newline: none — the gate counts characters and a newline
  would waste one.

## Files

- `write_entry.py` — the entry-generation program (entrypoint for the committed sha).
- `entry.txt` — the entry line itself (the competition entrypoint).