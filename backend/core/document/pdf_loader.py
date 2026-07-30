import fitz

from backend.core.document.loader import DocumentLoader
from backend.exceptions.document_exceptions import (
    DocumentNotFoundError,
    InvalidDocumentError,
)
from backend.models.document import Document
from backend.models.metadata import DocumentMetadata
from backend.models.page import Page


class PdfLoader(DocumentLoader):
    """
    Charge un document PDF et retourne un objet Document.
    """

    def load(self) -> Document:

        if not self.file_path.exists():
            raise DocumentNotFoundError(
                f"Le fichier '{self.file_path}' est introuvable."
            )

        try:
            pdf = fitz.open(self.file_path)

            # Création des objets Page
            pages = []

            for index in range(pdf.page_count):
                pdf_page = pdf.load_page(index)

                page = Page(
                    number=index + 1,
                    width=pdf_page.rect.width,
                    height=pdf_page.rect.height,
                )

                pages.append(page)

            # Métadonnées
            pdf_metadata = pdf.metadata or {}

            metadata = DocumentMetadata(
                title=pdf_metadata.get("title"),
                author=pdf_metadata.get("author"),
                subject=pdf_metadata.get("subject"),
                creator=pdf_metadata.get("creator"),
                producer=pdf_metadata.get("producer"),
            )

            # Création du document
            document = Document(
                path=self.file_path,
                page_count=pdf.page_count,
                metadata=metadata,
                pages=pages,
            )

            pdf.close()

            return document

        except Exception as error:
            raise InvalidDocumentError(
                "Impossible d'ouvrir le document PDF."
            ) from error