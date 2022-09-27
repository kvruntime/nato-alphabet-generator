import sys
from typing import Dict

from PyQt6.QtWidgets import QApplication

from natoprogram.viewmodels import NatoGeneratoViewModel

class App(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.setApplicationName("Nato Program")
        pass

    def run(self):
        vm = NatoGeneratoViewModel()
        vm.page.show()
        sys.exit(self.exec())

# TODO: end implementation of console version of the application.

# class ConsoleFrontend:
#     """ Nato program. """

#     def __init__(self) -> None:
#         self._guessed: str = ""
#         self._model = ModelNato()
#         self._natofied: Dict[str, str] = dict()
#         self._is_on: bool = True

#         self._init_game()
#         pass

#     def _init_game(self):
#         """ Intialiation of game. """
#         print("Welcome in the nato program.")
#         print("Enter 0 to exit the game.")
#         return None

#     def _guess_input(self):
#         self._guessed = input("\nEnter a word (or 0 to exit!): ")
#         return None

#     def _process(self):
#         """ Process the natofication. """
#         self._natofied = self._model.convertion(self._guessed)
#         return None

#     def run(self):
#         while self._is_on:
#             self._guess_input()

#             try:
#                 if eval(self._guessed) == 0:
#                     break
#             except NameError:
#                 pass
#             except SyntaxError:
#                 print("can not be found!")
#                 continue

#             self._process()
#             print(self._natofied)

#             self._natofied = dict()
#             self._guessed = ""

#         print("Bye!, see you next time.")
#         return None
