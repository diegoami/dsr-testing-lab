from behave import *
from coffee_machine import *

@given('the coffee machine is installed')
def step_impl(context):
    context.coffee_machine = CoffeeMachine()

@given('the coffee machine has coffee')
def step_impl(context):
    context.coffee_machine.coffees = 10

@given('I have deposited 1 euro')
def step_impl(context):
    context.coffee_machine.deposit_money(1)

@when('I press the coffee button')
def step_impl(context):
    context.coffee_machine.press_coffee_button()

@then('I should be served a coffee')
def step_impl(context):
  assert context.coffee_machine.served_drink is "coffee"
