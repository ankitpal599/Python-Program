class Cash:
    def pay(self):
        print("Payment made using Cash")
class Card:
    def pay(self):
        print("Payment made using Card")
class UPI:
    def pay(self):
        print("Payment made using UPI")
def make_payment(method):
    method.pay()
cash = Cash()
card = Card()
upi = UPI()
make_payment(cash)
make_payment(card)
make_payment(upi)
