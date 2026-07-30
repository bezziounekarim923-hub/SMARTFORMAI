from pathlib import Path

from backend.core.layout.layout_analyzer import LayoutAnalyzer
from backend.core.field_detection.field_detector import FieldDetector


def main():
    analyzer = LayoutAnalyzer()
    layout = analyzer.analyze_page(Path("datasets/page1_lines.png"))

    detector = FieldDetector()

    fields = detector.detect(layout.rectangles)

    print("=" * 50)
    print("Field Detector")
    print("=" * 50)

    print(f"Nombre de champs : {len(fields)}")

    for field in fields:
        print(field)


if __name__ == "__main__":
    main()