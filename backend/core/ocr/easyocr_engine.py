from pathlib import Path
from easyocr import Reader

from backend.models.rectangle import Rectangle
from backend.models.text_block import TextBlock


class EasyOCREngine:
    def __init__(self, languages=None, gpu=False):
        self.reader = Reader(lang_list=languages or ["fr", "en"], gpu=gpu)

    def detect(self, image):
        if isinstance(image, Path):
            image = str(image)

        results = self.reader.readtext(image)
        detected = []

        for bbox, text, confidence in results:
            xs = [int(point[0]) for point in bbox]
            ys = [int(point[1]) for point in bbox]
            rectangle = Rectangle(
                x=min(xs),
                y=min(ys),
                width=max(xs) - min(xs),
                height=max(ys) - min(ys),
            )
            detected.append(
                TextBlock(
                    text=text,
                    rectangle=rectangle,
                    confidence=float(confidence),
                )
            )

        return detected