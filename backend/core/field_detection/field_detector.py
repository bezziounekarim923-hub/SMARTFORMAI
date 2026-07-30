from backend.models.form_field import FormField
from backend.models.rectangle import Rectangle

from backend.core.field_detection.field_classifier import FieldClassifier


class FieldDetector:
    """
    Détecte les vrais champs parmi les rectangles.
    """

    MIN_WIDTH = 18
    MIN_HEIGHT = 12

    MAX_WIDTH = 1200
    MAX_HEIGHT = 600

    MAX_AREA = 120000

    def __init__(self):

        self.classifier = FieldClassifier()

    def detect(
        self,
        rectangles: list[Rectangle],
    ) -> list[FormField]:

        fields = []

        field_id = 1

        for rect in rectangles:

            w = rect.width
            h = rect.height

            # Trop petit
            if w < self.MIN_WIDTH or h < self.MIN_HEIGHT:
                continue

            # Trop grand
            if w > self.MAX_WIDTH or h > self.MAX_HEIGHT:
                continue

            # Aire trop importante
            if w * h > self.MAX_AREA:
                continue

            # Cadres de mise en page
            if w > 700 and h > 120:
                continue

            # Très haut = colonne
            if h > 250:
                continue

            field_type = self.classifier.classify(rect)

            # On ignore les objets inconnus
            if field_type == "unknown":
                continue

            # Limite les très grandes zones de texte
            if field_type == "textarea":
                if w > 450 or h > 180:
                    continue

            fields.append(
                FormField(
                    id=str(field_id),
                    page=1,
                    label="",
                    field_type=field_type,
                    rectangle=rect,
                )
            )

            field_id += 1

        return fields