import re

from backend.models.form_field import FormField


class LabelCleaner:
    """
    Nettoie les labels détectés par l'OCR.
    """

    def clean(
        self,
        fields: list[FormField],
    ) -> list[FormField]:

        for field in fields:

            label = field.label.strip()

            # Supprimer les espaces multiples
            label = re.sub(r"\s+", " ", label)

            # Supprimer ":" final
            label = label.rstrip(" :;")

            # Trop court
            if len(label) < 3:
                field.label = ""
                continue

            # Trop de chiffres
            digits = sum(c.isdigit() for c in label)

            if digits > len(label) / 2:
                field.label = ""
                continue

            # Caractères parasites
            if re.search(r"[{}<>_=~`]", label):
                field.label = ""
                continue

            # Beaucoup de ponctuation
            punctuation = sum(
                not c.isalnum() and c != " "
                for c in label
            )

            if punctuation > 4:
                field.label = ""
                continue

            field.label = label

        return fields