class CoffeeMachine:

    coffees = 0
    """Number of coffees in the machine"""

    deposited_money = 0
    """The money desposited by a customer. Can be used for buying coffee."""

    returned_money = 0
    """Monkey returned to the customer"""

    banked_money = 0
    """Money in the machine after it has been used to buy a coffee. Not usable by customer for buying coffee."""

    served_drink = ""
    """The drink in the """

    error_message = ""

    def __init__(self):
        return

    def press_coffee_button(self):
        if self.deposited_money == 1:
            self.served_drink = "coffee"
            self.banked_money += 1
            self.deposited_money = 0
        elif self.deposited_money > 1:
            self.served_drink = "coffee"
            self.returned_money = self.deposited_money - 1
            self.banked_money += 1
            self.deposited_money = 0
        elif self.deposited_money < 1:
            self.error_message = "Coffee costs 1 euro, cheapskate"

    def deposit_money(self, money):
        self.deposited_money += money

    def press_refund_button(self):
        self.returned_money = self.deposited_money
