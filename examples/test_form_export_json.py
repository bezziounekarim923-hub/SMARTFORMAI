import json
from pathlib import Path

from backend.core.form.form_analyzer import FormAnalyzer


def main(
    output_path: Path | str | None = None,
    pdf_path: Path | str | None = None,
) -> Path:
    analyzer = FormAnalyzer()

    pdf_path = Path(pdf_path or "datasets/forms/assurance.pdf")
    form = analyzer.analyze(pdf_path)

    output_path = Path(output_path or "output/form_structure.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as output_file:
        json.dump(form.to_dict(), output_file, ensure_ascii=False, indent=2)

    print("Form structure exported to:", output_path)
    return output_path


if __name__ == "__main__":
    main()
