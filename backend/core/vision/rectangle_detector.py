import cv2

from backend.models.rectangle import Rectangle


class RectangleDetector:
    """
    Détecte les rectangles présents dans une image.
    """

    def detect(self, image):

        contours, _ = cv2.findContours(
            image,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        rectangles = []

        for contour in contours:

            x, y, w, h = cv2.boundingRect(contour)

            if w < 30:
                continue

            if h < 15:
                continue

            rectangles.append(
                Rectangle(
                    x=x,
                    y=y,
                    width=w,
                    height=h,
                )
            )

        return rectangles