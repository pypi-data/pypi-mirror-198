#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
  ████
██    ██   Datature
  ██  ██   Powering Breakthrough AI
    ██

@File    :   nii_processor.py
@Author  :   Raighne.Weng
@Version :   0.7.3
@Contact :   raighne@datature.io
@License :   Apache License 2.0
@Desc    :   Nii Processor
'''

import tempfile
from os.path import exists, join
from os import makedirs
from pathlib import Path
import cv2
import numpy as np
import nibabel as nib
from datature import error
from datature.processor.base_processor import BaseProcessor


# pylint: disable=R0914,E1101
class NiiProcessor(BaseProcessor):
    """Nii processor class"""

    def valid(self, request_data):
        """Valid the input

        :param request_data: The request data, include file path.
        :return: None.
        """
        file_path = request_data.get("file")
        options = request_data.get("options")

        if not file_path:
            raise error.BadRequestError(
                "Required field, must include file path")

        if not options.get("orientation") or options.get(
                "orientation") not in ["x", "y", "z"]:
            raise error.BadRequestError(
                "NIfTI file must have an orientation of choice: [x, y, z]")

    def process(self, request_data):
        """Start process file to asset video

        :param request_data: The request data, include file path.
        :return: str: The generate video path.
        """
        out_path = tempfile.mkdtemp()

        file_path = request_data.get("file")
        direction = request_data.get("options").get("direction")

        file_name = Path(file_path).stem

        video_output = join(out_path, file_name)

        if not exists(video_output):
            makedirs(video_output)

        scan = nib.load(file_path)

        # Read data and get scan's shape
        scan_array = scan.get_fdata()
        scan_array_shape = scan_array.shape

        four_cc = cv2.VideoWriter_fourcc(*'avc1')
        video_writer = cv2.VideoWriter(f"{video_output}/{file_name}.mp4",
                                       four_cc, 30.0, (1024, 1024))

        axis = 0 if direction == 'x' else 1 if direction == 'y' else 2

        for i in range(scan_array_shape[axis]):
            # Get slice along the correct axis and resize
            slice_axis = scan_array.take(i, axis=axis)
            image = cv2.resize(slice_axis, (1024, 1024))

            # Convert to RGB and write to video file
            new_image = cv2.cvtColor(np.uint8(image), cv2.COLOR_GRAY2RGB)
            video_writer.write(new_image)

        video_writer.release()

        return f"{video_output}/{file_name}.mp4"
