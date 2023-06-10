class Banking_Management_System:
    def __init__(self):
        self.clients = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_permission_off = 0

    def create_account(self, unique_id):
        if unique_id in self.clients:
            print("This account already exists.")
        else:
            self.clients[unique_id] = {'balance': 0, 'transaction_history': []}
            print("New Account created successfully.")

    def deposit(self, unique_id, amount):
        if unique_id in self.clients:
            self.clients[unique_id]['balance'] += amount
            self.total_balance += amount
            self.clients[unique_id]['transaction_history'].append(f"Deposited: {amount}")
            print("Deposit money successfully.")
        else:
            print("This account does not exist.")

    def withdraw(self, unique_id, amount):
        if unique_id in self.clients:
            if self.clients[unique_id]['balance'] >= amount:
                self.clients[unique_id]['balance'] -= amount
                self.total_balance -= amount
                self.clients[unique_id]['transaction_history'].append(f"Withdrawn: {amount}")
                print("Withdrawal successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("This account does not exist.")

    def check_balance(self, unique_id):
        if unique_id in self.clients:
            balance = self.clients[unique_id]['balance']
            print(f"Available balance: {balance}")
        else:
            print("this account does not exist.")

    def transfer_amount(self, sender_id, receiver_id, amount):
        if sender_id in self.clients and receiver_id in self.clients:
            sender_balance = self.clients[sender_id]['balance']
            if sender_balance >= amount:
                self.clients[sender_id]['balance'] -= amount
                self.clients[receiver_id]['balance'] += amount
                self.clients[sender_id]['transaction_history'].append(f"Transferred: {amount} to {receiver_id}")
                self.clients[receiver_id]['transaction_history'].append(f"Received: {amount} from {sender_id}")
                print("Transfer successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Receiver accounts do not exist.")

    def check_transaction_history(self, unique_id):
        if unique_id in self.clients:
            print('\n')
            print("Transaction history:")
            print('\n')
            history = self.clients[unique_id]['transaction_history']
            for transaction in history:
                print(transaction)
        else:
            print("this account does not exist.")

    def take_loan(self, unique_id):
        if unique_id in self.clients:
            print('\n')
            print('Loan:')
            balance = self.clients[unique_id]['balance']
            if self.loan_permission_off == False:
                loan_amount = 2 * balance
                self.clients[unique_id]['balance'] += loan_amount
                self.total_loan_amount += loan_amount
                self.clients[unique_id]['transaction_history'].append(f"Loan taken: {loan_amount}")
                print("Loan Permitted.")
            else:
                print("Loan permission is currently off Now.")
       

    def admin_check_total_balance_of_bank(self):
        print(f"Total available balance in the bank: {self.total_balance}")

    def admin_check_total_loan_amount_of_clients(self):
        print(f"Total loan amount in the bank: {self.total_loan_amount}")

    def admin_on_loan_feature(self):
        self.loan_feature_on = True
        print("Loan feature is on.")

    def admin_off_loan_feature(self):
        if self.loan_feature_on:
            self.loan_feature_on = False
            print("Loan feature is off.")



Banking_Mechanism = Banking_Management_System()

print('\n')
print('For clients:')
print('\n')
Banking_Mechanism.create_account("client1")
Banking_Mechanism.deposit("client1", 500000)
Banking_Mechanism.withdraw("client1", 20000)
Banking_Mechanism.check_transaction_history("client1")
Banking_Mechanism.check_balance("client1")
Banking_Mechanism.transfer_amount("client1", "client2", 3000)
Banking_Mechanism.take_loan("client1")



print('\n')
print('For Admin:')
print('\n')

Banking_Mechanism.create_account("client2")
Banking_Mechanism.admin_check_total_balance_of_bank()
Banking_Mechanism.admin_check_total_loan_amount_of_clients()
Banking_Mechanism.admin_on_loan_feature()
Banking_Mechanism.admin_off_loan_feature()

print('\n')
print('After opening client2 account :')
print('\n')
Banking_Mechanism.transfer_amount("client1", "client2", 3000)