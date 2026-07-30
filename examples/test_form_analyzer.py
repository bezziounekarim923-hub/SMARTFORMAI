from pathlib import Path

from backend.core.form.form_analyzer import FormAnalyzer


def main():

    analyzer = FormAnalyzer()

    form = analyzer.analyze(
        Path("datasets/forms/assurance.pdf")
    )

    print("=" * 50)
    print("FORM ANALYZER")
    print("=" * 50)
    print(f"Nom : {form.name}")
    print(f"Pages : {form.page_count}")
    print(f"Nombre de champs : {len(form.fields)}")

    print()
    print("=" * 50)
    print("CHAMPS DÉTECTÉS")
    print("=" * 50)

    for field in form.fields:

        print(
            f"{field.label:<30}"
            f"x={field.rectangle.x:<5}"
            f" y={field.rectangle.y:<5}"
            f" w={field.rectangle.width:<5}"
            f" h={field.rectangle.height}"
        )


if __name__ == "__main__":
    main()