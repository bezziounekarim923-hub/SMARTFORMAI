from pathlib import Path

from backend.core.writer.pdf_writer import PDFWriter


def main():

    writer = PDFWriter()

    writer.write_text(
        input_pdf=Path("datasets/forms/assurance.pdf"),
        output_pdf=Path("output/assurance_rempli.pdf"),
        page_number=0,
        x=250,
        y=250,
        text="TEST SMARTFORMAI",
    )

    print("=" * 50)
    print("PDF rempli créé")
    print("=" * 50)


if __name__ == "__main__":
    main()