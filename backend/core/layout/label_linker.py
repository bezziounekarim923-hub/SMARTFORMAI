from backend.core.layout.label_matcher import LabelMatcher


class SpatialLinker:
    """
    Associe les textes aux champs grâce à un score.
    """

    def __init__(self):
        self.matcher = LabelMatcher()

    def link(self, graph):
        fields = graph.fields()
        texts = graph.texts()

        used_texts = set()

        for field in fields:
            best = None
            best_score = float("inf")

            for text in texts:
                if text.id in used_texts:
                    continue

                score = self.matcher.score(field, text)
                if score is None:
                    continue

                if score < best_score:
                    best_score = score
                    best = text

            if best is not None:
                field.text = best.text
                used_texts.add(best.id)

        return graph