# Task 5

import math

print ("investment - to calculate the amount of interest you'll earn on your investment.")
print("bond - to calculate the amount you'll have to pay on a home loan.\n")

investment_bond = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

if investment_bond.lower() == ("investment"):  #This simple line took me a while to figure out. \n
    # My initial code was long & messy.

    deposit = int(input("Please enter the amount being deposited: £"))
    interest_amount = int(input("Please enter you interest rate (%): "))/100
    investment_duration = int(input("Please enter the duration of the investment (in years): "))
    interest = input("Please enter the desired interest plan [Simple, Compound]: ")

    total_interest_simple = deposit * (1 + interest_amount * investment_duration)  # A = P *(1 + r*t)
    total_interest_compound = deposit * math.pow((1 + interest_amount),investment_duration)  # A = P * math.pow((1+r),t)

    if interest.lower() == ("simple"):
        print(f"\nThe calculated value under the 'Simple' plan is £{total_interest_simple}")
    elif interest.lower() == ("compound"):
        print(f"\nThe calculated value under the 'Compound' plan is £{total_interest_compound}")
    else:
        print("\nYou have printed an invalid entry.")

elif investment_bond.lower() == ("bond"):

    house_value = int(input("What is the present house value: £"))
    interest_amount = int(input("Please enter you interest rate (%): ")) / 100
    interest_amount_monthly = interest_amount / 12 # This should provide an accurate monthly interest.
    investment_length = int(input("How long will it take to repay the loan (in months): "))

    # bond formula = (i * P)/(1 - (1 + i)**(-n))
    bond_repayment = (interest_amount_monthly * house_value) / (1 - (1 + interest_amount_monthly) ** (-investment_length))
    print(f"You are required to pay £{bond_repayment} each month to pay off the investment")

else:
    print ("You have inputted an incorrect value.")
