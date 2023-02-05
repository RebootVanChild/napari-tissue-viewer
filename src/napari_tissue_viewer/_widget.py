"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from typing import TYPE_CHECKING

from qtpy.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QTabWidget,
    QWidget,
)

if TYPE_CHECKING:
    pass


class Widget(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        #
        self.tabs_file_select = QTabWidget()
        self.tab_list = [QWidget(), QWidget(), QWidget(), QWidget()]
        self.line_file_path_5x_list = [
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
        ]
        self.btn_file_path_5x_list = [
            QPushButton("browse", self),
            QPushButton("browse", self),
            QPushButton("browse", self),
            QPushButton("browse", self),
        ]
        self.line_file_path_20x_list = [
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
        ]
        self.btn_file_path_20x_list = [
            QPushButton("browse", self),
            QPushButton("browse", self),
            QPushButton("browse", self),
            QPushButton("browse", self),
        ]
        for i in range(len(self.tab_list)):
            self.tabs_file_select.addTab(self.tab_list[i], "A" + str(i + 1))
            self.tab_list[i].layout = QHBoxLayout()
            self.tab_list[i].layout.addWidget(self.line_file_path_5x_list[i])
            self.tab_list[i].layout.addWidget(self.btn_file_path_5x_list[i])
            self.tab_list[i].layout.addWidget(self.line_file_path_20x_list[i])
            self.tab_list[i].layout.addWidget(self.btn_file_path_20x_list[i])
            self.tab_list[i].setLayout(self.tab_list[i].layout)

        # self.tab1.layout = QVBoxLayout(self)
        # self.pushButton1 = QPushButton("PyQt5 button")
        # self.tab1.layout.addWidget(self.pushButton1)
        # self.tab1.setLayout(self.tab1.layout)
        #
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.tabs_file_select)
