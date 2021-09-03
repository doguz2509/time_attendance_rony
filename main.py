# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from typing import Tuple, AnyStr

from ui import UI

DATA_FILE_PATH = r'.\data.json'
ENTER_MENU = '1. SignIn\n2. SignUp\n3. Exit', 3


if __name__ == '__main__':

    menu: Tuple[AnyStr, int] = ENTER_MENU

    while True:
        with UI(DATA_FILE_PATH) as dm:
            input_ = input(menu[0])
            try:
                selection = int(input_)
                assert 1 <= selection < 3, "Incorrect selection"
                if selection == menu[1]:
                    print("Exiting")
                    break
                elif selection == 1:
                    menu = dm.select_user()
            except Exception as e:
                print(f"{e}")
                sys.exit(-1)

