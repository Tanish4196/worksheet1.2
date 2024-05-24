principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in decimal): "))
time = float(input("Enter the time period in years: "))
periods = int(input("Enter the number of compounding periods per year: "))

compound_interest = principal * (1 + rate / periods) ** (periods * time)


print("The compound interest is:", compound_interest)