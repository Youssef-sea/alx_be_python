import sys
from bank_account import BankAccount

def main():
    # Start with an initial balance for testing purposes.
    # In a real application, this might be loaded from a database or user input.
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands:")
        print("  deposit:<amount> - Deposits the specified amount.")
        print("  withdraw:<amount> - Withdraws the specified amount.")
        print("  display - Displays the current balance.")
        sys.exit(1)

    command_parts = sys.argv[1].split(':', 1) # Split only on the first colon
    command = command_parts[0].lower()
    amount = None

    if len(command_parts) > 1:
        try:
            amount = float(command_parts[1])
        except ValueError:
            print(f"Error: Invalid amount '{command_parts[1]}'. Amount must be a number.")
            sys.exit(1)

    if command == "deposit":
        if amount is not None:
            try:
                account.deposit(amount)
                print(f"Deposited: ${amount:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Error: Deposit command requires an amount. Usage: deposit:<amount>")
    elif command == "withdraw":
        if amount is not None:
            try:
                if account.withdraw(amount):
                    print(f"Withdrew: ${amount:.2f}")
                else:
                    print("Insufficient funds.")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Error: Withdraw command requires an amount. Usage: withdraw:<amount>")
    elif command == "display":
        account.display_balance()
    else:
        print(f"Invalid command: '{sys.argv[1]}'.")
        print("Commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()