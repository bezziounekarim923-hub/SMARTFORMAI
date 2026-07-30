from math import fabs


class SpatialLinker:
    """
    Associe chaque champ au meilleur bloc OCR.

    Un bloc OCR ne peut être utilisé qu'une seule fois.
    """

    MAX_HORIZONTAL_DISTANCE = 350
    MAX_VERTICAL_DISTANCE = 35

    def link(self, graph):

        used_texts = set()

        for field in graph.fields():

            best = None
            best_score = -100000

            for text in graph.texts():

                if text.id in used_texts:
                    continue

                score = self.compute_score(field, text)

                if score > best_score:
                    best_score = score
                    best = text

            if best is not None and best_score > 25:

                field.text = best.text
                field.score = best_score

                used_texts.add(best.id)

            else:

                field.text = ""
                field.score = 0

        return graph

    ##################################################################

    def compute_score(self, field, text):

        score = 0

        fx = field.rectangle.x
        fy = field.rectangle.y
        fw = field.rectangle.width
        fh = field.rectangle.height

        tx = text.rectangle.x
        ty = text.rectangle.y
        tw = text.rectangle.width
        th = text.rectangle.height

        field_center = fy + fh / 2
        text_center = ty + th / 2

        vertical = fabs(field_center - text_center)

        # -------------------------------------------------------
        # Alignement vertical
        # -------------------------------------------------------

        if vertical < 10:
            score += 45

        elif vertical < 18:
            score += 30

        elif vertical < self.MAX_VERTICAL_DISTANCE:
            score += 15

        else:
            score -= 50

        # -------------------------------------------------------
        # Texte situé à gauche
        # -------------------------------------------------------

        right = tx + tw

        if right <= fx:

            distance = fx - right

            score += 60

            if distance < 20:
                score += 35

            elif distance < 60:
                score += 25

            elif distance < 120:
                score += 15

            elif distance < self.MAX_HORIZONTAL_DISTANCE:
                score += 5

            else:
                score -= 30

        else:

            score -= 70

        # -------------------------------------------------------
        # Hauteur similaire
        # -------------------------------------------------------

        if abs(fh - th) < 8:
            score += 10

        # -------------------------------------------------------
        # Texte vide
        # -------------------------------------------------------

        label = text.text.strip()

        if not label:
            return -999

        # -------------------------------------------------------
        # Très long paragraphe
        # -------------------------------------------------------

        if len(label) > 120:
            score -= 120

        elif len(label) > 80:
            score -= 60

        # -------------------------------------------------------
        # Gros titre
        # -------------------------------------------------------

        if tw > 1200:
            score -= 200

        if th > 90:
            score -= 120

        # -------------------------------------------------------
        # OCR peu fiable
        # -------------------------------------------------------

        if text.confidence < 0.60:
            score -= 40

        return score