from pathlib import Path

from backend.core.ai.smart_form_engine import SmartFormEngine


def test_smart_form_engine_can_load_form():
    engine = SmartFormEngine()
    profile = {
        "nom": "Test",
        "prenom": "Utilisateur",
        "telephone": "0000000000",
        "adresse": "Rue de Test",
        "date_naissance": "1990-01-01",
        "proces_verbal": False,
    }

    form, mappings = engine.prepare(Path("datasets/forms/assurance.pdf"), profile)

    assert form is not None
    assert form.page_count == 1
    assert isinstance(form.fields, list)
    assert isinstance(mappings, list)


def test_smart_form_engine_maps_insurance_form_fields():
    engine = SmartFormEngine()
    profile = {
        "nom": "KHIARI",
        "prenom": "Mouloud",
        "telephone": "06665511917",
        "adresse": "Alger",
        "date_naissance": "1996-04-12",
        "proces_verbal": True,
    }

    form, mappings = engine.prepare(Path("datasets/forms/assurance.pdf"), profile)

    assert form is not None
    assert form.page_count == 1
    assert len(form.fields) > 0
    assert len(mappings) > 0

    mapped_keys = {mapping.profile_key for mapping in mappings}
    assert "nom" in mapped_keys
    assert "prenom" in mapped_keys
    assert "date_naissance" in mapped_keys

    assert all(
        0.0 <= mapping.confidence <= 1.0
        for mapping in mappings
    )

    assert all(
        mapping.field.field_type in {
            "text",
            "date",
            "checkbox",
            "radio",
            "textarea",
        }
        for mapping in mappings
    )
