from backend.models.rectangle import Rectangle


class CheckboxDetector:
    """
    Détecte les cases à cocher parmi les rectangles.
    """

    MIN_SIZE = 10
    MAX_SIZE = 40

    def detect(self, rectangles: list[Rectangle]) -> list[Rectangle]:

        checkboxes = []

        for rect in rectangles:

            w = rect.width
            h = rect.height

            # Les cases sont presque carrées
            if abs(w - h) > 8:
                continue

            if w < self.MIN_SIZE or w > self.MAX_SIZE:
                continue

            if h < self.MIN_SIZE or h > self.MAX_SIZE:
                continue

            checkboxes.append(rect)

        return checkboxes