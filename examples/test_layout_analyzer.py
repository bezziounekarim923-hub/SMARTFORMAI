from pathlib import Path

from backend.core.layout.layout_analyzer import LayoutAnalyzer


def main():
    analyzer = LayoutAnalyzer()

    result = analyzer.analyze_page(Path("datasets/page1.png"))

    print("=" * 50)
    print("Layout Analyzer")
    print("=" * 50)
    print(f"Page : {result.page_number}")
    print(f"Rectangles détectés : {len(result.rectangles)}")


if __name__ == "__main__":
    main()