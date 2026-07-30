from pathlib import Path

import fitz


class PDFWriter:
    """
    Écrit du texte dans un document PDF.
    """

    def write_text(
        self,
        input_pdf: Path,
        output_pdf: Path,
        page_number: int,
        x: float,
        y: float,
        text: str,
    ) -> None:

        print("Ouverture :", input_pdf)

        doc = fitz.open(str(input_pdf))

        page = doc[page_number]

        page.insert_text(
            (x, y),
            text,
            fontsize=12,
        )

        output_pdf.parent.mkdir(parents=True, exist_ok=True)

        print("Sauvegarde :", output_pdf)

        doc.save(str(output_pdf))
        doc.close()

        print("Terminé")