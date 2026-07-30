from pathlib import Path

import cv2

from backend.core.ocr.text_detector import TextDetector
from backend.core.vision.line_detector import LineDetector
from backend.core.vision.rectangle_detector import RectangleDetector
from backend.models.form_field import FormField
from backend.models.page_layout import PageLayout
from backend.models.rectangle import Rectangle


class SmartLayoutAnalyzer:
    """
    Analyse avancée de la structure d'une page pour améliorer la détection.
    """

    def __init__(self):
        self.line_detector = LineDetector()
        self.rectangle_detector = RectangleDetector()
        self.text_detector = TextDetector()

    def analyze_page(self, image, fields=None, text_blocks=None) -> PageLayout:
        if isinstance(image, (str, Path)):
            image = cv2.imread(str(image))

            if image is None:
                raise FileNotFoundError(image)

        line_image = self.line_detector.detect(image)
        rectangles = self.rectangle_detector.detect(line_image)

        if text_blocks is None:
            text_blocks = self.text_detector.detect(image)

        tables = self._detect_tables(rectangles)
        checkbox_groups = self._detect_option_groups(fields or [])

        return PageLayout(
            page_number=1,
            rectangles=rectangles,
            text_blocks=text_blocks,
            checkboxes=checkbox_groups,
            tables=tables,
        )

    def analyze(self, image, fields=None) -> PageLayout:
        """Compatibilité avec l'interface attendue par FormAnalyzer."""
        return self.analyze_page(image, fields)

    def _detect_tables(self, rectangles: list[Rectangle]) -> list[Rectangle]:
        """
        Identifie les contours de tableaux à partir des rectangles extraits.
        """
        tables = []

        for rect in rectangles:
            if rect.width >= 150 and rect.height >= 80:
                aspect_ratio = rect.width / max(rect.height, 1)
                if aspect_ratio >= 1.25:
                    tables.append(rect)

        return tables

    def _detect_option_groups(self, fields: list[FormField]) -> list[list[FormField]]:
        """
        Regroupe les cases à cocher et les boutons radio proches.
        """
        groups = []
        candidates = [
            field
            for field in fields
            if field.field_type in ("checkbox", "radio")
        ]

        candidates.sort(key=lambda field: (field.rectangle.y, field.rectangle.x))

        current_group: list[FormField] = []

        for field in candidates:
            if not current_group:
                current_group = [field]
                continue

            previous = current_group[-1]
            if (
                abs(field.rectangle.y - previous.rectangle.y) <= 25
                or abs(field.rectangle.x - previous.rectangle.x) <= 70
            ):
                current_group.append(field)
            else:
                if len(current_group) > 1:
                    groups.append(current_group)
                current_group = [field]

        if len(current_group) > 1:
            groups.append(current_group)

        return groups
