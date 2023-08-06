import test_version_powerhouse_helper.AddressBook.Address_Book_Handler as abh
import test_version_powerhouse_helper.NoteBook.Note_Book_Handler as nbh
from test_version_powerhouse_helper.OtherModules.Sort_Files import *
from test_version_powerhouse_helper.OtherModules.Сalculator import *
from test_version_powerhouse_helper.GameGooseKiller.Game_goose import start_game
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


def game():
    return start_game()

def calculator():
    return start_calc()

def folder_sorter():
    return start_sorting()

def address_book():
    address_container = abh.AddressBot()
    address_container.book.load()
    address_book_completer = WordCompleter(['help', 'add', 'search', 'edit', 'delete', 'save', 'load', 'congratulate', 'show', 'exit'])
    print('\033[32mYou have entered the address book. Enter your command ("help" to get a description of the commands)')
    while True:
        action = prompt('>>> ', completer=address_book_completer)
        if action == 'exit': 
            break
        try:
            print(abh.performer(abh.get_handler(action), address_container))
        except KeyError:
            print('There is no such command')
    return '\033[32mThank you for using our address book!'

def note_book():
    note_container = nbh.NoteBot()
    note_book_completer = WordCompleter(['help', 'add note', 'add date', 'show all', 'change note', 'delete note', 'search', 'show date', 'done', 'return', 'add tag', 'sort by tags', 'exit'])
    print('\033[32mYou have entered the note book. Enter your command ("help" to get a description of the commands)')
    while True:
        action = prompt('>>> ', completer=note_book_completer)
        if action == 'exit':
            note_container.book.save()
            break
        try:
            print(nbh.performer(nbh.get_handler(action), note_container))
        except KeyError:
            print('\033[31mThere is no such command')
    return '\033[32mThank you for using our address book!'


def main():

    print('''\033[43m\033[1m  _____                                     _                                      _    _          _                       
 |  __ \                                   | |                                    | |  | |        | |                      
 | |__) |   ___   __      __   ___   _ __  | |__     ___    _   _   ___    ___    | |__| |   ___  | |  _ __     ___   _ __ 
 |  ___/   / _ \  \ \ /\ / /  / _ \ | '__| | '_ \   / _ \  | | | | / __|  / _ \   |  __  |  / _ \ | | | '_ \   / _ \ | '__|\033[44m
 | |      | (_) |  \ V  V /  |  __/ | |    | | | | | (_) | | |_| | \__ \ |  __/   | |  | | |  __/ | | | |_) | |  __/ | |   
 |_|       \___/    \_/\_/    \___| |_|    |_| |_|  \___/   \__,_| |___/  \___|   |_|  |_|  \___| |_| | .__/   \___| |_|   
                                                                                                      | |                  
                                                                                                      |_|                  \n''')
    while True:
        main_completer = WordCompleter(['address book', 'note book', 'folder sorter', 'calculator', 'game', 'exit'])
        main_action = prompt('''You are in the main menu! Please select the section you need.\n> address book\n> note book\n> folder sorter\n> calculator\n> game\n> exit\n>>> ''', completer=main_completer)
        if main_action == 'exit':
            break
        handler = {'calculator' : calculator, 'folder sorter' : folder_sorter, 'address book' : address_book, 'note book' : note_book, 'game' : game}
        try:
            print(handler[main_action]())
        except KeyError:
            print('\033[31mThere is no such command')

    print('\033[32mThank you for using our concole assistant\033[0m')

if __name__ == '__main__':
    main()