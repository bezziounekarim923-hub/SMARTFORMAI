from backend.core.ai.semantic_matcher import SemanticMatcher


def main():

    profile = {
        "nom": "KHIARI",
        "prenom": "Mouloud",
        "telephone": "06665511917",
        "adresse": "Alger",
        "date_naissance": "12/04/1996",
    }

    matcher = SemanticMatcher()

    labels = [
        "Nom",
        "Prénom",
        "Téléphone",
        "Adresse",
        "Date de naissance",
    ]

    print("=" * 50)
    print("SEMANTIC MATCHER")
    print("=" * 50)

    for label in labels:

        key = matcher.match(
            label,
            profile,
        )

        print(f"{label:25} -> {key}")


if __name__ == "__main__":
    main()