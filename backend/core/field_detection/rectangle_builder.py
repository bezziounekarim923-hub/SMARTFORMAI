from backend.models.rectangle import Rectangle


class RectangleBuilder:
    """
    Construit les rectangles à partir
    des lignes détectées.
    """

    TOLERANCE = 8


    def build(
        self,
        horizontal,
        vertical,
    ):

        rectangles = []


        for hx, hy, hw, hh in horizontal:

            for vx, vy, vw, vh in vertical:


                x = vx
                y = hy

                right = vx + vw
                bottom = hy + hh


                width = right - x
                height = bottom - y


                if width < 20:
                    continue

                if height < 15:
                    continue


                rectangles.append(
                    Rectangle(
                        x=x,
                        y=y,
                        width=width,
                        height=height,
                    )
                )


        return rectangles