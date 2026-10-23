
import unittest
import pandas as pd

from pipeline import clean_data


class TestPipeline(unittest.TestCase):

    def test_duplicates_removed(self):
        df = pd.DataFrame({
            "Order_ID": [1, 1, 2],
            "Status": ["Delivered", "Delivered", "Delayed"]
        })

        result = clean_data(df)

        self.assertEqual(len(result), 2)

    def test_missing_rows_removed(self):
        df = pd.DataFrame({
            "Order_ID": [1, 2],
            "Status": ["Delivered", None]
        })

        result = clean_data(df)

        self.assertEqual(len(result), 1)

    def test_clean_data_preserves_valid_rows(self):
        df = pd.DataFrame({
            "Order_ID": [1, 2],
            "Status": ["Delivered", "Delayed"]
        })

        result = clean_data(df)

        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
