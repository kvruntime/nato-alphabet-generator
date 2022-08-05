from typing import List

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QGridLayout, QLabel, QLineEdit, QPushButton,
                             QScrollArea, QVBoxLayout, QWidget)


STYLE = """
        background-color:royalblue;
        padding: 5px 10px;
        border-radius: 5px;
        """


class PageMain(QWidget):

    def __init__(self):
        super().__init__()
        self._init_ui()
        pass

    def _init_ui(self):
        lbl_word = QLabel("Enter a word")
        lbl_word.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.tbox_word = QLineEdit()
        self.tbox_word.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.tbox_word.setPlaceholderText("Word")
        self.btn_convert = QPushButton("Convert")

        box_result = QWidget()
        result_area = QScrollArea()
        result_area.setFrameShape(QScrollArea.Shape.NoFrame)
        result_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        result_area.setMinimumHeight(120)
        result_area.setWidgetResizable(True)
        result_area.setWidget(box_result)
        self.layout_result = QVBoxLayout(box_result)

        layout = QGridLayout(self)
        layout.addWidget(lbl_word, 1, 0, 1, 1)
        layout.addWidget(self.tbox_word, 1, 1, 1, 1)
        layout.addWidget(self.btn_convert, 2, 0, 1, 1)
        layout.addWidget(result_area, 3, 0, 1, 2)

        return None


class PageMainVM:

    def __init__(self) -> None:
        self.page = PageMain()
        pass

    def add_result(self, results: List[str, ]):
        self.clear_results()
        
        for result in results:
            lbl = QLabel(str(result))
            lbl.setStyleSheet(STYLE)
            self.page.layout_result.addWidget(
                lbl, alignment=Qt.AlignmentFlag.AlignTop)
            
        return None

    def clear_results(self):
        self.page.tbox_word.setText("")
        if self.page.layout_result.count() == 0:
            return
        
        while self.page.layout_result.count():
            w = self.page.layout_result.takeAt(0)
            w.widget().deleteLater()
        return None

    def get_word(self):
        return self.page.tbox_word.text()
