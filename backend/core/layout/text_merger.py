from copy import deepcopy


class TextMerger:
    """
    Fusionne uniquement les blocs OCR qui appartiennent
    réellement au même label.
    """

    MAX_HORIZONTAL_GAP = 25
    MAX_VERTICAL_GAP = 8
    MAX_X_OFFSET = 20

    def merge(self, blocks):

        blocks = sorted(
            deepcopy(blocks),
            key=lambda b: (b.bbox.y, b.bbox.x),
        )

        merged = []
        used = [False] * len(blocks)

        for i, current in enumerate(blocks):

            if used[i]:
                continue

            changed = True

            while changed:

                changed = False

                for j in range(i + 1, len(blocks)):

                    if used[j]:
                        continue

                    candidate = blocks[j]

                    if self.can_merge(current, candidate):

                        current = self.merge_two(current, candidate)

                        used[j] = True

                        changed = True

            merged.append(current)

        return merged

    ############################################################

    def can_merge(self, a, b):

        ax = a.bbox.x
        ay = a.bbox.y
        aw = a.bbox.width
        ah = a.bbox.height

        bx = b.bbox.x
        by = b.bbox.y
        bw = b.bbox.width
        bh = b.bbox.height

        # Évite les gros paragraphes
        if aw > 800 or bw > 800:
            return False

        if ah > 80 or bh > 80:
            return False

        # Même ligne
        if abs((ay + ah / 2) - (by + bh / 2)) < 8:

            gap = bx - (ax + aw)

            if 0 <= gap <= self.MAX_HORIZONTAL_GAP:
                return True

        # Ligne suivante avec même alignement
        if abs(ax - bx) <= self.MAX_X_OFFSET:

            gap = by - (ay + ah)

            if 0 <= gap <= self.MAX_VERTICAL_GAP:
                return True

        return False

    ############################################################

    def merge_two(self, a, b):

        a.text = a.text.strip() + " " + b.text.strip()

        x = min(a.bbox.x, b.bbox.x)
        y = min(a.bbox.y, b.bbox.y)

        right = max(
            a.bbox.x + a.bbox.width,
            b.bbox.x + b.bbox.width,
        )

        bottom = max(
            a.bbox.y + a.bbox.height,
            b.bbox.y + b.bbox.height,
        )

        a.bbox.x = x
        a.bbox.y = y
        a.bbox.width = right - x
        a.bbox.height = bottom - y

        if hasattr(a, "confidence") and hasattr(b, "confidence"):
            a.confidence = max(a.confidence, b.confidence)

        return a