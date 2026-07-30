from backend.models.rectangle import Rectangle


class FieldClassifier:
    """
    Classe les rectangles détectés.
    """

    def classify(self, rectangle: Rectangle) -> str:

        w = rectangle.width
        h = rectangle.height

        if h <= 0:
            return "unknown"

        ratio = w / h

        # ------------------------------------
        # Trop petit
        # ------------------------------------

        if w < 18 or h < 12:
            return "unknown"

        # ------------------------------------
        # Checkbox
        # ------------------------------------

        if (
            22 <= w <= 42
            and
            22 <= h <= 42
            and
            0.80 <= ratio <= 1.20
        ):
            return "checkbox"

        # ------------------------------------
        # Radio
        # ------------------------------------

        if (
            38 <= w <= 60
            and
            30 <= h <= 60
            and
            0.70 <= ratio <= 1.35
        ):
            return "radio"

        # ------------------------------------
        # Date
        # ------------------------------------

        if (
            70 <= w <= 180
            and
            16 <= h <= 38
            and
            ratio >= 2.5
        ):
            return "date"

        # ------------------------------------
        # Champ texte
        # ------------------------------------

        if (
            90 <= w <= 700
            and
            16 <= h <= 45
            and
            ratio >= 2
        ):
            return "text"

        # ------------------------------------
        # Zone de texte
        # ------------------------------------

        if (
            w >= 150
            and
            h >= 45
        ):
            return "textarea"

        return "unknown"