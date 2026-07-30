from pathlib import Path

from backend.core.field_detection.field_detector import FieldDetector
from backend.core.field_detection.field_labeler import FieldLabeler
from backend.core.form.form_builder import FormBuilder
from backend.core.image.image_preprocessor import ImagePreprocessor
from backend.core.layout.smart_layout_analyzer import SmartLayoutAnalyzer
from backend.core.render.page_renderer import PageRenderer
from backend.core.vision.rectangle_detector import RectangleDetector

from backend.models.form import Form


class FormAnalyzer:
    """
    Analyse un formulaire PDF et détecte automatiquement les champs.
    """

    def __init__(self):
        self.renderer = PageRenderer()
        self.preprocessor = ImagePreprocessor()
        self.rectangle_detector = RectangleDetector()
        self.field_detector = FieldDetector()
        self.labeler = FieldLabeler()
        self.layout_analyzer = SmartLayoutAnalyzer()
        self.builder = FormBuilder()

    def analyze(self, pdf_path: Path) -> Form:
        """
        Analyse complète d'un formulaire PDF.
        """
        image = self.renderer.render(pdf_path, 0)
        binary = self.preprocessor.preprocess(image)
        rectangles = self.rectangle_detector.detect(binary)
        fields = self.field_detector.detect(rectangles)

        text_blocks = self.layout_analyzer.text_detector.detect(image)
        fields = self.labeler.label(image, fields, blocks=text_blocks)
        page_layout = self.layout_analyzer.analyze_page(image, fields, text_blocks=text_blocks)

        return self.builder.build(fields, page_layout)