import json
from pathlib import Path


def test_form_export_json_example_creates_output_file(tmp_path):
    from examples.test_form_export_json import main

    output_path = tmp_path / "form_structure.json"
    pdf_path = Path("datasets/forms/assurance.pdf")

    result_path = main(output_path=output_path, pdf_path=pdf_path)

    assert result_path == output_path
    assert output_path.exists()

    data = json.loads(output_path.read_text(encoding="utf-8"))

    assert isinstance(data, dict)
    assert "name" in data
    assert "fields" in data
    assert isinstance(data["fields"], list)
