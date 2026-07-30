import re
import unicodedata


class TextCorrector:
    """
    Corrige et normalise les textes issus de l'OCR.
    """

    def normalize(self, text: str) -> str:

        if not text:
            return ""

        # Supprimer les espaces inutiles
        text = text.strip()

        # Supprimer les ":" finaux
        text = re.sub(r":+$", "", text)

        # Remplacer les espaces multiples
        text = re.sub(r"\s+", " ", text)

        # Remplacer quelques erreurs OCR fréquentes
        corrections = {
            "Prenom": "Prénom",
            "Teleph0ne": "Téléphone",
            "Telephone": "Téléphone",
            "E-mail": "Email",
            "e-mail": "Email",
            "Mail": "Email",
            "Date Naiss": "Date de naissance",
            "Date naissance": "Date de naissance",
            "CP": "Code postal",
        }

        if text in corrections:
            return corrections[text]

        return text

    def simplify(self, text: str) -> str:
        """
        Version simplifiée utilisée pour le matching.
        """

        text = self.normalize(text)

        text = unicodedata.normalize("NFD", text)
        text = "".join(
            c for c in text
            if unicodedata.category(c) != "Mn"
        )

        return text.lower()