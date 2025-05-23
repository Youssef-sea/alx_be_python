# future_age_calculator.py

# Prompt the user to input their current age
current_age_str = input("How old are you? ")

# Convert the input string to an integer
current_age = int(current_age_str)

# Calculate how many years are between 2023 and 2050
# This value will be added to the current age.
years_difference = 2050 - 2023

# Calculate the user's age in 2050
future_age = current_age + years_difference

# Print the result in the specified format
print(f"In 2050, you will be {future_age} years old.")