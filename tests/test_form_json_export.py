from backend.models.form import Form
from backend.models.form_field import FormField
from backend.models.rectangle import Rectangle


def test_form_to_dict_contains_expected_structure():
    rectangle = Rectangle(x=1, y=2, width=100, height=50)
    field = FormField(
        id="field_1",
        page=1,
        label="Nom",
        field_type="text",
        rectangle=rectangle,
        options=None,
    )

    form = Form(
        name="test_form",
        page_count=1,
        fields=[field],
    )

    result = form.to_dict()

    assert result["name"] == "test_form"
    assert result["page_count"] == 1
    assert isinstance(result["fields"], list)
    assert len(result["fields"]) == 1
    assert result["fields"][0]["id"] == "field_1"
    assert result["fields"][0]["rectangle"] == {
        "x": 1,
        "y": 2,
        "width": 100,
        "height": 50,
    }


def test_field_to_dict_includes_options_when_present():
    rectangle = Rectangle(x=5, y=10, width=20, height=20)
    field = FormField(
        id="checkbox_1",
        page=1,
        label="Oui",
        field_type="checkbox",
        rectangle=rectangle,
        options=["Oui", "Non"],
    )

    result = field.to_dict()

    assert result["options"] == ["Oui", "Non"]
    assert result["field_type"] == "checkbox"
