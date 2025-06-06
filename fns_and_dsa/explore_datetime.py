from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and displays the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    """
    current_date = datetime.now()
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_date}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date,
    and displays it in "YYYY-MM-DD" format.
    """
    while True:
        try:
            num_days_str = input("Enter the number of days to add to the current date: ")
            num_days = int(num_days_str)
            break # Exit loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    current_date = datetime.now()
    future_date = current_date + timedelta(days=num_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()