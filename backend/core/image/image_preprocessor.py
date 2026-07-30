import cv2


class ImagePreprocessor:
    """
    Prépare une image avant la détection.
    """

    def preprocess(self, image):

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY,
        )

        gray = cv2.GaussianBlur(
            gray,
            (3, 3),
            0,
        )

        binary = cv2.threshold(
            gray,
            180,
            255,
            cv2.THRESH_BINARY_INV,
        )[1]

        return binary