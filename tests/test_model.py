# tests/test_model.py

import joblib
import numpy as np
from housing_price.model import train_model
import unittest


class TestMathOperations(unittest.TestCase):

    def test_add(self):
        model = joblib.load('house_price_model.pkl')

        # Generate a sample input for prediction
        sample_input = np.array([[1550, 4, 2, 2, 2000]])

        # Make a prediction
        prediction = model.predict(sample_input)

        # Ensure the prediction is a non-negative value
        assert prediction >= 0


if __name__ == '__main__':
    unittest.main()
