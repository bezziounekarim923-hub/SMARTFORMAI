from os import PathLike
from pathlib import Path

import cv2
import numpy as np

from backend.core.ocr.ocr_factory import OCRFactory


class TextDetector:
    def __init__(self):
        self.engine = OCRFactory.create()

    def detect(self, image: PathLike | str | np.ndarray, max_width: int = 1200, max_height: int = 1200):
        if isinstance(image, PathLike):
            image = str(image)

        if isinstance(image, np.ndarray):
            image = self._resize_image(image, max_width, max_height)

        return self.engine.detect(image)

    def _resize_image(self, image: np.ndarray, max_width: int, max_height: int) -> np.ndarray:
        height, width = image.shape[:2]

        if width <= max_width and height <= max_height:
            return image

        scale = min(max_width / width, max_height / height)
        new_size = (int(width * scale), int(height * scale))

        return cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)