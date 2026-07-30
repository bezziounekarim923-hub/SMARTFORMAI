from pathlib import Path

from backend.core.mapping.form_filler import FormFiller
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
                rectangle=Rectangle(100, 150, 200, 40),
                page=1,
            ),
            FormField(
                id="3",
                label="Téléphone",
                field_type="text",
                rectangle=Rectangle(100, 200, 200, 40),
                page=1,
            ),
        ],
    )

    profile = {
        "nom": "KHIARI",
        "prenom": "Mouloud",
        "telephone": "06665511917",
    }

    filler = FormFiller()

    filler.fill(
        input_pdf=Path("datasets/forms/assurance.pdf"),
        output_pdf=Path("output/assurance_rempli.pdf"),
        form=form,
        profile=profile,
    )

    print("=" * 50)
    print("FORM FILLER")
    print("=" * 50)
    print("Formulaire rempli avec succès.")


if __name__ == "__main__":
    main()