# This script will allow a investor to determine their 
# portfolio's Alpha using the investment formula for calcuating Alpha

def calc_alpha(pr_input, rf_rate, beta, market_return):
    try:
        pr_float = float(pr_input) # How much a portfolio has grown or shrunk relative to the initial investment. 
        rf_float = float(rf_rate) # Rate of return on an investment that has zero risk
        beta_float = float(beta) # Volatility or systematic risk, of a security or portfolio compared to the market
        market_return_float = float(market_return) # total of all profit or loss on an investment over a period of time
    except ValueError:
        print("That's not a valid number")
        return None

    alpha = (pr_float - rf_float) - (beta_float * (market_return_float - rf_float))
    return alpha

# Formula usage
pr_input = input("Enter Portfolio Return Percentage: ")
rf_rate = input("Enter The Risk Free Rate: ")
beta = input("Enter the Portfolio Beta from 0.1 to 1.0: ")
market_return = input("Enter the Portfolio Market Return: ")

alpha = calc_alpha(pr_input, rf_rate, beta, market_return)
if alpha is not None:
    print(f"The portfolio's Alpha is: {alpha:.2f}")


