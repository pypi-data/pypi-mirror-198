# Copyright (C) 2021-2022, Mindee.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://opensource.org/licenses/Apache-2.0> for full license details.

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union
from PIL import Image

import numpy as np
from tqdm import tqdm

from .datasets import VisionDataset
from .utils import convert_target_to_relative, crop_bboxes_from_image

__all__ = ["IndicData"]


class IndicData(VisionDataset):
    """
    >>> from doctr.datasets import IndicData
    >>> train_set = IndicData(train=True, download=True)
    >>> img, target = train_set[0]

    Args:
        train: whether the subset should be the training one
        use_polygons: whether polygons should be considered as rotated bounding box (instead of straight ones)
        recognition_task: whether the dataset should be used for recognition task
        **kwargs: keyword arguments from `VisionDataset`.
    """

    URL = "https://guillaumejaume.github.io/FUNSD/dataset.zip"
    SHA256 = "c31735649e4f441bcbb4fd0f379574f7520b42286e80b01d80b445649d54761f"
    FILE_NAME = "indic_testsets.zip"

    def __init__(
        self,
        train: bool = True,
        use_polygons: bool = False,
        recognition_task: bool = False,
        language: str = 'devanagari',
        inp_path: str = '../data/doctr-detection/Archive/val/', #'./data/processed'
        sets: str = 'test',
        **kwargs: Any,
    ) -> None:

        super().__init__(
            self.URL,
            self.FILE_NAME,
            self.SHA256,
            True,
            pre_transforms=convert_target_to_relative if not recognition_task else None,
            **kwargs,
        )
        self.train = train
        np_dtype = np.float32

        # Use the subset
        if(language=='hindi'):
            language = 'devanagari'
        # subfolder = os.path.join(inp_path, language)
        # subfolder = os.path.join(subfolder,sets)
        subfolder = inp_path

        # labels.json contains dict_keys(['img_dimensions', 'img_hash', 'polygons'])
        # there is no dimensions.json
        text_data= json.load(open(os.path.join(subfolder,'labels.json')))
        tmp_root = os.path.join(subfolder, "images")
        
        # if(sets!='test'):
        #     text_data= json.load(open(os.path.join(subfolder,'labels.json')))
        #     box_data= json.load(open(os.path.join(subfolder,'dimensions.json')))
        #     tmp_root = os.path.join(subfolder, "images")
        # else:
        #     tmp_root = subfolder

        # # List images
        self.data: List[Tuple[Union[str, np.ndarray], Union[str, Dict[str, Any]]]] = []
        message = "unpacking "+ language + " testset"
        for img_path in tqdm(iterable=os.listdir(tmp_root), desc=message, total=len(os.listdir(tmp_root))):           
            
            # File existence check
            if not os.path.exists(os.path.join(tmp_root, img_path)):
                raise FileNotFoundError(f"unable to locate {os.path.join(tmp_root, img_path)}")

            
            _targets = [
                (f'{img_path}_{word_num}',box[0]+box[3])
                # for filename in text_data
                for word_num,box in enumerate(text_data[img_path]['polygons'])
            ]
            # All the bounding boxes in Funsd are represented by their coordinates 
            # following the schema box = [xleft, ytop, xright, ybottom].
            
            # to get a list of words and their respective coordinates separately
            target_word_num, box_targets = zip(*_targets)
            
            # if(sets!='test'):
            #     text_targets = [text_data[img_path]]
            #     box_targets = [box_data[img_path]]
            #     image_names = [img_path]
            # else:
            #     text_targets = [""]
            #     im = Image.open(os.path.join(tmp_root, img_path))
            #     width, height = im.size
            #     box = [0 , 0, width, height]
            #     box_targets = [box]
            #     image_names = [img_path]

            if use_polygons:
                # xmin, ymin, xmax, ymax -> (x, y) coordinates of top left, top right, bottom right, bottom left corners
                box_targets = [
                    [
                        [box[0], box[1]],
                        [box[2], box[1]],
                        [box[2], box[3]],
                        [box[0], box[3]],
                    ]
                    for box in box_targets
                ]

            # if recognition_task:
            #     crops = crop_bboxes_from_image(
            #         img_path=os.path.join(tmp_root, img_path), geoms=np.asarray(box_targets, dtype=np_dtype)
            #     )
            #     for crop, label, name in zip(crops, list(text_targets), list(image_names)):
            #         # filter labels with unknown characters
            #         if not any(char in label for char in ["☑", "☐", "\uf703", "\uf702"]):
            #             self.data.append((crop, label, name))
            else:
                self.data.append(
                    (
                        img_path,
                        dict(boxes=np.asarray(box_targets, dtype=np_dtype), labels=list(target_word_num), images=list(target_word_num)),
                    )
                )
        self.root = tmp_root

    def extra_repr(self) -> str:
        return f"train={self.train}"
