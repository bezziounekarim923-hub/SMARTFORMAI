import cv2
import numpy as np


class LineDetector:
    """
    Détection des lignes horizontales et verticales
    d'un formulaire.
    """

    def detect(self, image):

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        binary = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY_INV,
            25,
            10,
        )

        horizontal = self.detect_horizontal(binary)

        vertical = self.detect_vertical(binary)

        return horizontal, vertical


    def detect_horizontal(self, binary):

        width = binary.shape[1]

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (
                max(20, width // 30),
                1
            )
        )

        lines = cv2.morphologyEx(
            binary,
            cv2.MORPH_OPEN,
            kernel
        )

        contours, _ = cv2.findContours(
            lines,
            cv2.RETR_LIST,
            cv2.CHAIN_APPROX_SIMPLE
        )

        result = []

        for c in contours:

            x, y, w, h = cv2.boundingRect(c)

            if w > 30 and h <= 5:

                result.append(
                    (x, y, w, h)
                )

        return result


    def detect_vertical(self, binary):

        height = binary.shape[0]

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (
                1,
                max(20, height // 30)
            )
        )

        lines = cv2.morphologyEx(
            binary,
            cv2.MORPH_OPEN,
            kernel
        )


        contours, _ = cv2.findContours(
            lines,
            cv2.RETR_LIST,
            cv2.CHAIN_APPROX_SIMPLE
        )

        result = []

        for c in contours:

            x, y, w, h = cv2.boundingRect(c)

            if h > 30 and w <= 5:

                result.append(
                    (x, y, w, h)
                )

        return result