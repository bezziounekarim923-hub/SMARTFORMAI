from pathlib import Path

from backend.core.ai.smart_form_engine import SmartFormEngine as CoreSmartFormEngine


class SmartFormEngine(CoreSmartFormEngine):
    """
    Alias de compatibilité pour le moteur SmartFormAI.
    """

    def analyze(
        self,
        pdf_path: Path,
        profile: dict,
    ):
        return self.prepare(pdf_path, profile)
