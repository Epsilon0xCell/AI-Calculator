# AI-Calculator roadmap

Written 2026-10-30 from the repo as it stands at 6e392ec. No
dates on the future items, because I do not know when I will be
back in this code, and a date I invent here would be a small lie
in a public file.

## Done

- The whole program in ai_calculator.py: a ChatterBot named
  Calculator, read_only on, only the MathematicalEvaluation logic
  adapter, SQL storage.
- The chat loop moved into main(), the bot setup split into
  build_bot(), and the quit match split into is_quit(text), in
  commit 6e392ec. The import guard now lives inside build_bot():
  a missing ChatterBot prints one install hint to stderr and
  exits 1, no traceback.
- The entry guard: sys.exit(main()) runs only when the file is
  run directly, so importing ai_calculator.py starts nothing
  and tests can import is_quit safely.
- The empty-line skip, in commit 6e392ec: a line that is empty
  after stripping is skipped and the prompt returns, instead
  of being sent to the adapter.
- Clean exits: quit in any case with spaces ignored, EOF, and
  Ctrl-C all print Exiting. main() returns 0 on a normal end.
- First tests, in test_ai_calculator.py at 6e392ec: 4 unittest
  tests covering plain quit, case and spaces, other text that
  is not quit, and (on a machine without ChatterBot) the
  missing dependency path.
- First-person comments recording why the settings and the wide
  error catch are the way they are, including the cost of the
  catch.
- The README with the behaviour verified by testing and the
  honest limits section, plus requirements.txt and these visuals.

## Working now

- Nothing in flight. No TODO or FIXME notes exist anywhere in
  the code, checked 2026-10-30.

## Next

- One verified end-to-end maths answer on a current Python. The
  README records that this has not been re-verified: ChatterBot
  1.0.5 has old pinned dependencies, and in the last test
  environment its NLTK downloads were blocked, so every question
  landed in the error reply. Until that run happens, the maths
  answering stands as provided by the library, not as verified
  by me.
- A test for the empty-line skip in the loop itself, if the
  loop can be driven without a working ChatterBot install.
  The current tests cover is_quit and the missing install, not
  the loop in main().

## Later

- Nothing honest to put here yet. Any change to the library
  underneath, or to how the loop handles its errors, waits on
  the verification above.

## Not planned

- General chat. Loading another logic adapter would change what
  this is; the one-adapter setup is the point.
- Letting the bot learn from input. read_only stays on, so the
  replies do not drift.
- A graphical interface. The terminal is the interface I use.
