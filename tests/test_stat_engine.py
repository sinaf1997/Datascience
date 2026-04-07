import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):

    def test_get_mean(self):
        engine = StatEngine([1, 2, 3, 4, 5])
        self.assertEqual(engine.get_mean(), 3)

    def test_get_median_odd(self):
        engine = StatEngine([1, 3, 2])
        self.assertEqual(engine.get_median(), 2)

    def test_get_median_even(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_median(), 2.5)

    def test_get_mode_single(self):
        engine = StatEngine([1, 2, 2, 3])
        self.assertEqual(engine.get_mode(), [2])

    def test_get_mode_multiple(self):
        engine = StatEngine([1, 1, 2, 2, 3])
        self.assertEqual(engine.get_mode(), [1, 2])

    def test_get_mode_unique(self):
        engine = StatEngine([1, 2, 3])
        self.assertEqual(engine.get_mode(), "All values are unique.")

    def test_get_variance_population(self):
        engine = StatEngine([1, 2, 3, 4, 5])
        self.assertAlmostEqual(engine.get_variance(is_sample=False), 2.0)

    def test_get_variance_sample(self):
        engine = StatEngine([1, 2, 3, 4, 5])
        self.assertAlmostEqual(engine.get_variance(is_sample=True), 2.5)

    def test_get_standard_deviation(self):
        engine = StatEngine([1, 2, 3, 4, 5])
        self.assertAlmostEqual(engine.get_standard_deviation(), 1.5811, places=4)

    def test_get_outliers(self):
        engine = StatEngine([1, 2, 3, 100])
        self.assertEqual(engine.get_outliers(), [100])

    def test_empty_data(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_mixed_data(self):
        engine = StatEngine([1, 2, '3', None, 4])
        self.assertEqual(engine.get_mean(), 2.3333333333333335)

if __name__ == "__main__":
    unittest.main()