from threading import Lock

class BankAccount(object):
    def __init__(self):
        self.balance = None
        self.lock = Lock()

    def get_balance(self):
        if self.balance is None:
            raise ValueError("Closed account")
        return self.balance

    def open(self):
        self.balance = 0

    def deposit(self, amount):
        try:
            self.lock.acquire()
            if self.balance is None:
                raise ValueError("Closed account")
            if amount <= 0:
                raise ValueError("Invalid deposit amount")
            self.balance += amount
        finally:
            self.lock.release()

    def withdraw(self, amount):
        try:
            self.lock.acquire()
            print(self.balance)
            if self.balance is None:
                raise ValueError("Closed account")
            if amount <= 0:
                raise ValueError("Invalid withdraw amount")
            if amount > self.balance:
                raise ValueError("Insufficent balance")
            self.balance -= amount
        finally:
            self.lock.release()

    def close(self):
        self.balance = None
