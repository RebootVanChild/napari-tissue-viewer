"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from typing import TYPE_CHECKING

from qtpy.QtWidgets import QHBoxLayout, QTabWidget, QWidget

if TYPE_CHECKING:
    pass


class Widget(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        #
        self.file_select_tabs = QTabWidget()
        self.tab_list = [QWidget(), QWidget(), QWidget(), QWidget()]
        for i in range(len(self.tab_list)):
            self.file_select_tabs.addTab(self.tab_list[i], "A" + str(i + 1))

        # self.tab1.layout = QVBoxLayout(self)
        # self.pushButton1 = QPushButton("PyQt5 button")
        # self.tab1.layout.addWidget(self.pushButton1)
        # self.tab1.setLayout(self.tab1.layout)
        #
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.file_select_tabs)
