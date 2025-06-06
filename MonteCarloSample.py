# Here is a Python example of a Monte Carlo simulation for forecasting the future value 
# of an investment portfolio. The example assumes annual returns follow a normal 
# distribution, and we simulate multiple paths of portfolio growth over a specified 
# period. Generated from ChatGPT.

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define parameters for the simulation
initial_investment = 100000  # Initial portfolio value
annual_return = 0.08         # Expected annual return (8%)
annual_volatility = 0.15     # Annual volatility (15%)
years = 20                   # Investment horizon (20 years)
simulations = 10000          # Number of simulations

# Explanation: 
# These parameters set up the initial investment, expected return, 
# risk (volatility), time horizon, and the number of simulations.

# Step 2: Generate random returns for each simulation
np.random.seed(42)  # Seed for reproducibility
simulated_paths = np.zeros((simulations, years + 1))  # Empty array for results
simulated_paths[:, 0] = initial_investment  # Set initial investment for all paths

# Explanation:
# `np.zeros` creates a 2D array to store the portfolio value for each year of every simulation. 
# The first column is the starting value of the portfolio.

for i in range(simulations):
    for t in range(1, years + 1):
        random_return = np.random.normal(annual_return, annual_volatility)
        simulated_paths[i, t] = simulated_paths[i, t - 1] * (1 + random_return)

# Explanation:
# This double-loop simulates the portfolio value year by year.
# For each year (`t`), the portfolio value is updated by applying a random return 
# sampled from a normal distribution defined by the expected return and volatility.

# Step 3: Analyze results
ending_values = simulated_paths[:, -1]  # Get the portfolio value at the end of 20 years
mean_ending_value = np.mean(ending_values)
percentile_5 = np.percentile(ending_values, 5)
percentile_95 = np.percentile(ending_values, 95)

# Explanation:
# At the end of the simulation, we extract the final portfolio values for each simulation.
# We calculate the mean, 5th percentile, and 95th percentile for risk analysis.

# Step 4: Visualization
plt.figure(figsize=(10, 6))
plt.plot(simulated_paths.T, color='lightblue', alpha=0.1)  # Plot all simulation paths
plt.title("Monte Carlo Simulation of Portfolio Value Over 20 Years")
plt.xlabel("Years")
plt.ylabel("Portfolio Value")
plt.axhline(mean_ending_value, color='red', linestyle='--', label=f'Mean: ${mean_ending_value:,.2f}')
plt.axhline(percentile_5, color='orange', linestyle='--', label=f'5th Percentile: ${percentile_5:,.2f}')
plt.axhline(percentile_95, color='green', linestyle='--', label=f'95th Percentile: ${percentile_95:,.2f}')
plt.legend()
plt.show()

# Explanation:
# This visualization shows the range of possible portfolio growth paths.
# Key metrics like mean and percentile lines help investors understand potential outcomes.
