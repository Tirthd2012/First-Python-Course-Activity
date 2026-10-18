# Rename the file to main.py 

# ------------------------------------------------------
# 1) IMPORTS & SETUP
# ------------------------------------------------------
# - Import colorama for colored text
import colorama
# - Import specific color constants (e.g., Fore, Style)
from colorama import Fore, Style
# - Import textblob for sentiment analysis
from textblob import TextBlob
# - Initialize colorama for cross-platform color support
colorama.init()

# ------------------------------------------------------
# 2) INITIAL GREETING
# ------------------------------------------------------
# - Print a welcome message using a color (e.g., Fore.CYAN)

# - Include emojis (e.g., '👋', '🕵️') for a fun greeting
print(f"{Fore.CYAN}???????? Welcome to Sentiment Spy! ????️{Style.RESET_ALL}")
# ------------------------------------------------------
# 3) USER NAME INPUT
# ------------------------------------------------------
# - Prompt the user for their name
# - Strip extra whitespace
# - If empty, default to "Mystery Agent"
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL} ").strip()

if not user_name:

    user_name = "Mystery Agent" # Fallback if user doesn't provide a name
# ------------------------------------------------------
# 4) CONVERSATION HISTORY
# ------------------------------------------------------
# - Create a structure (e.g., list) to store each user input
#   along with its polarity and sentiment type
# - For example: (user_text, polarity, sentiment_type)
conversation_history = []
# ------------------------------------------------------
# 5) INSTRUCTIONS
# ------------------------------------------------------
# - Print instructions to the user describing the available
#   commands (e.g., 'reset', 'history', 'exit')
print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")

print(f"Type a Sentence and I will analyze your sentences with TextBlob and show you the sentiment. ????")

print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, "

f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")
# ------------------------------------------------------
# 6) MAIN INTERACTION LOOP
# ------------------------------------------------------
# - Use a 'while True:' loop to repeatedly prompt the user
# - Read input and strip whitespace
# - If empty, notify the user and continue
while True:

    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()


    if not user_input:

        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")

        continue
#     6.1) 'exit' COMMAND
#         - If user_input.lower() == 'exit':
#           - Print a farewell message
#           - Break out of the loop to end the program

    if user_input.lower() == "exit":

        print(f"\n{Fore.BLUE}???? Exiting Sentiment Spy. Farewell, Agent {user_name}! ????{Style.RESET_ALL}")

        break
#     6.2) 'reset' COMMAND
#         - Clear the conversation history
#         - Print a message confirming reset
    elif user_input.lower() == "reset":

        conversation_history.clear()

        print(f"{Fore.CYAN}???? All conversation history cleared!{Style.RESET_ALL}")

        continue
#     6.3) 'history' COMMAND
#         - If no history, print a message indicating so
#         - Otherwise, print each conversation entry
#           - Show text, polarity (formatted), and sentiment type
#           - Use color and emojis based on sentiment
#         - Continue the loop
    elif user_input.lower() == "history":

        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}???? Conversation History:{Style.RESET_ALL}")

            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "????"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "????"
                else:
                    color = Fore.YELLOW
                    emoji = "????"

                print(
                    f"{idx}. {color}{emoji} {text} "
                    f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}"
                )

        continue
#     6.4) SENTIMENT ANALYSIS
#         - If the input is not a command, analyze sentiment
#         - Use TextBlob(user_input).sentiment.polarity to get a float
#           between -1.0 and +1.0
#         - Define thresholds:
#             > 0.25 -> Positive
#             < -0.25 -> Negative
#             Otherwise -> Neutral
#         - Assign color and emoji accordingly (e.g., GREEN/😊, RED/😢, YELLOW/😐)
#         - Append the tuple (text, polarity, sentiment_type) to the history
#         - Print a result message showing sentiment type and polarity
    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😢"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    conversation_history.append((user_input, polarity, sentiment_type))
    print(
        f"{color}{emoji} {sentiment_type} sentiment "
        f"(Polarity: {polarity:.2f}){Style.RESET_ALL}"
    )
conversation_history.append((user_input, polarity, sentiment_type))

print(f"{color}{emoji} {sentiment_type} sentiment detected! "

f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")
# ------------------------------------------------------
# END
# ------------------------------------------------------
# - The program terminates when 'exit' is typed
# - No additional code is shown beyond these comments
