from pathlib import Path

import numpy as np

from backend.core.vision.line_detector import LineDetector
from backend.core.vision.rectangle_detector import RectangleDetector
from backend.core.ocr.text_detector import TextDetector

from backend.models.page_layout import PageLayout


class LayoutAnalyzer:
    """
    Analyse la structure graphique d'une page.
    """

    def __init__(self):
        self.line_detector = LineDetector()
        self.rectangle_detector = RectangleDetector()
        self.text_detector = TextDetector()

    def analyze_page(self, image_path: Path) -> PageLayout:
        """
        Analyse une page et retourne les éléments détectés.
        """
        line_image = self.line_detector.detect(image_path)
        rectangles = self.rectangle_detector.detect(line_image)
        text_blocks = self.text_detector.detect(image_path)

        return PageLayout(
            page_number=1,
            rectangles=rectangles,
            text_blocks=text_blocks,
        )

    def analyze(self, image_path: Path, fields=None) -> PageLayout:
        """
        Méthode de compatibilité pour FormAnalyzer.
        """
        return self.analyze_page(image_path)