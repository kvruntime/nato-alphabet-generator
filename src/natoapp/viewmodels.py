from typing import List
from natoapp.pages import PageMain
from natoapp.datalayers import NatoGenerator
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt

class NatoGeneratoViewModel:
    def __init__(self) -> None:
        self.page = PageMain()
        self.model = NatoGenerator()
        
        self._bindings()
        pass
    
    def update_results(self, results: List[str, ]):
        while self.page.layoutResultArea.count():
            self.page.layoutResultArea.takeAt(0).widget().deleteLater()

        for result in results:
            label = QLabel(str(result))
            self.page.layoutResultArea.addWidget(
                label, alignment=Qt.AlignmentFlag.AlignTop)
        return None
    
    def command_generate_nato(self):
        name = self.page.inputName.text()
        natos = self.model.convertion(name)
        self.page.inputName.setText("")
        self.update_results(natos) #type:ignore
        return None
    
    def _bindings(self):
        self.page.buttonConvert.clicked.connect(self.command_generate_nato)
        return None
    