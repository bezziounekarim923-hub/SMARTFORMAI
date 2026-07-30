from backend.core.field_detection.line_detector import LineDetector
from backend.core.field_detection.rectangle_builder import RectangleBuilder
from backend.core.field_detection.duplicate_filter import DuplicateFilter


class RectangleDetector:
    """
    Détecteur de rectangles de formulaires V2.

    Pipeline :

    Image
      |
      |-- LineDetector
      |
      |-- RectangleBuilder
      |
      |-- DuplicateFilter
      |
      --> Rectangles propres
    """


    def __init__(self):

        self.line_detector = LineDetector()

        self.builder = RectangleBuilder()

        self.filter = DuplicateFilter()



    def detect(self, image):

        # Détection des lignes
        horizontal, vertical = self.line_detector.detect(
            image
        )


        # Construction des rectangles
        rectangles = self.builder.build(
            horizontal,
            vertical
        )


        # Suppression doublons
        rectangles = self.filter.clean(
            rectangles
        )


        return rectangles