# Class to manage a checkbook balance
class Checkbook:
    def __init__(self):
        # Initialize balance to zero
        self.balance = 0.0

    # Method to deposit money into the checkbook
    def deposit(self, amount):
        try:
            # Attempt to convert input to float and add to balance
            amount = float(amount)
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            # Handle invalid input gracefully
            print("Invalid input. Please enter a valid numeric value.")

    # Method to withdraw money from the checkbook
    def withdraw(self, amount):
        try:
            # Attempt to convert input to float and check if enough balance
            amount = float(amount)
            if amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            # Handle invalid input gracefully
            print("Invalid input. Please enter a valid numeric value.")

    # Method to get the current balance
    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

# Main function to interact with the checkbook
def main():
    # Create an instance of the Checkbook class
    cb = Checkbook()
    while True:
        # Prompt user for action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        # Perform action based on user input
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = input("Enter the amount to deposit: $")
            # Call deposit method
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = input("Enter the amount to withdraw: $")
            # Call withdraw method
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            # Call get_balance method
            cb.get_balance()
        else:
            # Handle invalid command
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    # Call main function when script is executed
    main()
