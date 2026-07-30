from pathlib import Path

import cv2
import fitz
import numpy as np


class PageRenderer:
    """
    Transforme une page PDF en image OpenCV.
    """

    def __init__(self, dpi: int = 300):
        self.dpi = dpi

    def render(self, pdf_path: Path, page_number: int):

        pdf = fitz.open(str(pdf_path))

        page = pdf.load_page(page_number)

        zoom = self.dpi / 72

        matrix = fitz.Matrix(zoom, zoom)

        pix = page.get_pixmap(matrix=matrix)

        img = np.frombuffer(
            pix.samples,
            dtype=np.uint8,
        )

        img = img.reshape(
            pix.height,
            pix.width,
            pix.n,
        )

        if pix.n == 4:
            img = cv2.cvtColor(
                img,
                cv2.COLOR_RGBA2BGR,
            )
        else:
            img = cv2.cvtColor(
                img,
                cv2.COLOR_RGB2BGR,
            )

        pdf.close()

        return img