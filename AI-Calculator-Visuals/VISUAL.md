# AI-Calculator, drawn out

I made these five pictures because the whole program now fits in
one honest frame: three functions in ai_calculator.py (99
lines), where build_bot() sets up one ChatterBot for maths only,
is_quit(text) does the clean quit match, and main() holds the
greeting and the chat loop, with empty lines skipped before they
reach the bot.

## The visuals

- [architecture.svg](architecture.svg): the shape. The terminal
  on the left, the three functions as a stack in the middle, and
  ChatterBot plus its db.sqlite3 file on the right, with the
  entry guard stated under the stack.
- [sequence.svg](sequence.svg): one question followed across
  three lanes, from the me: prompt through main() to the printed
  answer, with the error path, the empty-line skip, and the quit
  path stated under it.
- [flowchart.svg](flowchart.svg): the loop in main() as
  decisions. build_bot() and its install check, the greeting,
  input, the EOF and Ctrl-C check, the is_quit check, the new
  empty-line skip, and the wide error catch that sends the loop
  around again.
- [product-map.svg](product-map.svg): the product in one frame:
  who it serves, what it does, what it does not do, and where it
  stops.
- [statistics.svg](statistics.svg): the numbers from the table
  below, drawn as bars on paper, with the LICENSE honestly the
  biggest bar in the repo.

Each sheet also ships as a PNG beside its SVG: the same drawing,
finished as a photograph of the paper page.

Every sheet here is drawn to look like what it is: a page sketched
by hand on paper, and each one is signed GK somewhere in the
drawing, never twice in the same place, because that is what I do
with a page I made.

## Written product map

What it is: a terminal calculator chatbot in Python. It wraps
ChatterBot with only its MathematicalEvaluation logic adapter, in
read-only mode, so I type a maths question at the prompt and the
bot answers in the same terminal. The maths itself is the
library's, not something this repo re-implements, and the README
says so.

Who it serves: me, at a terminal, wanting a quick maths answer
without leaving it.

How it is built now:

- build_bot() holds the import guard and the bot setup. If
  ChatterBot is missing it prints one install hint to stderr and
  exits 1, with no traceback. If it is present it returns a
  ChatBot named Calculator, read_only True, with only the
  MathematicalEvaluation logic adapter and SQL storage.
- is_quit(text) returns True only when strip().lower() on the
  line gives quit, so QUIT and a quit line with spaces around
  it also exit, and other text does not.
- main() builds the bot, prints an ANSI reset and then the
  greeting, and runs the loop. It returns 0 on a normal end.
  The entry guard at the bottom runs sys.exit(main()) only
  when the file is run directly, so importing the file starts
  nothing.

Capabilities, grouped:

- Asking and answering: each non-empty line typed at the me:
  prompt goes to bot.get_response and the reply prints as a
  Calculator: line.
- Skipping empty input: a line that is empty after stripping
  is skipped with continue and the prompt comes back, instead
  of being sent to the adapter as a question.
- Staying on maths: only the MathematicalEvaluation adapter is
  loaded, so a line the adapter cannot treat as maths has
  nowhere else to go and lands in the error reply.
- Not learning: read_only is on, so the bot does not learn from
  what gets typed at it and its replies do not drift.
- Leaving cleanly: quit (any case, surrounding spaces ignored),
  closing the input, and Ctrl-C all print Exiting and end the
  loop, with no traceback.
- Failing plainly at start: if ChatterBot is not installed,
  build_bot() prints one short line to stderr with the install
  hint and the program exits 1 instead of dumping a traceback.

Inputs: lines typed at the prompt. First use also needs the
network once, for the NLTK data files ChatterBot downloads.
Outputs: Calculator: lines on stdout, and a db.sqlite3 file the
SQL storage adapter creates in the folder the calculator runs
from, even in read-only mode.

Boundaries, what it does NOT do: no general chat, no other logic
adapter, no learning, no interface beyond the terminal. One limit
I keep on the record: the wide except around get_response also
hides failures inside the library itself, so a sound maths
question can get the valid-input reply when the library is the
part that broke. The README records a verified run where exactly
that happened on every question, because ChatterBot 1.0.5 and its
pinned dependencies are too old for a clean current install and
its NLTK downloads were blocked in that sandbox. A correct
end-to-end maths answer was not re-verified there, and I do not
claim one here.

Tests in the repo now: test_ai_calculator.py holds 4 unittest
tests. Three cover is_quit (plain quit, case and spaces, and
other text that is not quit). One covers the missing dependency
path: on a machine without ChatterBot it runs the program in a
subprocess and checks exit 1, the hint on stderr, and no
traceback; that test is skipped if ChatterBot is installed.

## Statistics, with citations

Counted 2026-10-30, from the clone this folder ships in, at the
commit before this visuals commit (6e392ec).

| Number | Value | How it was counted, and from what |
|---|---|---|
| Files in the repo | 7 | git ls-files in the clone, counted 2026-10-30 |
| Python lines | 144 | Line count over the 2 tracked .py files (ai_calculator.py 99 lines and test_ai_calculator.py 45 lines), by wc -l style counting over tracked files, binary and image files excluded, 2026-10-30 |
| Markdown lines | 72 | Line count over the 1 tracked .md file (README.md), same method, 2026-10-30 |
| Text lines | 1 | Line count over the 1 tracked .txt file (requirements.txt), same method, 2026-10-30 |
| No-extension lines | 674 | Line count over the 1 tracked file with no extension (LICENSE, GPL v3), same method, 2026-10-30 |
| Commits | 6 | git log in the clone, counted 2026-10-30 |
| First commit | 2023-02-11 | git log, oldest entry, 2026-10-30 |
| Last commit before this one | 2026-10-30 | git log, newest entry, date in America/Chicago for commit 6e392ec (timestamped 2026-10-31 01:38 UTC), 2026-10-30 |
| Tests | 4 tests, ran and passed here under unittest | Observed 2026-10-30: python3 -m unittest -v in the clone ran 4 tests and reported OK, and python3 -m unittest test_ai_calculator -v gave the same result. python3 -m pytest test_ai_calculator.py could not run because pytest is not installed in this sandbox (No module named pytest). ChatterBot is not installed here either, which is the condition the missing dependency test checks, so that test ran and was not skipped. No other test result is claimed. |
| Languages (API) | Python 5,112 bytes | GitHub API, GET /repos/Epsilon0xCell/AI-Calculator/languages, read 2026-10-30 |
| Repo size (API) | 141 KB | GitHub API, GET /repos/Epsilon0xCell/AI-Calculator, size field, read 2026-10-30 |
| Stars / forks (API) | 1 / 0 | Same API response, read 2026-10-30 |

External statistics: none. No outside number says anything honest
about this repo, so the repo's own numbers are the whole table.

## Roadmap summary

Done: the calculator loop moved into main(), build_bot() and
is_quit() split out, the empty-line skip, the entry guard that
makes the file safe to import, and a first test file covering
quit matching and the missing install. Working now: nothing in
flight. Next, if I return to it: getting one verified end-to-end
maths answer on a current Python, which the README records as
still unverified. The full roadmap, with the Later and Not
planned sections, is in [ROADMAP.md](ROADMAP.md).
