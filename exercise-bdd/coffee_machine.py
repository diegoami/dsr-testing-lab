class CoffeeMachine:

    coffees = 0
    deposited_money = 0
    returned_money = 0
    served_drink = ""
    error_message = ""

    def __init__(self):
        return

    def press_coffee_button(self):
        if self.deposited_money == 1:
            self.served_drink = "coffee"
            self.deposited_money = 0
        elif self.deposited_money > 1:
            self.served_drink = "coffee"
            self.returned_money = self.deposited_money - 1
            self.deposited_money = 0
        elif self.deposited_money < 1:
            self.error_message = "Coffees cost 1 euro, cheapskate"

    def deposit_money(self, money):
        self.deposited_money += money
