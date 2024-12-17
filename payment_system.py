class Account(object):
	"""docstring for Account"""
	def __init__(self, account_name, balance):

		self.account_name = account_name

		self.balance = balance

	def deposit(self, amount):

		self.balance += amount

	def withdraw(self, amount):
		
		if amount > self.balance:

			return False

		self.balance -= amount
		

class Payment(object):
	"""docstring for Payment"""
	def __init__(self):

		self.accounts = {}

	def create_account(self):

		print("\n ---Create New Account---")

		account_name = input("Enter account name: ")

		deposit = float(input("Enter initial deposit amount: "))

		if account_name in self.accounts:

			print(f"Account {account_name} already exists")

		else:

			new_account = Account(account_name, deposit)

			self.accounts[account_name] = new_account

			print(f"Account '{account_name}' created successfully with balance: ${deposit:.2f}")

	def make_payments(self):

		print("\n ---Make a Payment---")

		from_account = input("Enter sender's account name: ")

		to_account = input("Enter receiver's account name: ")

		amount = float(input("Enter payment amount: "))

		if from_account not in self.accounts or to_account not in self.accounts:

			print("One or both accounts do not exist.")

			return

		if self.accounts[from_account].withdraw(amount):

			self.accounts[to_account].deposit(amount)

			print(f"Payment of ${amount:.2f} made from {from_account} to {to_account}.")

		else:

			print(f"Insuffiecient balance in {from_account} account.")

	def account_balance(self):

		print("\n ---Make a Payment---")

		account_name = input("Enter account name: ")

		if account_name in self.accounts:

			balance = self.accounts[account_name].balance

			print(f"The balance for {account_name} is: ${balance:.2f}")

		else:

			print("Account does not exist.")

	def menu(self):

		while True:

			print("\n --- Payment System ---")

			print("1. Create an account")

			print("2. Make a payment")

			print("3. Check Account Balance")

			print("4. Exit")

			choice = int(input("Enter Your Choice (1-4): "))

			if choice == 1:

				self.create_account()

			elif choice == 2:

				self.make_payments()

			elif choice == 3:

				self.account_balance()

			elif choice == 4:

				print("\n Thank you for using payment system.")

				break

			else:
				print("\n Invalid choice try again.")


if __name__ == "__main__":

	payment = Payment()

	payment.menu()
		