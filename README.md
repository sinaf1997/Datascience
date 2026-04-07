# Statistical Engineering & Simulation Project

##  Project Overview
This project implements a statistical engine from scratch using pure Python (without external libraries like NumPy or Pandas). It processes raw numerical data and computes key statistical measures such as mean, median, mode, variance, standard deviation, and outliers.

Additionally, the project includes a Monte Carlo simulation to demonstrate the Law of Large Numbers (LLN) by simulating a server failure scenario with a fixed probability.



##  Mathematical Logic

### Mean
Mean = (Σx) / n

Where:
- Σx = sum of all data points  
- n = number of data points  



### Median (Even vs Odd)

- If the number of values is **odd**:
  Median = middle value after sorting  

- If the number of values is **even**:
  Median = (x₁ + x₂) / 2  
  (average of the two middle values)



### Mode

- The mode is the most frequent value(s)
- If multiple values have the same highest frequency → multimodal
- If all values appear once → no mode



### Variance

- Population Variance:
  Var = Σ(x - μ)² / n

- Sample Variance (Bessel’s Correction):
  Var = Σ(x - μ)² / (n - 1)

Where:
- x = data value  
- μ = mean  
- n = number of data points  


### Standard Deviation

Standard Deviation = √Variance

It measures how far values are from the mean.



### Outlier Detection (Z-Score Method)

Z = (x - μ) / σ

A value is considered an outlier if:

|Z| > threshold (default = 2)


### Law of Large Numbers (LLN)

As the number of trials increases, the experimental probability approaches the true probability.

In this project:
- True crash probability = 0.045  
- Larger simulations produce more accurate results  



##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/statistical_engine.git
cd statistical_engine
Run the Project using: python main.py
Run all tests using: python -m unittest discover tests

