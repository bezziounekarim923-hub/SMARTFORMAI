from backend.models.form_field import FormField


class FieldValidator:
    """
    Supprime les faux champs en utilisant les blocs OCR.
    """

    def __init__(self):

        self.max_overlap = 0.45

    def validate(
        self,
        fields: list[FormField],
        text_blocks,
    ) -> list[FormField]:

        valid = []

        for field in fields:

            keep = True

            fx = field.rectangle.x
            fy = field.rectangle.y
            fw = field.rectangle.width
            fh = field.rectangle.height

            field_area = fw * fh

            for block in text_blocks:

                if not block.text.strip():
                    continue

                tx = block.bbox.x
                ty = block.bbox.y
                tw = block.bbox.width
                th = block.bbox.height

                x1 = max(fx, tx)
                y1 = max(fy, ty)

                x2 = min(fx + fw, tx + tw)
                y2 = min(fy + fh, ty + th)

                if x2 <= x1 or y2 <= y1:
                    continue

                overlap = (x2 - x1) * (y2 - y1)

                ratio = overlap / field_area

                if ratio > self.max_overlap:
                    keep = False
                    break

            if keep:
                valid.append(field)

        return valid