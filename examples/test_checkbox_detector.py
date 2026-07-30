from pathlib import Path

from backend.core.form.form_analyzer import FormAnalyzer
from backend.core.field_detection.checkbox_detector import CheckboxDetector
from backend.core.image.image_preprocessor import ImagePreprocessor
from backend.core.render.page_renderer import PageRenderer
from backend.core.vision.rectangle_detector import RectangleDetector


def main():

    renderer = PageRenderer()
    preprocessor = ImagePreprocessor()
    rectangle_detector = RectangleDetector()
    checkbox_detector = CheckboxDetector()

    image = renderer.render(
        Path("datasets/forms/assurance.pdf"),
        0,
    )

    binary = preprocessor.preprocess(image)

    rectangles = rectangle_detector.detect(binary)

    checkboxes = checkbox_detector.detect(rectangles)

    print("=" * 50)
    print(f"Rectangles : {len(rectangles)}")
    print(f"Cases à cocher : {len(checkboxes)}")
    print("=" * 50)

    for checkbox in checkboxes:
        print(checkbox)


if __name__ == "__main__":
    main()