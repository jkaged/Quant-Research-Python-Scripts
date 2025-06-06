# This script will allow a investor to determine their 
# Compound Annual Growth Rate (CAGR) using its formula
# The CAGR formula is: CAGR = (End Years Value/Beginning YearsValue) ^ (1/No. of years) - 1

def CAGR_Calc(EndVal, BeginVal, NumYears):
    try:
        EndVal = float(EndVal) # Investment value at end of investment years or periods
        BeginVal = float(BeginVal) # Investment value at beginning of investment years or periods
        NumYears = float(NumYears) # Number of years invested
    except ValueError:
        print("That's not a valid number")
        return None

    CAGR_Return = ((EndVal/BeginVal) ** (1/NumYears)) - 1
    return CAGR_Return

# Formula usage
EndVal = input("Enter The Investment Value at the End of Investment Period: ")
BeginVal = input("Enter the Investment Value at the Beginning of Investment Period: ")
NumYears = input("Enter the Number of Years the Investment was held: ")

CAGR_Return = CAGR_Calc(EndVal, BeginVal, NumYears)
if CAGR_Return is not None:
    print(f"The stock's CAGR is: {CAGR_Return:.2f}")