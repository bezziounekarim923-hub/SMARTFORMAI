from backend.models.form_field import FormField


class QuestionDetector:
    """
    Détecte les questions Oui / Non.
    """

    def detect(
        self,
        fields: list[FormField],
    ) -> list[FormField]:

        for field in fields:

            label = field.label.lower()

            if "oui" in label or "non" in label:
                continue

            if "?" in label:

                field.field_type = "yes_no"

                field.options = [
                    "Oui",
                    "Non",
                ]

        return fields