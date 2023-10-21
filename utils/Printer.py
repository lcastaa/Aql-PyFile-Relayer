# Printer.py is responsible for output put on the terminal uses the Colorizer.py to style the text
# Created By Luis Castaneda
from utils import Colorizer


# Prints a header
def print_header(label):
    print(Colorizer.yellow('╔════════════════ ════════════════╗'))
    print(f'{label}')
    print(Colorizer.yellow('╚════════════════ ════════════════╝'))


def print_top_border():
    print(Colorizer.yellow('╔════════════════ ════════════════╗'))


def print_bottom_border():
    print(Colorizer.yellow('╚════════════════ ════════════════╝'))


# Prints an error
def print_error(prompt):
    print(Colorizer.red(prompt))


# Prints success message
def print_success(prompt):
    print(Colorizer.green(prompt))


# Takes in a list of options ['opt1','opt2',...] and prints menu
def print_menu(options):
    print(Colorizer.yellow("╔══════════════ •●• ══════════════╗"))
    for i, option in enumerate(options):
        print(f'   --[{i + 1}]--   {option}')
    print(Colorizer.yellow("╚══════════════ •●• ══════════════╝ "))


# Prompts user and returns Int value
def prompt_for_int(prompt):
    user_input = int(input(Colorizer.cyan(prompt)))
    return user_input


# prints a 'yes or no' prompt and returns a boolean value of choice
def prompt_for_bool(prompt):
    choice = input(Colorizer.cyan(prompt)).lower()
    if choice == 'y':
        return True
    elif choice == 'n':
        return False
    else:
        print('Invalid Response...Try Again')
        prompt_for_bool(prompt)


# Prompts user and collects user response returns a String value
def prompt_for_input(prompt):
    user_input = input(Colorizer.cyan(prompt))
    return user_input
