# Here is a Python example of a Black-Scholes simulation for pricing a European call or put option. 
# This simulation models the price of the option based on the Black-Scholes formula.
# include sensitivity analysis using the Greeks (Delta, Gamma, Vega, Theta, and Rho). 
# These metrics help assess how the option price changes with respect to various parameters.

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Step 1: Define parameters for the Black-Scholes model
spot_price = 100          # Current stock price (S)
strike_price = 110        # Strike price of the option (K)
time_to_maturity = 1      # Time to expiration in years (T)
risk_free_rate = 0.05     # Risk-free interest rate (r)
volatility = 0.2         # Annualized volatility of the stock (σ)
option_type = "call"      # Type of option: 'call' or 'put'

# Step 2: Define functions to calculate d1 and d2
def calculate_d1_d2(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return d1, d2

# Step 3: Black-Scholes pricing function
def black_scholes(S, K, T, r, sigma, option_type):
    d1, d2 = calculate_d1_d2(S, K, T, r, sigma)
    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    return price

# Step 4: Greeks calculation functions
def calculate_greeks(S, K, T, r, sigma, option_type):
    d1, d2 = calculate_d1_d2(S, K, T, r, sigma)
    delta = norm.cdf(d1) if option_type == "call" else norm.cdf(d1) - 1
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T) / 100  # Vega per 1% change in volatility
    theta_call = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T))
                  - r * K * np.exp(-r * T) * norm.cdf(d2)) / 365
    theta_put = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T))
                 + r * K * np.exp(-r * T) * norm.cdf(-d2)) / 365
    theta = theta_call if option_type == "call" else theta_put
    rho_call = K * T * np.exp(-r * T) * norm.cdf(d2) / 100
    rho_put = -K * T * np.exp(-r * T) * norm.cdf(-d2) / 100
    rho = rho_call if option_type == "call" else rho_put
    
    return {"Delta": delta, "Gamma": gamma, "Vega": vega, "Theta": theta, "Rho": rho}

# Step 5: Calculate and display the option price and Greeks
option_price = black_scholes(spot_price, strike_price, time_to_maturity, risk_free_rate, volatility, option_type)
greeks = calculate_greeks(spot_price, strike_price, time_to_maturity, risk_free_rate, volatility, option_type)

print(f"The price of the {option_type} option is: ${option_price:.2f}")
print("Greeks:")
for greek, value in greeks.items():
    print(f"  {greek}: {value:.4f}")

# Step 6: Visualization (Optional)
# Plot how Delta changes with the stock price
stock_prices = np.linspace(50, 150, 100)
deltas = [calculate_greeks(S, strike_price, time_to_maturity, risk_free_rate, volatility, option_type)["Delta"] for S in stock_prices]

plt.figure(figsize=(10, 6))
plt.plot(stock_prices, deltas, label="Delta")
plt.title("Delta vs Stock Price")
plt.xlabel("Stock Price")
plt.ylabel("Delta")
plt.axvline(spot_price, color='red', linestyle='--', label='Current Spot Price')
plt.legend()
plt.grid()
plt.show()
