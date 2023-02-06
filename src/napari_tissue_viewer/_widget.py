"""
This module is an example of a barebones QWidget plugin for napari

It implements the Widget specification.
see: https://napari.org/stable/plugins/guides.html?#widgets

Replace code below according to your needs.
"""
from functools import partial
from typing import TYPE_CHECKING

from qtpy.QtWidgets import (
    QCheckBox,
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
    channel_names = [
        ["DAPI/CD31", "DAPI/CD31", "DAPI/CD31", "DAPI/CD31"],
        ["PanCK", "PanCK", "PanCK", "PanCK"],
        ["CD68", "CD68", "CD3", "CD3"],
        ["CD20", "CD4", "CD20", "CD4"],
    ]
    # [A1_5x, A1_20x], [A2_5x, A2_20x] ...
    image_loaded = [
        [False, False],
        [False, False],
        [False, False],
        [False, False],
    ]
    # [A1, A2, A3, A4] [5x, 20x] [DAPI/CD31, PanCK, CD68, CD3, CD20, CD4]
    visibility = {
        "blocks": [True, True, True, True],
        "resolution": [True, True],
        "channels": [True, True, True, True, True, True],
    }

    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        tabs_file_select = QTabWidget()
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
            tabs_file_select.addTab(self.tab_list[i], "A" + str(i + 1))
            tab_layout = QFormLayout(self)
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
            tab_layout.addRow("5x", hbox_load_file_5x)
            tab_layout.addRow("20x", hbox_load_file_20x)
            tab_layout.addRow("5x registration", hbox_load_file_5x_5x)
            tab_layout.addRow("20x registration", hbox_load_file_5x_20x)
            self.tab_list[i].setLayout(tab_layout)

        # file load button
        self.btn_load_file = QPushButton("load", self)
        self.btn_load_file.clicked.connect(self.load_file)
        # block check boxes
        self.block_check_boxes = [
            QCheckBox("A1"),
            QCheckBox("A2"),
            QCheckBox("A3"),
            QCheckBox("A4"),
        ]
        hbox_block_visibility = QHBoxLayout()
        for i in range(len(self.block_check_boxes)):
            hbox_block_visibility.addWidget(self.block_check_boxes[i])
        # res check boxes
        self.res_check_boxes = [
            QCheckBox("5x"),
            QCheckBox("20x"),
        ]
        hbox_res_visibility = QHBoxLayout()
        for i in range(len(self.res_check_boxes)):
            hbox_res_visibility.addWidget(self.res_check_boxes[i])
        # channel check boxes
        self.channel_check_boxes = [
            QCheckBox("DAPI/CD31"),
            QCheckBox("PanCK"),
            QCheckBox("CD68"),
            QCheckBox("CD3"),
            QCheckBox("CD20"),
            QCheckBox("CD4"),
        ]
        hbox_channel_visibility = QHBoxLayout()
        for i in range(len(self.channel_check_boxes)):
            hbox_channel_visibility.addWidget(self.channel_check_boxes[i])

        layout = QFormLayout(self)
        layout.addRow(tabs_file_select)
        layout.addRow(self.btn_load_file)
        layout.addRow(hbox_block_visibility)
        layout.addRow(hbox_res_visibility)
        layout.addRow(hbox_channel_visibility)
        self.setLayout(layout)
        # self.layout().addWidget(self.tabs_file_select)
        # self.layout().addWidget(self.btn_load_file)

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
        # example: A1-5x-DAPI/CD31
        for i in range(len(self.tab_list)):
            if self.line_file_path_5x_list[i].text() != "":
                self.viewer.open(self.line_file_path_5x_list[i].text())
                self.image_loaded[i][0] = True
                self.viewer.layers[-4].blending = "additive"
                self.viewer.layers[-4].name = (
                    "A" + str(i + 1) + "-5x-" + self.channel_names[0][i]
                )
                self.viewer.layers[-3].name = (
                    "A" + str(i + 1) + "-5x-" + self.channel_names[1][i]
                )
                self.viewer.layers[-2].name = (
                    "A" + str(i + 1) + "-5x-" + self.channel_names[2][i]
                )
                self.viewer.layers[-1].name = (
                    "A" + str(i + 1) + "-5x-" + self.channel_names[3][i]
                )
            if self.line_file_path_20x_list[i].text() != "":
                self.viewer.open(self.line_file_path_20x_list[i].text())
                self.image_loaded[i][1] = True
                self.viewer.layers[-4].blending = "additive"
                self.viewer.layers[-4].name = (
                    "A" + str(i + 1) + "-20x-" + self.channel_names[0][i]
                )
                self.viewer.layers[-3].name = (
                    "A" + str(i + 1) + "-20x-" + self.channel_names[1][i]
                )
                self.viewer.layers[-2].name = (
                    "A" + str(i + 1) + "-20x-" + self.channel_names[2][i]
                )
                self.viewer.layers[-1].name = (
                    "A" + str(i + 1) + "-20x-" + self.channel_names[3][i]
                )
