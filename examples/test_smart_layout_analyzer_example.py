from pathlib import Path

from backend.core.form.form_analyzer import FormAnalyzer


def main() -> None:
    analyzer = FormAnalyzer()
    pdf_path = Path("datasets/forms/assurance.pdf")

    form = analyzer.analyze(pdf_path)

    print("=" * 70)
    print("SMART LAYOUT ANALYZER EXAMPLE")
    print("=" * 70)
    print(f"Formulaire : {form.name}")
    print(f"Pages : {form.page_count}")
    print(f"Champs détectés : {len(form.fields)}")
    print()
    print("=" * 70)
    print("CHAMPS DÉTECTÉS")
    print("=" * 70)

    for field in form.fields:
        print(
            f"{field.label:<30}"
            f"type={field.field_type:<10}"
            f"x={field.rectangle.x:<5}"
            f"y={field.rectangle.y:<5}"
            f"w={field.rectangle.width:<5}"
            f"h={field.rectangle.height}" 
        )


if __name__ == "__main__":
    main()
