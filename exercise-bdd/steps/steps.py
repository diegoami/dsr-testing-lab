from behave import *
from coffee_machine import *

@given('the coffee machine is installed')
def step_impl(context):
    context.coffee_machine = CoffeeMachine()

@given('the coffee machine has 10 coffees')
def step_impl(context):
    context.coffee_machine.coffees = 10

@given('1 euro has been deposited')
def step_impl(context):
    context.coffee_machine.deposit_money(1)

@when('the coffee button is pressed')
def step_impl(context):
    context.coffee_machine.press_coffee_button()

@then('coffee should be served')
def step_impl(context):
  assert context.coffee_machine.served_drink is "coffee"
