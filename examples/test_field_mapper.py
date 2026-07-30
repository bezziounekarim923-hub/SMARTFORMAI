from backend.core.mapping.field_mapper import FieldMapper
from backend.models.form import Form
from backend.models.form_field import FormField
from backend.models.rectangle import Rectangle


def main():

    form = Form(
        name="Assurance",
        page_count=1,
        fields=[
            FormField(
                id="1",
                label="Nom",
                field_type="text",
                rectangle=Rectangle(100, 100, 200, 40),
                page=1,
            ),
            FormField(
                id="2",
                label="Prénom",
                field_type="text",
                rectangle=Rectangle(100, 180, 200, 40),
                page=1,
            ),
            FormField(
                id="3",
                label="Téléphone",
                field_type="text",
                rectangle=Rectangle(100, 260, 200, 40),
                page=1,
            ),
        ],
    )

    profile = {
        "nom": "KHIARI",
        "prenom": "Mouloud",
        "telephone": "06665511917",
    }

    mapper = FieldMapper()

    mappings = mapper.map(form, profile)

    print("=" * 50)
    print("FIELD MAPPER")
    print("=" * 50)

    for mapping in mappings:
        print(f"{mapping.profile_key} -> {mapping.field.label} = {mapping.value}")


if __name__ == "__main__":
    main()