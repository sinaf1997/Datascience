import random

def simulate_crashes(days: int) -> float:
    if days <= 0:
        raise ValueError("Number of days must be a positive integer.")
    crashes = sum(1 for _ in range(days) if random.random() < 0.045)
    return crashes / days