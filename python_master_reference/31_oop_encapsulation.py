"""
31 - OOP: Encapsulation
Encapsulation means controlling access to data inside a class.
"""

# Create a class called BankAccount.
class BankAccount:

    # This method runs automatically when we create a new BankAccount object.
    def __init__(self, owner, balance):

        # Store the account owner's name.
        self.owner = owner

        # Store the balance as a private-like attribute.
        # The double underscore means we should not access it directly from outside the class.
        self.__balance = balance

    # Create a method to deposit money into the account.
    def deposit(self, amount):

        # Only allow deposit if the amount is greater than 0.
        if amount > 0:

            # Add the deposit amount to the balance.
            self.__balance += amount

            print(f"Deposited {amount}")

    # Create a method to safely read the balance.
    def get_balance(self):

        # Return the current balance.
        return self.__balance


# Create a BankAccount object for Khadir with starting balance 100.
account = BankAccount("Khadir", 1000000)

# Deposit 50 into the account.
account.deposit(50)

# Print the current balance using the get_balance method.
print(account.get_balance())

# This would cause an error because __balance is private-like.
# print(account.__balance)
