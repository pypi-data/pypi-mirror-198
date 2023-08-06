import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from .sort import main as sort_directory
from .addressbook import main as addressbook
from .notebook import main as notebook
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)


def exit_from_chat():
    sys.exit('    > Good bye!')


def main():
    COMMANDS = {'use addressbook': addressbook, 'use notebook': notebook,
                'sort directory': sort_directory, 'exit': exit_from_chat}

    command_completer = WordCompleter(COMMANDS.keys(), ignore_case=True)
    print(Fore.YELLOW + Back.BLUE + ' Glory to  Ukraine! ')
    print(Fore.BLUE + Back.YELLOW + 'Glory to the Heroes!')
    print('    > Hello! I am your personal PADAWAN helper')
    print("    > How can I help you?")
    while True:
        commands_string = prompt(
            '    > Enter what do you want to do:', completer=command_completer, complete_while_typing=True).lstrip()
        for i in COMMANDS.keys():
            if commands_string.lower().startswith(i):
                command = commands_string[:len(i)].lower()
                COMMANDS[command]()
                break

if __name__ == '__main__':
    main()