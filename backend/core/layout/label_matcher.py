from backend.models.form_field import FormField
from backend.models.text_block import TextBlock


class LabelMatcher:
    """
    Associe les libellés OCR aux champs détectés.
    """

    def __init__(
        self,
        row_tolerance_ratio: float = 0.6,
        max_horizontal_ratio: float = 6.0,
        max_above_ratio: float = 3.0,
        max_fallback_distance: float = 250.0,
    ):
        self.row_tolerance_ratio = row_tolerance_ratio
        self.max_horizontal_ratio = max_horizontal_ratio
        self.max_above_ratio = max_above_ratio
        self.max_fallback_distance = max_fallback_distance

    def match(
        self,
        fields: list[FormField],
        text_blocks: list[TextBlock],
    ) -> list[FormField]:
        for field in fields:
            best_text = self._find_left_label(field, text_blocks)

            if best_text is None:
                best_text = self._find_above_label(field, text_blocks)

            if best_text is None:
                best_text = self._find_nearest_within_radius(field, text_blocks)

            field.label = best_text.text if best_text else ""

        return fields

    def _find_left_label(self, field: FormField, text_blocks: list[TextBlock]):
        rect = field.rectangle
        row_tol = rect.height * self.row_tolerance_ratio
        max_dx = rect.width * self.max_horizontal_ratio

        best_block = None
        best_dx = float("inf")

        for block in text_blocks:
            if not block.text.strip():
                continue

            bbox = block.bbox
            same_row = abs(bbox.center_y - rect.center_y) <= row_tol
            is_left = bbox.center_x < rect.center_x
            if not (same_row and is_left):
                continue

            dx = rect.center_x - bbox.center_x
            if dx > max_dx:
                continue

            if dx < best_dx:
                best_dx = dx
                best_block = block

        return best_block

    def _find_above_label(self, field: FormField, text_blocks: list[TextBlock]):
        rect = field.rectangle
        max_dy = rect.height * self.max_above_ratio
        max_dx = rect.width * 1.5

        best_block = None
        best_dy = float("inf")

        for block in text_blocks:
            if not block.text.strip():
                continue

            bbox = block.bbox
            is_above = bbox.center_y < rect.center_y
            aligned_x = abs(bbox.center_x - rect.center_x) <= max_dx
            if not (is_above and aligned_x):
                continue

            dy = rect.center_y - bbox.center_y
            if dy > max_dy:
                continue

            if dy < best_dy:
                best_dy = dy
                best_block = block

        return best_block

    def _find_nearest_within_radius(self, field: FormField, text_blocks: list[TextBlock]):
        rect = field.rectangle

        best_block = None
        best_distance = float("inf")

        for block in text_blocks:
            if not block.text.strip():
                continue

            bbox = block.bbox
            distance = ((rect.center_x - bbox.center_x) ** 2 + (rect.center_y - bbox.center_y) ** 2) ** 0.5

            if distance < best_distance:
                best_distance = distance
                best_block = block

        if best_block is not None and best_distance <= self.max_fallback_distance:
            return best_block

        return None