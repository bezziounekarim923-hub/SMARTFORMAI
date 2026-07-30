from pathlib import Path

import cv2

from backend.core.vision.line_detector import LineDetector

detector = LineDetector()

lines = detector.detect(Path("datasets/page1.png"))

cv2.imwrite("datasets/page1_lines.png", lines)

print("=" * 50)
print("Détection terminée")
print("=" * 50)
print("Image sauvegardée : datasets/page1_lines.png")