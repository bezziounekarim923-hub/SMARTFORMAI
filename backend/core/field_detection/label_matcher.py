from backend.models.form_field import FormField
from backend.models.text_block import TextBlock


class LabelMatcher:
    """
    Associe les blocs OCR aux champs détectés.
    """

    def __init__(
        self,
        row_tolerance=18,
        max_left_distance=350,
        max_above_distance=120,
        max_radius=250,
    ):

        self.row_tolerance = row_tolerance
        self.max_left_distance = max_left_distance
        self.max_above_distance = max_above_distance
        self.max_radius = max_radius

    def match(
        self,
        fields: list[FormField],
        text_blocks: list[TextBlock],
    ) -> list[FormField]:

        for field in fields:

            label = self._find_left(field, text_blocks)

            if label is None:
                label = self._find_above(field, text_blocks)

            if label is None:
                label = self._find_nearest(field, text_blocks)

            field.label = label.text if label else ""

        return fields

    ####################################################################

    def _find_left(
        self,
        field: FormField,
        text_blocks: list[TextBlock],
    ):

        fx = field.rectangle.x
        fy = field.rectangle.y
        fw = field.rectangle.width
        fh = field.rectangle.height

        field_center = fy + fh / 2

        best = None
        best_distance = 999999

        for block in text_blocks:

            label = block.text.strip()

            if not label:
                continue

            tx = block.bbox.x
            ty = block.bbox.y
            tw = block.bbox.width
            th = block.bbox.height

            text_center = ty + th / 2

            if abs(field_center - text_center) > self.row_tolerance:
                continue

            right = tx + tw

            if right > fx:
                continue

            distance = fx - right

            if distance > self.max_left_distance:
                continue

            if distance < best_distance:
                best_distance = distance
                best = block

        return best

    ####################################################################

    def _find_above(
        self,
        field: FormField,
        text_blocks: list[TextBlock],
    ):

        fx = field.rectangle.x
        fy = field.rectangle.y
        fw = field.rectangle.width

        best = None
        best_distance = 999999

        for block in text_blocks:

            label = block.text.strip()

            if not label:
                continue

            tx = block.bbox.x
            ty = block.bbox.y
            tw = block.bbox.width
            th = block.bbox.height

            bottom = ty + th

            if bottom > fy:
                continue

            distance = fy - bottom

            if distance > self.max_above_distance:
                continue

            if abs((tx + tw / 2) - (fx + fw / 2)) > fw:
                continue

            if distance < best_distance:
                best_distance = distance
                best = block

        return best

    ####################################################################

    def _find_nearest(
        self,
        field: FormField,
        text_blocks: list[TextBlock],
    ):

        fx = field.rectangle.x + field.rectangle.width / 2
        fy = field.rectangle.y + field.rectangle.height / 2

        best = None
        best_distance = 999999

        for block in text_blocks:

            label = block.text.strip()

            if not label:
                continue

            tx = block.bbox.x + block.bbox.width / 2
            ty = block.bbox.y + block.bbox.height / 2

            d = ((fx - tx) ** 2 + (fy - ty) ** 2) ** 0.5

            if d < best_distance:
                best_distance = d
                best = block

        if best_distance <= self.max_radius:
            return best

        return None