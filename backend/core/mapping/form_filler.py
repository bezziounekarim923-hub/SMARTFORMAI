from pathlib import Path

from backend.core.mapping.field_mapper import FieldMapper
from backend.core.writer.pdf_writer import PDFWriter


class FormFiller:
    """
    Remplit automatiquement un formulaire PDF.
    """

    def fill(
        self,
        input_pdf: Path,
        output_pdf: Path,
        form,
        profile,
    ) -> None:

        mapper = FieldMapper()
        writer = PDFWriter()

        mappings = mapper.map(form, profile)

        # Ouvre le PDF une seule fois
        import fitz

        doc = fitz.open(str(input_pdf))

        for mapping in mappings:

            page = doc[mapping.field.page - 1]

            rect = mapping.field.rectangle

            page.insert_text(
                (rect.x + 5, rect.y + rect.height - 5),
                mapping.value,
                fontsize=10,
            )

        output_pdf.parent.mkdir(parents=True, exist_ok=True)

        doc.save(str(output_pdf))
        doc.close()