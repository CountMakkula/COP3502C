from base_classes import *
#Secure account class
class SecureAccount(Account):
    def __init__(self, password):
        super().__init__()
        self.password = password

    def get_balance(self, password):
        if password != self.password:
            print("Incorrect password")
        else:
            return super().get_balance()

    def deposit(self, amount, password):
        if password != self.password:
            print("Incorrect password")
        else:
            return super().deposit(amount)

    def withdraw(self, amount, password):
        if password != self.password:
            print("Incorrect password")
        else:
            return super().withdraw(amount)

#Memory calculator class
class MemoryCalculator(Calculator):
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        if x == "RESULT":
            x = self.result
        elif y == "RESULT":
            y = self.result
        self.result = super().add(x, y)
        return self.result

    def sub(self, x, y):
        if x == "RESULT":
            x = self.result
        elif y == "RESULT":
            y = self.result
        self.result = super().sub(x, y)
        return self.result

#Fractions class
class ImprovedFraction(Fraction):
    def add(self, other):
        if other // 1 == other:
            N = ImprovedFraction(other, 1)
            return super().add(N)
        else:
            return super().add(other)

    def multiply(self, other):
        if other // 1 == other:
            N = ImprovedFraction(other, 1)
            return super().multiply(N)
        else:
            return super().multiply(other)
        return self

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __str__(self):
        return f"{self.num}/{self.den}"