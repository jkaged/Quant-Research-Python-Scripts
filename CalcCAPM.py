# This script will allow a investor to determine their 
# Capital Asset Pricing Model (CAPM) using its formula
# The CAPM formula is: Equity Cost = Risk Free Rate + Beta (Market Return - Risk Free Rate)

# Next, grab real time stock data to calculate, may need to use Django or Flask

def calc_CAPM(rf_rate, beta, mrkt_return):
    try:
        rf_float = float(rf_rate) # Risk Free Rate
        beta_float = float(beta) # Investment Beta
        mrkt_return_float = float(mrkt_return) # Expected Market Return
    except ValueError:
        print("That's not a valid number")
        return None

    CAPM_Return = rf_float + beta_float * (mrkt_return_float - rf_float)
    return CAPM_Return

# Formula usage
rf_rate = input("Enter The Risk Free Rate Percentage: ")
beta = input("Enter the stock's Beta from 0.1 to 2.0: ")
mrkt_return = input("Enter the stock's expected Market Return Percent: ")

CAPM_Return = calc_CAPM(rf_rate, beta, mrkt_return)
if CAPM_Return is not None:
    print(f"The stock's CAPM is: {CAPM_Return:.2f}")