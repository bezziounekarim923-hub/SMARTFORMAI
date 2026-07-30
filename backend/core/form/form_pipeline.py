from pathlib import Path

from backend.core.document.pdf_loader import PdfLoader


class FormPipeline:
    """
    Pipeline principal d'analyse d'un formulaire.
    """

    def process(self, pdf_path: Path):

        print("=" * 50)
        print("SMARTFORMAI PIPELINE")
        print("=" * 50)

        # Chargement du document
        document = PdfLoader(pdf_path).load()

        print("Document chargé")
        print(f"Pages : {document.page_count}")

        return document