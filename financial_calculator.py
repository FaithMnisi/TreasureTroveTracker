import math

while True:
    # Show the user the menu
    print("Welcome to the Treasure Trove Tracker\n")
    print("Investment - to calculate the amount of interest you'll earn on your investment")
    print("Bond - to calculate the amount you'll have to pay on a home loan")
    print("Exit - to exit the program")

    # Request user to choose between investment, bond, or exit
    choice = input("Enter either 'bond', 'investment', or 'exit' to proceed: ")

    # Check if the user wants to exit the program
    if choice.lower() == 'exit':
        print("Goodbye!")
        break

    # Display an error message if the user doesn't enter 'bond', 'investment', or 'exit'
    if choice.lower() not in ['bond', 'investment']:
        print("Invalid choice. Please enter either 'bond', 'investment', or 'exit'.")
        continue

    # If user chooses 'investment'
    if choice.lower() == "investment":
        attempts = 0

        while attempts < 3:
            # Request user to choose between simple and compound interest
            interest = input("\nEnter either 'simple' or 'compound' interest: ")

            # Request principal amount, interest rate, and number of years
            if interest.lower() == "simple":
                principal_amount = float(input("Enter the investment amount: "))
                interest_rate = float(input("Enter the interest rate as a percentage (e.g. 8): ")) / 100
                years = int(input("How many years do you want to invest? "))

                # Calculate simple interest
                simple_interest = principal_amount * (1 + interest_rate * years)
                print(f"\nThe total investment amount after {years} years will be R{simple_interest:.2f}")
                break

            # Request principal amount, interest rate, and number of investment years
            elif interest.lower() == "compound":
                principal_amount = float(input("Enter the investment amount: "))
                interest_rate = float(input("Enter the interest rate as a percentage (e.g. 8): ")) / 100
                years = int(input("How many years do you want to invest? "))

                # Calculate compound interest
                compound_interest = principal_amount * math.pow((1 + interest_rate), years)
                print(f"\nThe total investment amount after {years} years will be R{compound_interest:.2f}")
                break

            # Display error message if user doesn't choose simple or compound interest
            else:
                print("Invalid choice. Please enter either 'simple' or 'compound'.")
                attempts += 1

        # Exit program if user enters wrong investment type three times
        if attempts == 3:
            print("Maximum number of attempts reached. Exiting")
            break

    # If user chooses bond
    elif choice.lower() == "bond":
        value = float(input("Enter the present value of your house: "))
        monthly_rate = int(input("Enter the interest rate: ")) / 100 / 12
        repayment_months = int(input("How long will it take you to repay the loan (in months)? "))

        # Calculate how much the user has to repay each month
        bond_repayment = (monthly_rate * value) / (1 - (1 + monthly_rate) ** -repayment_months)
        print(f"\nYour monthly repayment rate will be R{bond_repayment:.2f} per month for {repayment_months} months")

    # Prompt user to go back to the menu or exit
    response = input("Enter 'menu' to return to the menu or 'exit' to exit the program: ")
    if response.lower() == 'exit':
        print("Farewell, financial voyager!")
        break
