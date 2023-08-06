import os
from typing import Tuple, Union, List
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel, QComboBox, QPushButton, QSlider
)


class ComboBox(QComboBox):
    def __init__(
        self, 
        items: List[str], 
        current_index: int,
        stylesheet: Union[str, os.PathLike] = None
    ) -> None:
        super().__init__()
        self.addItems(items)
        self.setCurrentIndex(current_index)

        # TODO: 외부 함수화 또는 PySide6에서 이런 함수 있는지 찾아보셈
        if stylesheet is not None:
            with open(os.path.join(os.path.split(__file__)[0], stylesheet), "r", encoding="utf-8") as f:
                stylesheet = f.read()
                print(stylesheet)
            self.setStyleSheet(str(stylesheet))


class PushButton(QPushButton):
    def __init__(
        self, 
        text: str = "",
        font: str = "Arial", 
        fontsize: int = 10, 
        stylesheet: Union[str, os.PathLike] = None
    ) -> None:
        super().__init__()
        self.setText(text)
        self.setFont(QFont(f"{font}", fontsize))

        if stylesheet is not None:
            with open(os.path.join(os.path.split(__file__)[0], stylesheet), "r", encoding="utf-8") as f:
                stylesheet = f.read()
                print(stylesheet)
            self.setStyleSheet(str(stylesheet))


class Slider(QSlider):
    def __init__(
        self, 
        orientation, 
        set_range_values: Tuple[int], 
        set_value: int, 
        stylesheet: Union[str, os.PathLike] = None
    ) -> None:
        super().__init__(orientation)
        self.setRange(*set_range_values)
        self.setValue(set_value)

        if stylesheet is not None:
            with open(os.path.join(os.path.split(__file__)[0], stylesheet), "r", encoding="utf-8") as f:
                stylesheet = f.read()
                print(stylesheet)
            self.setStyleSheet(str(stylesheet))


class Label(QLabel):
    def __init__(
        self, 
        text: str = "",
        font: str = "Arial", 
        fontsize: int = 10, 
        orientation = None,
        stylesheet: Union[str, os.PathLike] = None
    ) -> None:
        super().__init__()
        self.setText(text)
        self.setFont(QFont(f"{font}", fontsize))
        if orientation is not None:
            self.setAlignment(orientation)

        if stylesheet is not None:
            with open(os.path.join(os.path.split(__file__)[0], stylesheet), "r", encoding="utf-8") as f:
                stylesheet = f.read()
                print(stylesheet)
            self.setStyleSheet(str(stylesheet))