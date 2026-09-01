# Task 5: Abstraction (Using Abstract Base Class)
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ${amount}")

# Test all classes
cc = CreditCardPayment()
cc.process_payment(250)

upi = UPIPayment()
upi.process_payment(50)
