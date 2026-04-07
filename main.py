from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes
import json

def main():
    # Load sample salaries
    with open("data/sample_salaries.json", "r") as file:
        salaries = json.load(file)

    # Statistical analysis
    engine = StatEngine(salaries)
    print("Mean salary:", engine.get_mean())
    print("Median salary:", engine.get_median())
    print("Mode salary:", engine.get_mode())
    print("Variance (Population):", engine.get_variance(is_sample=False))
    print("Standard Deviation (Population):", engine.get_standard_deviation(is_sample=False))
    print("Outliers:", engine.get_outliers())

    # Monte Carlo simulation
    for days in [30, 100, 10000]:
        probability = simulate_crashes(days)
        print(f"Simulated crash probability over {days} days: {probability:.4f}")

if __name__ == "__main__":
    main()