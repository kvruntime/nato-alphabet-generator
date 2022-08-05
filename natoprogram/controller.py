
from natoprogram import model
from natoprogram.model import ModelNato
from natoprogram.pagemain import PageMainVM


class Controller:

    def __init__(self, pagevm:PageMainVM, model:ModelNato) -> None:
        self.model = model
        self.pagevm = pagevm
        self._listen_signals()
        pass
    
    def _listen_signals(self):
        self.pagevm.page.btn_convert.clicked.connect(self.convertion)
        return None
    
    def convertion(self):
        word = self.model.convertion(self.pagevm.get_word())
        self.pagevm.add_result(word)
        return None
    