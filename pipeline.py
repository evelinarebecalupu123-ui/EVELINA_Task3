
import logging
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input.csv"
OUTPUT_FILE = BASE_DIR / "cleaned_output.csv"
LOG_FILE = BASE_DIR / "pipeline.log"

logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    force=True,
)


def clean_data(df):
    """Remove duplicate rows and rows containing missing values."""
    return df.drop_duplicates().dropna().copy()


def run_pipeline(input_file=INPUT_FILE, output_file=OUTPUT_FILE):
    try:
        input_file = Path(input_file)
        output_file = Path(output_file)

        if not input_file.exists():
            raise FileNotFoundError(
                f"Input dataset not found: {input_file}"
            )

        logging.info("Pipeline started")
        df = pd.read_csv(input_file)
        original_rows = len(df)

        cleaned_df = clean_data(df)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        cleaned_df.to_csv(output_file, index=False)

        logging.info("Original rows: %d", original_rows)
        logging.info("Clean rows: %d", len(cleaned_df))
        logging.info("Removed rows: %d", original_rows - len(cleaned_df))
        logging.info("Pipeline completed successfully")

        return cleaned_df

    except Exception:
        logging.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    result = run_pipeline()
    print("Pipeline completed successfully.")
    print("Cleaned rows:", len(result))
    print("Output file:", OUTPUT_FILE)
    print("Log file:", LOG_FILE)
