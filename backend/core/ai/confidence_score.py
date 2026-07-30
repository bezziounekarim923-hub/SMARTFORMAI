class ConfidenceScore:
    """
    Calcule un score de confiance entre un label
    et une clé du profil.
    """

    def compute(
        self,
        label: str,
        key: str,
    ) -> float:

        label = label.lower().strip()
        key = key.lower().strip()

        if label == key:
            return 1.0

        if key in label:
            return 0.90

        if label in key:
            return 0.90

        words1 = set(label.split())
        words2 = set(key.split())

        common = len(words1 & words2)

        total = max(
            len(words1),
            len(words2),
        )

        if total == 0:
            return 0

        return common / total