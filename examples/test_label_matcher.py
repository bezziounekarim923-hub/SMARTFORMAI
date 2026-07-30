from pathlib import Path

from backend.core.field_detection.field_detector import FieldDetector
from backend.core.field_detection.label_matcher import LabelMatcher
from backend.core.layout.layout_analyzer import LayoutAnalyzer


def main():
    analyzer = LayoutAnalyzer()
    image_path = Path("datasets/rendered/page1.png")

    if not image_path.exists():
        raise FileNotFoundError(f"Image introuvable : {image_path.resolve()}")

    layout = analyzer.analyze_page(image_path)

    detector = FieldDetector()
    fields = detector.detect(layout.rectangles or [])

    matcher = LabelMatcher()
    fields = matcher.match(fields, layout.text_blocks or [])

    print("=" * 60)
    print("LABEL MATCHER")
    print("=" * 60)
    print(f"Image        : {image_path}")
    print(f"Champs détectés : {len(fields)}")
    print(f"Text blocks  : {len(layout.text_blocks or [])}")
    print()

    if not fields:
        print("Aucun champ détecté.")
        return

    for i, field in enumerate(fields, start=1):
        print(f"[{i}]")
        print(f"Type      : {field.field_type}")
        print(f"Label     : {field.label!r}")
        print(f"Rectangle : {field.rectangle}")
        print()


if __name__ == "__main__":
    main()