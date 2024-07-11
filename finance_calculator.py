# 

import math

def investment_calculator():
    P = float(input("Enter the amount of money you are depositing: "))
    r = float(input("Enter the interest rate (as a percentage): ")) / 100
    t = int(input("Enter the number of years you plan to invest for: "))
    interest = input("Do you want 'simple' or 'compound' interest? ").strip().lower()
    
    if interest == 'simple':
        A = P * (1 + r * t)
    elif interest == 'compound':
        A = P * math.pow((1 + r), t)
    else:
        print("Invalid input. Please choose either 'simple' or 'compound' interest.")
        return
    
    print(f"Your investment will grow to R{A:.2f} after {t} years with {interest} interest.")

def bond_calculator():
    P = float(input("Enter the present value of the house: "))
    i = float(input("Enter the interest rate (as a percentage): ")) / 100
    n = int(input("Enter the number of months until you pay off the bond : "))
    
    repayment = P * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)
    
    print(f"Your monthly bond repayment will be ${repayment:.2f}.")

def main():
    print("Welcome to the Finance Calculator!")
    print("Choose either 'investment' or 'bond' from the menu below to proceed:")
    
    while True:
        user_choice = input("Enter 'investment' or 'bond': ").strip().lower()
        
        if user_choice == 'investment':
            investment_calculator()
            break
        elif user_choice == 'bond':
            bond_calculator()
            break
        else:
            print("Invalid input. Please enter 'investment' or 'bond'.")

if __name__ == "__main__":
    main()
