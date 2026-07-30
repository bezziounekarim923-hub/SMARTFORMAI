from pathlib import Path

from backend.core.image.image_preprocessor import ImagePreprocessor
from backend.core.render.page_renderer import PageRenderer
from backend.core.vision.rectangle_detector import RectangleDetector


renderer = PageRenderer()

image = renderer.render(
    Path("datasets/forms/assurance.pdf"),
    0,
)

binary = ImagePreprocessor().preprocess(image)

rectangles = RectangleDetector().detect(binary)

print("=" * 50)
print("RECTANGLES :", len(rectangles))
print("=" * 50)

for rect in rectangles[:20]:
    print(rect)