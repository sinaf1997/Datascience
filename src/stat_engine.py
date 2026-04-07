import math
from typing import List, Union


class StatEngine:
    def __init__(self, data: Union[List[float], List[int]]):
        """
        Initialize the statistical engine with cleaned numeric data.
        """

        # Ensure input is a list
        if not isinstance(data, list):
            raise TypeError("Data must be a list of numbers.")

        # Clean data (keep only numeric values)
        self.data = [x for x in data if isinstance(x, (int, float))]

        # Check if data is empty after cleaning
        if not self.data:
            raise ValueError("Data must contain at least one numerical value.")

    # -----------------------------
    # CENTRAL TENDENCY
    # -----------------------------
    def get_mean(self) -> float:
        """Return the mean (average) of the data."""
        return sum(self.data) / len(self.data)

    def get_median(self) -> float:
        """Return the median of the data."""
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def get_mode(self) -> Union[List[float], str]:
        """
        Return the mode(s) of the data.
        If all values are unique, return a message.
        """
        frequency = {}

        for num in self.data:
            frequency[num] = frequency.get(num, 0) + 1

        max_freq = max(frequency.values())

        modes = [num for num, freq in frequency.items() if freq == max_freq]

        # If every value appears once → no mode
        if max_freq == 1:
            return "No mode (all values are unique)"

        return modes

    # -----------------------------
    # DISPERSION
    # -----------------------------
    def get_variance(self, is_sample: bool = True) -> float:
        """
        Return variance.
        - Sample variance uses (n - 1)
        - Population variance uses n
        """
        n = len(self.data)

        if is_sample and n < 2:
            raise ValueError("Sample variance requires at least two data points.")

        mean = self.get_mean()

        squared_diffs = [(x - mean) ** 2 for x in self.data]

        if is_sample:
            return sum(squared_diffs) / (n - 1)  # Bessel's correction
        return sum(squared_diffs) / n

    def get_standard_deviation(self, is_sample: bool = True) -> float:
        """Return standard deviation."""
        return math.sqrt(self.get_variance(is_sample))

    # -----------------------------
    # OUTLIER DETECTION
    # -----------------------------
    def get_outliers(self, threshold: float = 2) -> List[float]:
        """
        Return values that are more than 'threshold'
        standard deviations away from the mean.
        """
        mean = self.get_mean()
        std_dev = self.get_standard_deviation()

        # Avoid division issues if std_dev is zero
        if std_dev == 0:
            return []

        return [
            x for x in self.data
            if abs((x - mean) / std_dev) > threshold
        ]