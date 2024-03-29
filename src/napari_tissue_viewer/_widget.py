from functools import partial
from typing import TYPE_CHECKING

import numpy as np
from qtpy.QtWidgets import (
    QCheckBox,
    QFileDialog,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

if TYPE_CHECKING:
    pass


class Widget(QWidget):
    channel_names = ["DAPI/CD31", "PanCK", "CD68", "CD3", "CD20", "CD4"]
    channel_colors = ["blue", "green", "red", "red", "yellow", "yellow"]
    channel_list = [
        [4, 5, 4, 5],
        [2, 2, 3, 3],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
    ]
    # [A1_5x, A1_20x, seg], [A2_5x, A2_20x, seg] ...
    image_loaded = [
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
        [False, False, False, False, False, False],
    ]

    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer
        tabs_file_select = QTabWidget()
        self.tab_list = [QWidget(), QWidget(), QWidget(), QWidget()]
        # segmentation tabs
        tabs_seg_select = [
            QTabWidget(),
            QTabWidget(),
            QTabWidget(),
            QTabWidget(),
        ]
        self.tab_seg_list = [
            [QWidget(), QWidget(), QWidget(), QWidget()],
            [QWidget(), QWidget(), QWidget(), QWidget()],
            [QWidget(), QWidget(), QWidget(), QWidget()],
            [QWidget(), QWidget(), QWidget(), QWidget()],
        ]
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
        self.line_file_path_seg_list = [
            [
                QLineEdit(self),
                QLineEdit(self),
                QLineEdit(self),
                QLineEdit(self),
            ],
            [
                QLineEdit(self),
                QLineEdit(self),
                QLineEdit(self),
                QLineEdit(self),
            ],
            [
                QLineEdit(self),
                QLineEdit(self),
                QLineEdit(self),
                QLineEdit(self),
            ],
            [
                QLineEdit(self),
                QLineEdit(self),
                QLineEdit(self),
                QLineEdit(self),
            ],
        ]
        self.btn_file_path_seg_list = [
            [
                QPushButton("browse", self),
                QPushButton("browse", self),
                QPushButton("browse", self),
                QPushButton("browse", self),
            ],
            [
                QPushButton("browse", self),
                QPushButton("browse", self),
                QPushButton("browse", self),
                QPushButton("browse", self),
            ],
            [
                QPushButton("browse", self),
                QPushButton("browse", self),
                QPushButton("browse", self),
                QPushButton("browse", self),
            ],
            [
                QPushButton("browse", self),
                QPushButton("browse", self),
                QPushButton("browse", self),
                QPushButton("browse", self),
            ],
        ]
        # load layout
        for i in range(len(self.tab_list)):
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
            for channel_idx in range(len(self.channel_list)):
                tab_seg_layout = QFormLayout()
                hbox_load_file_seg = QHBoxLayout()
                hbox_load_file_seg.addWidget(
                    self.line_file_path_seg_list[i][channel_idx]
                )
                hbox_load_file_seg.addWidget(
                    self.btn_file_path_seg_list[i][channel_idx]
                )
                self.btn_file_path_seg_list[i][channel_idx].clicked.connect(
                    partial(self.select_seg_file, i, channel_idx)
                )
                tab_seg_layout.addRow(hbox_load_file_seg)
                self.tab_seg_list[i][channel_idx].setLayout(tab_seg_layout)
                tabs_seg_select[i].addTab(
                    self.tab_seg_list[i][channel_idx],
                    self.channel_names[self.channel_list[channel_idx][i]],
                )
            tab_layout.addRow("5x", hbox_load_file_5x)
            tab_layout.addRow("20x", hbox_load_file_20x)
            tab_layout.addRow("5x registration", hbox_load_file_5x_5x)
            tab_layout.addRow("20x registration", hbox_load_file_5x_20x)
            tab_layout.addRow(tabs_seg_select[i])
            self.tab_list[i].setLayout(tab_layout)
            tabs_file_select.addTab(self.tab_list[i], "A" + str(i + 1))
        self.line_scale_factor = QLineEdit(self)
        self.line_scale_factor.setText("1")
        # file load button
        self.btn_load_file = QPushButton("load", self)
        self.btn_load_file.clicked.connect(self.load_file)
        # auto contrast button
        self.btn_auto_contrast = QPushButton("auto contrast", self)
        self.btn_auto_contrast.clicked.connect(self.set_auto_contrast)
        # block check boxes
        self.block_check_boxes = [
            QCheckBox("A1"),
            QCheckBox("A2"),
            QCheckBox("A3"),
            QCheckBox("A4"),
        ]
        hbox_block_visibility = QHBoxLayout()
        for i in range(len(self.block_check_boxes)):
            self.block_check_boxes[i].setEnabled(False)
            self.block_check_boxes[i].stateChanged.connect(self.set_visibility)
            hbox_block_visibility.addWidget(self.block_check_boxes[i])
        # res check boxes
        self.res_check_boxes = [
            QCheckBox("5x"),
            QCheckBox("20x"),
            QCheckBox("Segmentation"),
        ]
        hbox_res_visibility = QHBoxLayout()
        for i in range(len(self.res_check_boxes)):
            self.res_check_boxes[i].setEnabled(False)
            self.res_check_boxes[i].stateChanged.connect(self.set_visibility)
            hbox_res_visibility.addWidget(self.res_check_boxes[i])
        # channel check boxes
        self.channel_check_boxes = [
            QCheckBox(self.channel_names[0]),
            QCheckBox(self.channel_names[1]),
            QCheckBox(self.channel_names[2]),
            QCheckBox(self.channel_names[3]),
            QCheckBox(self.channel_names[4]),
            QCheckBox(self.channel_names[5]),
        ]
        hbox_channel_visibility = QHBoxLayout()
        for i in range(len(self.channel_check_boxes)):
            self.channel_check_boxes[i].setEnabled(False)
            self.channel_check_boxes[i].stateChanged.connect(
                self.set_visibility
            )
            hbox_channel_visibility.addWidget(self.channel_check_boxes[i])
        main_layout = QVBoxLayout()
        # box for import files
        import_group_box = QGroupBox()
        import_layout = QFormLayout()
        import_layout.addRow(tabs_file_select)
        import_layout.addRow(
            "image downsampled? scale factor = ", self.line_scale_factor
        )
        import_layout.addRow(self.btn_load_file)
        import_group_box.setLayout(import_layout)
        # box for ctrls
        ctrl_group_box = QGroupBox()
        ctrl_layout = QFormLayout()
        ctrl_layout.addRow(self.btn_auto_contrast)
        ctrl_layout.addRow(hbox_block_visibility)
        ctrl_layout.addRow(hbox_res_visibility)
        ctrl_layout.addRow(hbox_channel_visibility)
        ctrl_group_box.setLayout(ctrl_layout)
        # add to main
        main_layout.addWidget(import_group_box)
        main_layout.addWidget(ctrl_group_box)
        self.setLayout(main_layout)

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

    def select_seg_file(self, block_index, channel_index):
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Select Segmentation", "", "TIFF Files (*.tif)"
        )
        self.line_file_path_seg_list[block_index][channel_index].setText(
            fileName
        )

    def load_file(self):
        # example: A1-5x-DAPI/CD31
        self.viewer.dims.ndisplay = 3
        for i in range(len(self.tab_list)):
            affine_5x_5x = np.array(
                [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
            )
            if self.line_file_path_5x_list[i].text() != "":
                # block signals
                self.block_check_boxes[i].blockSignals(True)
                self.res_check_boxes[0].blockSignals(True)
                self.viewer.open(
                    self.line_file_path_5x_list[i].text(), plugin='napari-aicsimageio')
                self.image_loaded[i][0] = True
                # update checkboxes and visibilities
                self.block_check_boxes[i].setEnabled(True)
                self.block_check_boxes[i].setChecked(True)
                self.res_check_boxes[0].setEnabled(True)
                self.res_check_boxes[0].setChecked(True)
                # activate signals
                self.block_check_boxes[i].blockSignals(False)
                self.res_check_boxes[0].blockSignals(False)
                for j in range(4):
                    # block signals
                    self.channel_check_boxes[
                        self.channel_list[j][i]
                    ].blockSignals(True)
                    self.channel_check_boxes[
                        self.channel_list[j][i]
                    ].setEnabled(True)
                    self.channel_check_boxes[
                        self.channel_list[j][i]
                    ].setChecked(True)
                    # activate signals
                    self.channel_check_boxes[
                        self.channel_list[j][i]
                    ].blockSignals(False)
                # apply affine
                if self.line_file_path_5x_5x_list[i].text() != "":
                    affine_5x_5x = self.calculate_affine_from_file(
                        self.line_file_path_5x_5x_list[i].text(),
                        self.viewer.layers[-1],
                    )
                    self.viewer.layers[-4].affine = affine_5x_5x
                    self.viewer.layers[-3].affine = affine_5x_5x
                    self.viewer.layers[-2].affine = affine_5x_5x
                    self.viewer.layers[-1].affine = affine_5x_5x
                self.viewer.layers[-4].blending = "additive"
                for j in range(4):
                    self.viewer.layers[j - 4].colormap = self.channel_colors[
                        self.channel_list[j][i]
                    ]
                    self.viewer.layers[j - 4].name = (
                        "A"
                        + str(i + 1)
                        + "-5x-"
                        + self.channel_names[self.channel_list[j][i]]
                    )
            if self.line_file_path_20x_list[i].text() != "":
                # block signals
                self.block_check_boxes[i].blockSignals(True)
                self.res_check_boxes[1].blockSignals(True)
                self.viewer.open(
                    self.line_file_path_20x_list[i].text(), plugin='napari-aicsimageio')
                self.image_loaded[i][1] = True
                # update checkboxes
                self.block_check_boxes[i].setEnabled(True)
                self.block_check_boxes[i].setChecked(True)
                self.res_check_boxes[1].setEnabled(True)
                self.res_check_boxes[1].setChecked(True)
                # activate signals
                self.block_check_boxes[i].blockSignals(False)
                self.res_check_boxes[1].blockSignals(False)
                for j in range(4):
                    # block signals
                    self.channel_check_boxes[
                        self.channel_list[j][i]
                    ].blockSignals(True)
                    self.channel_check_boxes[
                        self.channel_list[j][i]
                    ].setEnabled(True)
                    self.channel_check_boxes[
                        self.channel_list[j][i]
                    ].setChecked(True)
                    # activate signals
                    self.channel_check_boxes[
                        self.channel_list[j][i]
                    ].blockSignals(False)
                # record scale for segmentation
                scale = self.viewer.layers[-1].extent[2]
                # apply affine
                combined_matrix = np.array(
                    [
                        [1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1],
                    ]
                )
                if self.line_file_path_5x_20x_list[i].text() != "":
                    affine_5x_20x = self.affine_xyz_to_zyx(
                        np.loadtxt(
                            open(
                                self.line_file_path_5x_20x_list[i].text(), "rb"
                            ),
                            delimiter=",",
                        )
                    )
                    combined_matrix = np.dot(affine_5x_5x, affine_5x_20x)
                    self.viewer.layers[-4].affine = combined_matrix
                    self.viewer.layers[-3].affine = combined_matrix
                    self.viewer.layers[-2].affine = combined_matrix
                    self.viewer.layers[-1].affine = combined_matrix
                self.viewer.layers[-4].blending = "additive"
                for j in range(4):
                    self.viewer.layers[j - 4].colormap = self.channel_colors[
                        self.channel_list[j][i]
                    ]
                    self.viewer.layers[j - 4].name = (
                        "A"
                        + str(i + 1)
                        + "-20x-"
                        + self.channel_names[self.channel_list[j][i]]
                    )
                # load segmentation file
                for j in range(len(self.channel_list)):
                    seg_file_name = self.line_file_path_seg_list[i][j].text()
                    if seg_file_name != "":
                        downsampled_scale = float(
                            self.line_scale_factor.text()
                        )
                        self.viewer.open(
                            self.line_file_path_seg_list[i][j].text()
                        )
                        self.viewer.layers[-1].blending = "additive"
                        self.viewer.layers[-1].name = (
                            "A"
                            + str(i + 1)
                            + "-20x-"
                            + self.channel_names[self.channel_list[j][i]]
                            + "-Segmentation"
                        )
                        z_start_index = (
                            self.get_z_start_index_from_seg_file_name(
                                seg_file_name, downsampled_scale
                            )
                        )
                        self.viewer.layers[-1].translate = [
                            z_start_index * scale[0],
                            0,
                            0,
                        ]
                        # if self.segmentation_align_buttons[1].isChecked():
                        #     self.viewer.layers[-1].translate = [
                        #         (
                        #             dim_pixel_z
                        #             - self.viewer.layers[-1].extent[0][1][0]
                        #         )
                        #         * scale[0],
                        #         0,
                        #         0,
                        #     ]
                        self.viewer.layers[-1].scale = scale
                        self.viewer.layers[-1].affine = combined_matrix
                        # block signals
                        self.res_check_boxes[2].blockSignals(True)
                        self.image_loaded[i][2 + j] = True
                        # update checkboxes
                        self.res_check_boxes[2].setEnabled(True)
                        self.res_check_boxes[2].setChecked(True)
                        # activate signals
                        self.res_check_boxes[2].blockSignals(False)

    def calculate_affine_from_file(self, file_path, layer):
        transform_parameters = np.loadtxt(
            file_path,
            delimiter=",",
            converters=lambda x: float(eval(x)),
        )
        # get dimensions and pixel size to find center (in microns)
        image_center = (
            np.array(layer.extent[0][1]) * np.array(layer.extent[2]) / 2,
        )
        rot_mat_x = np.array(
            [
                [
                    np.cos(np.deg2rad(transform_parameters[1][0])),
                    np.sin(np.deg2rad(transform_parameters[1][0])),
                    0,
                ],
                [
                    -np.sin(np.deg2rad(transform_parameters[1][0])),
                    np.cos(np.deg2rad(transform_parameters[1][0])),
                    0,
                ],
                [0, 0, 1],
            ]
        )
        rot_mat_y = np.array(
            [
                [
                    np.cos(np.deg2rad(transform_parameters[1][1])),
                    0,
                    np.sin(np.deg2rad(transform_parameters[1][1])),
                ],
                [0, 1, 0],
                [
                    -np.sin(np.deg2rad(transform_parameters[1][1])),
                    0,
                    np.cos(np.deg2rad(transform_parameters[1][1])),
                ],
            ]
        )
        rot_mat_z = np.array(
            [
                [1, 0, 0],
                [
                    0,
                    np.cos(np.deg2rad(transform_parameters[1][2])),
                    np.sin(np.deg2rad(transform_parameters[1][2])),
                ],
                [
                    0,
                    -np.sin(np.deg2rad(transform_parameters[1][2])),
                    np.cos(np.deg2rad(transform_parameters[1][2])),
                ],
            ]
        )
        rot_mat = rot_mat_x.dot(rot_mat_y).dot(rot_mat_z)
        translate_arr = (
            -rot_mat.dot(np.array(image_center).T)
            + np.array(image_center).T
            + np.array(
                [
                    [transform_parameters[0][2]],
                    [transform_parameters[0][1]],
                    [transform_parameters[0][0]],
                ]
            )
        )
        affine_matrix = np.append(
            np.hstack((rot_mat, translate_arr)),
            [[0, 0, 0, 1]],
            axis=0,
        )
        return affine_matrix

    def affine_xyz_to_zyx(self, mxyz):
        mzyx = mxyz
        mzyx[:3, :3] = np.rot90(mxyz[:3, :3], 2)
        mzyx[:3, 3] = np.flip(mxyz[:3, 3])
        return mzyx

    def set_visibility(self):
        visibility_mat = [
            [
                [False, False, False, False],
                [False, False, False, False],
                [False, False, False, False],
            ],
            [
                [False, False, False, False],
                [False, False, False, False],
                [False, False, False, False],
            ],
            [
                [False, False, False, False],
                [False, False, False, False],
                [False, False, False, False],
            ],
            [
                [False, False, False, False],
                [False, False, False, False],
                [False, False, False, False],
            ],
        ]
        # each block
        for i in range(4):
            # res 5x 20x
            for j in range(2):
                if self.image_loaded[i][j]:
                    if self.block_check_boxes[i].isChecked():
                        if self.res_check_boxes[j].isChecked():
                            # channel
                            for k in range(4):
                                if self.channel_check_boxes[
                                    self.channel_list[k][i]
                                ].isChecked():
                                    visibility_mat[i][j][k] = True
                    res = ""
                    if j == 0:
                        res = "5x"
                    if j == 1 or j == 2:
                        res = "20x"
                    for k in range(4):
                        layer_name = (
                            "A"
                            + str(i + 1)
                            + "-"
                            + res
                            + "-"
                            + self.channel_names[self.channel_list[k][i]]
                        )
                        self.viewer.layers[
                            layer_name
                        ].visible = visibility_mat[i][j][k]
            # segmentation
            for k in range(4):
                if self.image_loaded[i][2 + k]:
                    if (
                        self.block_check_boxes[i].isChecked()
                        and self.res_check_boxes[2].isChecked()
                        and self.channel_check_boxes[
                            self.channel_list[k][i]
                        ].isChecked()
                    ):
                        visibility_mat[i][2][k] = True
                    layer_name = (
                        "A"
                        + str(i + 1)
                        + "-20x-"
                        + self.channel_names[self.channel_list[k][i]]
                        + "-Segmentation"
                    )
                    self.viewer.layers[layer_name].visible = visibility_mat[i][
                        2
                    ][k]

    def set_auto_contrast(self):
        # each block
        for i in range(4):
            # only perform auto contrast on 5x
            if self.image_loaded[i][0]:
                for k in range(4):
                    layer_name = (
                        "A"
                        + str(i + 1)
                        + "-5x-"
                        + self.channel_names[self.channel_list[k][i]]
                    )
                    data = self.viewer.layers[layer_name].data
                    max_on_bound = max(
                        max(data[0][0][:]),
                        max(data[0][-1][:]),
                        max(data[-1][0][:]),
                        max(data[-1][-1][:]),
                        max(data[:][0][0]),
                        max(data[:][0][-1]),
                        max(data[:][-1][0]),
                        max(data[:][-1][-1]),
                        max(data[0][:][0]),
                        max(data[-1][:][0]),
                        max(data[0][:][-1]),
                        max(data[-1][:][-1]),
                    )
                    original_contrast = self.viewer.layers[
                        layer_name
                    ].contrast_limits
                    self.viewer.layers[layer_name].contrast_limits = (
                        max_on_bound,
                        original_contrast[1],
                    )

    def get_z_start_index_from_seg_file_name(self, filename, scale_20x):
        i = 0
        while True:
            if filename[i] == "Z" and filename[i + 1] == "_":
                break
            i += 1
        i += 2
        digit_start_index = i
        while filename[i] != "-":
            i += 1
        digit_end_index = i
        z_start_index = (
            float(filename[digit_start_index:digit_end_index]) * scale_20x
        )
        return z_start_index

    # def apply_segmentation_affine(self, block_index, chanel_index):
    #     self.viewer.layers[-1].name = (
    #             "A"
    #             + str(i + 1)
    #             + "-20x-"
    #             + self.channel_names[self.channel_list[j][i]]
    #             + "segmentation"
    #     )
    #     self.viewer.layers[-1].affine = [[1, 0, 0, 0],
    #     [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
