from pathlib import Path

from backend.core.form.form_pipeline import FormPipeline


def main():

    pipeline = FormPipeline()

    pipeline.process(
        Path("datasets/forms/assurance.pdf")
    )


if __name__ == "__main__":
    main()