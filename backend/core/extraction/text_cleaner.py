class TextCleaner:
    """
    Corrige les erreurs courantes produites par l'OCR.
    """

    def clean(self, text: str) -> str:

        corrections = {
            "qmail": "gmail",
            "gmaiI": "gmail",
            "gmailcom": "gmail.com",
            "@gmailcom": "@gmail.com",
            " hotmailcom": "@hotmail.com",
            " com": ".com",
            " . com": ".com",
            "..": ".",
        }

        result = text

        for wrong, correct in corrections.items():
            result = result.replace(wrong, correct)

        return result.strip()