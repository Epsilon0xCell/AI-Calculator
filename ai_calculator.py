import sys

try:
    from chatterbot import ChatBot
except ImportError:
    print("Calculator: ChatterBot is not installed. Install it with: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

# naming the ChatBot calculator
# using mathematical evaluation logic
# the calculator AI will not learn with the user input
Bot = ChatBot(name = 'Calculator',
                read_only = True,                  
                logic_adapters = ["chatterbot.logic.MathematicalEvaluation"],                 
                storage_adapter = "chatterbot.storage.SQLStorageAdapter")
    

# clear the screen and start the calculator
print('\033c')
print("Hello, I am a calculator. How may I help you?")
while (True):
    # take the input from the user
    # closing the input (EOF) or pressing Ctrl-C exits cleanly, like quit
    try:
        user_input = input("me: ")
    except (EOFError, KeyboardInterrupt):
        print("Exiting")
        break

    # check if the user has typed quit to exit the prgram
    if user_input.strip().lower() == 'quit':
        print("Exiting")
        break

    # otherwise, evaluate the user input
    # print invalid input if the AI is unable to comprehend the input
    try:
        response = Bot.get_response(user_input)
        print("Calculator:", response)
    except Exception:
        print("Calculator: Please enter valid input.")
