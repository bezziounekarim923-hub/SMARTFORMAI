from os import PathLike
from pathlib import Path

import cv2
import numpy as np
from paddleocr import PaddleOCR

from backend.core.ocr.ocr_engine import OCREngine
from backend.models.rectangle import Rectangle
from backend.models.text_block import TextBlock


class PaddleOCREngine(OCREngine):
    """
    Implémentation OCR basée sur PaddleOCR.
    """

    def __init__(self):
        params = {"lang": "fr", "use_angle_cls": True}
        try:
            self.reader = PaddleOCR(**params)
        except (TypeError, ValueError):
            params.pop("use_angle_cls", None)
            self.reader = PaddleOCR(**params)

    def _normalize_path(self, image):
        if isinstance(image, (PathLike, Path)):
            return str(image)

        if isinstance(image, np.ndarray):
            if image.ndim == 3 and image.shape[2] == 4:
                image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
            elif image.ndim == 3 and image.shape[2] == 3:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        return image

    def _flatten_results(self, results):
        if not results:
            return []

        if isinstance(results[0], list) and len(results[0]) > 0 and isinstance(results[0][0], list):
            return [item for page in results for item in page]

        return results

    def detect(self, image) -> list[TextBlock]:
        image = self._normalize_path(image)

        method = getattr(self.reader, "predict", None) or getattr(self.reader, "ocr", None)
        if method is None:
            raise RuntimeError("No OCR method available on PaddleOCR reader")

        results = method(image)
        if not results:
            return []

        first = results[0]
        if self._is_rec_output(first):
            return self._parse_rec_output(
                first["rec_texts"] if isinstance(first, dict) else first.rec_texts,
                first.get("rec_scores", []) if isinstance(first, dict) else getattr(first, "rec_scores", []),
                first["rec_polys"] if isinstance(first, dict) else first.rec_polys,
            )

        if isinstance(first, dict) and "ocr_result" in first:
            lines = first["ocr_result"]
        else:
            lines = self._flatten_results(results)

        blocks = []
        for line in lines:
            if len(line) != 2:
                continue

            bbox, rec = line
            text = rec[0]
            score = float(rec[1])

            xs = [int(point[0]) for point in bbox]
            ys = [int(point[1]) for point in bbox]

            blocks.append(
                TextBlock(
                    text=str(text),
                    confidence=score,
                    rectangle=Rectangle(
                        x=min(xs),
                        y=min(ys),
                        width=max(xs) - min(xs),
                        height=max(ys) - min(ys),
                    ),
                )
            )

        return blocks

    def _is_rec_output(self, page):
        if isinstance(page, dict):
            return "rec_texts" in page and "rec_polys" in page

        if hasattr(page, "keys"):
            try:
                return "rec_texts" in page.keys() and "rec_polys" in page.keys()
            except Exception:
                pass

        return hasattr(page, "rec_texts") and hasattr(page, "rec_polys")

    def _parse_rec_output(self, texts, scores, polys) -> list[TextBlock]:
        blocks = []

        for text, score, poly in zip(texts, scores, polys):
            if not text:
                continue

            xs = [int(point[0]) for point in poly]
            ys = [int(point[1]) for point in poly]

            blocks.append(
                TextBlock(
                    text=str(text),
                    confidence=float(score) if score is not None else 0.0,
                    rectangle=Rectangle(
                        x=min(xs),
                        y=min(ys),
                        width=max(xs) - min(xs),
                        height=max(ys) - min(ys),
                    ),
                )
            )

        return blocks