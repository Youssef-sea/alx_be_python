# User Input for Financial Details

## monthly income
user_monthly_income = input("Enter your monthly income:")

## monthly expenses
user_monthly_expenses = input("Enter your monthly expenses:")

## convert the input
monthly_income = int(user_monthly_income)
monthly_expenses = int(user_monthly_expenses)

# Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings
annual_interest_rate = 0.05  # 5% as a decimal
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Display the user’s monthly savings
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
