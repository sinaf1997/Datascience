# Statistical Engine & Simulation

## Project Overview
This project implements a pure-Python statistical engine and a Monte Carlo simulation to demonstrate statistical concepts and the Law of Large Numbers (LLN). The statistical engine processes raw numerical data, while the simulation models server failure probabilities.

## Features
### Core Statistical Engine
- **Central Tendency**: Mean, Median, Mode (handles multimodal distributions).
- **Dispersion**: Variance (Population and Sample), Standard Deviation.
- **Outlier Detection**: Identifies data points beyond a threshold of standard deviations.
- **Robust Error Handling**: Handles empty arrays and mixed data types gracefully.

### Monte Carlo Simulation
- Simulates server crashes with a 4.5% daily failure probability.
- Demonstrates the Law of Large Numbers by running simulations over different time periods.

## Mathematical Logic
- **Variance**: 
  \[ \sigma^2 = \frac{\sum (x_i - \mu)^2}{N} \] (Population)
  \[ s^2 = \frac{\sum (x_i - \mu)^2}{N-1} \] (Sample)
- **Median**: For even-length data, the median is the average of the two middle values.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd statistical_engine
   ```
2. Run the main script:
   ```bash
   python main.py
   ```

## Testing
Run the unit tests using:
```bash
python -m unittest discover tests
```

## Acceptance Criteria Checklist
- [x] Passes empty list handling.
- [x] Accurately calculates sample variance vs population variance.
- [x] Handles multimodal distributions in `get_mode`.
- [x] Simulates server crashes and calculates probabilities.
- [x] Fully documented and tested.

---

Developed as part of the Statistical Engineering & Simulation Assessment.
