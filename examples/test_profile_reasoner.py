from backend.core.ai.profile_reasoner import ProfileReasoner


def main():

    reasoner = ProfileReasoner()

    tests = [

        ("1996-04-12", "date"),

        ("12/04/1996", "date"),

        (True, "yes_no"),

        (False, "yes_no"),

        ("KHIARI", "text"),
    ]

    print("=" * 50)
    print("PROFILE REASONER")
    print("=" * 50)

    for value, field_type in tests:

        result = reasoner.adapt(
            value,
            field_type,
        )

        print(
            f"{value!r:15} -> {field_type:10} -> {result}"
        )


if __name__ == "__main__":
    main()