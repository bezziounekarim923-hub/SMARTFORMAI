import numpy as np

from backend.core.ocr.text_detector import TextDetector
from backend.models.form_field import FormField


class FieldLabeler:
    """
    Associe automatiquement un texte au champ le plus proche.
    """

    def __init__(self):
        self.ocr = TextDetector()

    def label(self, image, fields: list[FormField], blocks=None) -> list[FormField]:

        if not fields:
            return fields

        if blocks is None:
            if isinstance(image, np.ndarray):
                image = self._crop_label_region(image, fields)
            blocks = self.ocr.detect(image)

        for field in fields:

            best_block = None
            best_score = float("inf")

            fx = field.rectangle.x
            fy = field.rectangle.y + field.rectangle.height / 2

            for block in blocks:

                bx = block.bbox.x + block.bbox.width
                by = block.bbox.y + block.bbox.height / 2

                # Le texte doit être à gauche du champ
                if bx > fx:
                    continue

                dx = fx - bx
                dy = abs(fy - by)

                # Trop éloigné verticalement
                if dy > 35:
                    continue

                score = dx + (dy * 3)

                if score < best_score:
                    best_score = score
                    best_block = block

            if best_block:
                field.label = best_block.text.strip()

        return fields

    def _crop_label_region(self, image: np.ndarray, fields: list[FormField]) -> np.ndarray:
        height, width = image.shape[:2]

        # Crop only the left zone where labels are most likely to be located.
        # Keep the full vertical span so OCR block coordinates remain aligned
        # with the original field rectangles.
        left = 0
        right = min(width, int(max(field.rectangle.x for field in fields) + 200))

        if left >= right:
            return image

        return image[:, left:right]
