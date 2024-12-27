class Payment:
    def __init__(self, recipient, amount):
        self.recipient = recipient 
        self.amount = amount
    def check_balance(self, initial):
        return initial - self.amount
        
payment1 = Payment("A", 25) 
payment2= Payment("B", 50) 
print(payment1.recipient)
print(payment1.check_balance(500))
