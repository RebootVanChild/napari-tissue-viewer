"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from functools import partial
from typing import TYPE_CHECKING

from qtpy.QtWidgets import (
    QFileDialog,
    QFormLayout,
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
        self.line_file_path_5x_5x_list = [
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
        ]
        self.btn_file_path_5x_5x_list = [
            QPushButton("browse", self),
            QPushButton("browse", self),
            QPushButton("browse", self),
            QPushButton("browse", self),
        ]
        self.line_file_path_5x_20x_list = [
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
            QLineEdit(self),
        ]
        self.btn_file_path_5x_20x_list = [
            QPushButton("browse", self),
            QPushButton("browse", self),
            QPushButton("browse", self),
            QPushButton("browse", self),
        ]
        for i in range(len(self.tab_list)):
            self.tabs_file_select.addTab(self.tab_list[i], "A" + str(i + 1))
            layout = QFormLayout(self)
            hbox_load_file_5x = QHBoxLayout()
            hbox_load_file_5x.addWidget(self.line_file_path_5x_list[i])
            hbox_load_file_5x.addWidget(self.btn_file_path_5x_list[i])
            self.btn_file_path_5x_list[i].clicked.connect(
                partial(self.select_file, i, "5x")
            )
            hbox_load_file_20x = QHBoxLayout()
            hbox_load_file_20x.addWidget(self.line_file_path_20x_list[i])
            hbox_load_file_20x.addWidget(self.btn_file_path_20x_list[i])
            self.btn_file_path_20x_list[i].clicked.connect(
                partial(self.select_file, i, "20x")
            )
            hbox_load_file_5x_5x = QHBoxLayout()
            hbox_load_file_5x_5x.addWidget(self.line_file_path_5x_5x_list[i])
            hbox_load_file_5x_5x.addWidget(self.btn_file_path_5x_5x_list[i])
            self.btn_file_path_5x_5x_list[i].clicked.connect(
                partial(self.select_file, i, "5x-5x")
            )
            hbox_load_file_5x_20x = QHBoxLayout()
            hbox_load_file_5x_20x.addWidget(self.line_file_path_5x_20x_list[i])
            hbox_load_file_5x_20x.addWidget(self.btn_file_path_5x_20x_list[i])
            self.btn_file_path_5x_20x_list[i].clicked.connect(
                partial(self.select_file, i, "5x-20x")
            )
            layout.addRow("5x", hbox_load_file_5x)
            layout.addRow("20x", hbox_load_file_20x)
            layout.addRow("5x registration", hbox_load_file_5x_5x)
            layout.addRow("20x registration", hbox_load_file_5x_20x)
            self.tab_list[i].setLayout(layout)

        # file load button
        self.btn_load_file = QPushButton("load", self)
        self.btn_load_file.clicked.connect(self.load_file)

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.tabs_file_select)

    # block_index: 0-3, file type: "5x", "20x", "5x-5x", "5x-20x"
    def select_file(self, block_index, file_type):
        if file_type == "5x":
            fileName, _ = QFileDialog.getOpenFileName(
                self, "Select 5x Image", "", "CZI Files (*.czi)"
            )
            self.line_file_path_5x_list[block_index].setText(fileName)
        if file_type == "20x":
            fileName, _ = QFileDialog.getOpenFileName(
                self, "Select 20x Image", "", "CZI Files (*.czi)"
            )
            self.line_file_path_20x_list[block_index].setText(fileName)
        if file_type == "5x-5x":
            fileName, _ = QFileDialog.getOpenFileName(
                self, "Select 5x Registration", "", "CSV Files (*.csv)"
            )
            self.line_file_path_5x_5x_list[block_index].setText(fileName)
        if file_type == "5x-20x":
            fileName, _ = QFileDialog.getOpenFileName(
                self, "Select 20x Registration", "", "CSV Files (*.csv)"
            )
            self.line_file_path_5x_20x_list[block_index].setText(fileName)

    def load_file(self):
        self.viewer.open(self.line_file_path_5x_list[0].text())
