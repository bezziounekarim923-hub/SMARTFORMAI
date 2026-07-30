from pathlib import Path

from backend.core.ai.form_understanding import FormUnderstanding


def main():

    engine = FormUnderstanding()

    form = engine.analyze(
        Path("datasets/forms/assurance.pdf")
    )

    print("=" * 60)
    print("FORM UNDERSTANDING")
    print("=" * 60)

    print(form.name)
    print()

    for field in form.fields:

        print(
            field.field_type,
            field.label,
        )


if __name__ == "__main__":
    main()