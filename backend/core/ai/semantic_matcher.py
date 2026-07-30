from difflib import SequenceMatcher


class SemanticMatcher:
    """
    Associe un label de formulaire avec la meilleure clé du profil.
    """

    def match(
        self,
        label: str,
        profile: dict,
    ) -> str | None:

        label = label.lower().strip()

        best_key = None
        best_score = 0

        for key in profile:

            score = SequenceMatcher(
                None,
                label,
                key.lower(),
            ).ratio()

            if score > best_score:
                best_score = score
                best_key = key

        if best_score < 0.45:
            return None

        return best_key