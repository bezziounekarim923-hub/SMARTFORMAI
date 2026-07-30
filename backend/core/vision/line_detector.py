from pathlib import Path

import cv2
import numpy as np


class LineDetector:
    """
    Détecte les lignes horizontales et verticales
    d'une image.

    Accepte :
    - un Path
    - une image OpenCV (numpy.ndarray)
    """

    def detect(self, image):

        # -----------------------------
        # Chargement de l'image
        # -----------------------------
        if isinstance(image, (str, Path)):

            image = cv2.imread(str(image))

            if image is None:
                raise FileNotFoundError(image)

        elif not isinstance(image, np.ndarray):

            raise TypeError(
                "Le paramètre image doit être un Path ou une image OpenCV."
            )

        # -----------------------------
        # Passage en niveaux de gris
        # -----------------------------
        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY,
        )

        # -----------------------------
        # Binarisation
        # -----------------------------
        _, thresh = cv2.threshold(
            gray,
            180,
            255,
            cv2.THRESH_BINARY_INV,
        )

        # -----------------------------
        # Détection des lignes horizontales
        # -----------------------------
        horizontal_kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (40, 1),
        )

        horizontal = cv2.morphologyEx(
            thresh,
            cv2.MORPH_OPEN,
            horizontal_kernel,
        )

        # -----------------------------
        # Détection des lignes verticales
        # -----------------------------
        vertical_kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            (1, 40),
        )

        vertical = cv2.morphologyEx(
            thresh,
            cv2.MORPH_OPEN,
            vertical_kernel,
        )

        # -----------------------------
        # Fusion des lignes
        # -----------------------------
        lines = cv2.bitwise_or(
            horizontal,
            vertical,
        )

        return lines