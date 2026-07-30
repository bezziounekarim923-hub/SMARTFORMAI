from pathlib import Path

from backend.core.ocr.text_detector import TextDetector


def main():
    detector = TextDetector()

    results = detector.detect(Path("datasets/page1.png"))

    print("=" * 50)
    print("Texte détecté")
    print("=" * 50)

    for block in results:
        print("=" * 40)
        print("Texte :", block.text)
        print("Confiance :", block.confidence)
        print("Rectangle :", block.bbox)


if __name__ == "__main__":
    main()