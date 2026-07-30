from pathlib import Path

from backend.core.document.pdf_loader import PdfLoader
from backend.core.render.page_renderer import PageRenderer
from backend.core.image.image_preprocessor import ImagePreprocessor
from backend.core.vision.rectangle_detector import RectangleDetector


def main():

    loader = PdfLoader()
    renderer = PageRenderer()
    preprocessor = ImagePreprocessor()
    detector = RectangleDetector()

    document = loader.load(
        Path("datasets/forms/assurance.pdf")
    )

    page = document.pages[0]

    image = renderer.render(page)

    binary = preprocessor.preprocess(image)

    rectangles = detector.detect(binary)

    print("=" * 50)
    print("RECTANGLE DETECTOR")
    print("=" * 50)
    print(f"Rectangles détectés : {len(rectangles)}")

    for rect in rectangles[:20]:
        print(rect)


if __name__ == "__main__":
    main()