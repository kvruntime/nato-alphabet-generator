from typing import List

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *


class PageMain(QWidget):
    def __init__(self):
        super().__init__()
        self._initialize_interface()
        pass

    def _initialize_interface(self):
        labelName = QLabel("Input the name here: ")
        labelName.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.inputName = QLineEdit()
        self.inputName.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.inputName.setPlaceholderText("Word")
        self.buttonConvert = QPushButton("Convert")

        scrollResultArea = QScrollArea()
        widgetResultArea = QWidget()
        self.layoutResultArea = QVBoxLayout(widgetResultArea)
        
        scrollResultArea.setFrameShape(QScrollArea.Shape.NoFrame)
        scrollResultArea.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scrollResultArea.setMinimumHeight(120)
        scrollResultArea.setWidgetResizable(True)
        scrollResultArea.setWidget(widgetResultArea)
        

        layout = QGridLayout(self)
        layout.addWidget(labelName, 1, 0, 1, 1)
        layout.addWidget(self.inputName, 1, 1, 1, 1)
        layout.addWidget(self.buttonConvert, 2, 0, 1, 1)
        layout.addWidget(scrollResultArea, 3, 0, 1, 2)
        return None
