from pathlib import Path

from backend.core.extraction.person_extractor import PersonExtractor
from backend.core.ocr.text_detector import TextDetector


def main():

    detector = TextDetector()

    blocks = detector.detect(Path("datasets/rendered/page1.png"))

    extractor = PersonExtractor()

    person = extractor.extract(blocks)

    print("=" * 50)
    print("PERSON EXTRACTOR")
    print("=" * 50)

    
    print("Nom :", person.nom)
    print("Prénom :", person.prenom)
    print("Téléphone :", person.telephone)
    print("Email :", person.email)
    print("Date naissance :", person.date_naissance)


if __name__ == "__main__":
    main()