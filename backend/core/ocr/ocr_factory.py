from backend.core.ocr.paddleocr_engine import PaddleOCREngine


class OCRFactory:

    @staticmethod
    def create():

        return PaddleOCREngine()