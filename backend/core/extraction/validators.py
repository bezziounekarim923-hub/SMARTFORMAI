import re


class Validators:
    """
    Vérifie les données extraites.
    """

    @staticmethod
    def is_email(value: str) -> bool:
        return re.fullmatch(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            value,
        ) is not None

    @staticmethod
    def is_phone(value: str) -> bool:
        digits = re.sub(r"\D", "", value)
        return len(digits) in (10, 11)

    @staticmethod
    def is_date(value: str) -> bool:
        return re.fullmatch(
            r"\d{2}/\d{2}/\d{4}",
            value,
        ) is not None