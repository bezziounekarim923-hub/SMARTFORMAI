import re

from backend.models.person import Person
from backend.core.extraction.text_cleaner import TextCleaner
from backend.core.extraction.validators import Validators


class PersonExtractor:
    """
    Extrait les informations d'une personne à partir des blocs OCR.
    """

    def _extract_name(self, text: str) -> tuple[str, str]:
        """
        Extrait le nom et le prénom à partir d'une ligne.
        """

        text = text.replace("Mr :", "")
        text = text.replace("Mr:", "")
        text = text.replace("Monsieur", "")
        text = text.strip()

        words = text.split()

        if len(words) >= 2:
            nom = words[0]
            prenom = " ".join(words[1:])
            return nom, prenom

        return "", ""

    def extract(self, text_blocks) -> Person:

        person = Person()

        cleaner = TextCleaner()

        for block in text_blocks:

            # Nettoyage du texte OCR
            text = cleaner.clean(block.text)

            # Nom et prénom
            if text.startswith("Mr") or text.startswith("Monsieur"):
                nom, prenom = self._extract_name(text)
                person.nom = nom
                person.prenom = prenom

            # Email
            if Validators.is_email(text):
                person.email = text

            # Téléphone
            phone = re.search(r"0\d{9,10}", text)
            if phone and Validators.is_phone(phone.group()):
                person.telephone = phone.group()

            # Date de naissance
            date = re.search(r"\d{2}/\d{2}/\d{4}", text)
            if date and Validators.is_date(date.group()):
                person.date_naissance = date.group()

        return person