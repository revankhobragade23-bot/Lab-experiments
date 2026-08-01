# Payment Method

class CreditCard:
    def pay(self,amount):
        print("payment of $", amount, "successful using credit card")

class PayPal:
    def pay(self,amount):
        print("payment of $", amount, "successful using PayPal")

class UPI:
    def pay(self,amount):
        print("payment of $", amount, "successful using UPI")


# Payment Processor
            
class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.pay(amount)

# Main Program 
    
print("Select Payment Method:")
print("1. Credit Card") 
print("2. PayPal")
print("3. UPI")

choice = int(input("Enter choice: "))
amount = int(input("Enter amount: "))

if choice == 1:
    method = CreditCard()
elif choice == 2:
    method = PayPal()
elif choice == 3:
    method = UPI()
else:
    print("Invalid choice")
    exit()

processor = PaymentProcessor(method)
processor.process_payment(amount)        