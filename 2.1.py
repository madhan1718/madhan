class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self.__account_balance += amount
          print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
      else:
          print("Invalid deposit amount. Amount must be greater than zero.")

  def withdraw(self, amount):
      if 0 < amount <= self.__account_balance:
          self.__account_balance -= amount
          print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
      elif amount > self.__account_balance:
          print("Insufficient funds.")
      else:
          print("Invalid withdrawal amount. Amount must be greater than zero.")

  def display_balance(self):
      print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")


# Create an instance of BankAccount and test the functionalities
account = BankAccount("12345", "John Doe", 1000.0)

account.display_balance()  # Display initial balance
account.deposit(500.0)  # Deposit money
account.withdraw(200.0)  # Withdraw money
account.display_balance()  # Display updated balance
