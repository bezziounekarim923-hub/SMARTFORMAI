from pathlib import Path

from backend.core.ai.smart_form_engine import SmartFormEngine


def main():

    profile = {
        "nom": "KHIARI",
        "prenom": "Mouloud",
        "telephone": "06665511917",
        "adresse": "Alger",
        "date_naissance": "1996-04-12",
        "proces_verbal": True,
    }

    engine = SmartFormEngine()

    # Utilisation de la méthode prepare()
    form, mappings = engine.prepare(
        Path("datasets/forms/assurance.pdf"),
        profile,
    )

    print("=" * 70)
    print("SMART FORM ENGINE")
    print("=" * 70)

    print()
    print(f"Formulaire : {form.name}")
    print()

    # -----------------------------
    # Champs détectés
    # -----------------------------
    print("=" * 70)
    print("CHAMPS DÉTECTÉS")
    print("=" * 70)

    for field in form.fields:
        print(
            f"Label='{field.label}' | "
            f"Type='{field.field_type}' | "
            f"x={field.rectangle.x} "
            f"y={field.rectangle.y}"
        )

    # -----------------------------
    # Mappings trouvés
    # -----------------------------
    print()
    print("=" * 70)
    print("MAPPINGS")
    print("=" * 70)

    if not mappings:
        print("Aucun mapping trouvé.")
    else:
        for mapping in mappings:
            print(
                f"{mapping.field.label:30}"
                f"{mapping.profile_key:20}"
                f"{str(mapping.value):20}"
                f"{mapping.confidence:.2f}"
            )


if __name__ == "__main__":
    main()