import re


class LabelClassifier:
    """
    Détermine si un texte OCR est un véritable label de champ.
    """

    def is_label(self, text: str) -> bool:

        if not text:
            return False

        text = text.strip()

        # Trop court
        if len(text) < 2:
            return False

        # Trop long
        if len(text) > 40:
            return False

        # Numéro de question
        if re.match(r"^\d+\)", text):
            return False

        # Beaucoup de chiffres
        digits = sum(c.isdigit() for c in text)

        if digits > len(text) / 2:
            return False

        # Titre entièrement en majuscules
        letters = [c for c in text if c.isalpha()]

        if letters:
            upper = sum(c.isupper() for c in letters)

            if upper / len(letters) > 0.8:
                return False

        return True