# I wrote this file as a script that runs top to bottom. The loop now
# sits inside main() and the bot is built by build_bot(), so importing
# this file for tests starts nothing; running it directly behaves as
# before.
import sys


def build_bot():
    """Create the calculator bot, or exit 1 with a hint if the
    ChatterBot install is missing.

    I check for ChatterBot before anything else runs. Without it
    there is no calculator at all, so a missing install gets one
    short line on stderr and exit 1 instead of a traceback. I keep
    the hint off stdout because stdout is where the conversation
    with the bot happens.
    """
    try:
        from chatterbot import ChatBot
    except ImportError:
        print(
            "Calculator: ChatterBot is not installed. Install it with: pip install -r requirements.txt",
            file=sys.stderr,
        )
        sys.exit(1)

    # read_only is the setting in this call that matters most to me.
    # I do not want the bot learning from whatever gets typed at it,
    # because then its replies would drift over time instead of
    # staying on maths. I also give it only the MathematicalEvaluation
    # adapter on purpose. With no general chat adapter in the list, a
    # line the adapter cannot treat as maths has nowhere else to go
    # and lands in the error reply at the bottom of the loop.
    # The SQL storage adapter still creates a db.sqlite3 file in the
    # folder I run this from, even in read-only mode. Running the
    # calculator leaves that file behind.
    return ChatBot(
        name="Calculator",
        read_only=True,
        logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
    )


def is_quit(text):
    # I compare a cleaned copy of the line, not the raw line. An
    # earlier version compared the raw input and missed " quit " with
    # spaces around it, and "QUIT" in capitals never matched either.
    return text.strip().lower() == "quit"


def main():
    bot = build_bot()

    # The escape below resets the terminal so the greeting is the
    # first thing on screen. It is an ANSI sequence, not a portable
    # clear command. In a terminal that does not understand it the
    # greeting still prints, just without the clear first.
    print("\033c")
    print("Hello, I am a calculator. How may I help you?")
    while True:
        # Every way out of this loop prints the same word. I want
        # closing the input, pressing Ctrl-C, and typing quit to look
        # identical from the outside, because a scripted run that runs
        # out of input is a normal end here, not an error.
        try:
            user_input = input("me: ")
        except (EOFError, KeyboardInterrupt):
            print("Exiting")
            break

        if is_quit(user_input):
            print("Exiting")
            break

        # An empty line is not a maths question. Sending it to the
        # adapter used to produce the same "valid input" reply as a
        # real failure, so I skip it here and just prompt again.
        if not user_input.strip():
            continue

        # I catch Exception here instead of one named ChatterBot
        # error, because the library raises different errors for
        # input it cannot evaluate and I have no stable list of them
        # to catch. The cost is real and I accept it knowingly: this
        # catch also hides failures inside the library itself, so a
        # sound maths question can get the "valid input" reply when
        # the library is the part that broke. The README records a
        # test run where exactly that happened on every question.
        try:
            response = bot.get_response(user_input)
            print("Calculator:", response)
        except Exception:
            print("Calculator: Please enter valid input.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
