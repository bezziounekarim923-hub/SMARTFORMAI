from pathlib import Path

from backend.core.form.form_analyzer import FormAnalyzer


class FormUnderstanding:
    """
    Comprend automatiquement un formulaire.
    """

    def __init__(self):

        self.analyzer = FormAnalyzer()

    def analyze(self, pdf_path: Path):

        form = self.analyzer.analyze(pdf_path)

        return form