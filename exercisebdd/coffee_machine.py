class CoffeeMachine:

    coffees = 0
    """Number of coffees in the machine."""

    deposited_money = 0
    """The money desposited by a customer. Can be used for buying coffee."""

    returned_money = 0
    """Money returned to the customer."""

    banked_money = 0
    """Money in the machine after it has been used to buy a coffee. Not usable by customer for buying coffee."""

    served_drink = ""
    """The last drink dispensed by the machine."""

    error_message = ""
    """The error message currently displayed by the machine."""

    def __init__(self):
        return

    def press_coffee_button(self):
        if self.coffees < 1:
            self.error_message = "No coffee, sorry."
            self.returned_money = self.deposited_money
            self.deposited_money = 0
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

    def take_drink(self):
        drink = self.served_drink
        self.served_drink = ""
        return drink

    def return_money(self, money):
        self.deposited_money -= money
        self.returned_money  += money

