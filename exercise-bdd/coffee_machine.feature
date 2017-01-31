Feature: A coffee machine that dispenses coffee

  Scenario: Buy a coffee
     Given the coffee machine is installed
      and the coffee machine has 10 coffees
      and 1 euro has been deposited
      when the coffee button is pressed
      then coffee should be served

  Scenario: Buy coffee with excess money
     Given the coffee machine is installed
      and the coffee machine has 10 coffees
      and 2 euros have been deposited
      when the coffee button is pressed
      then coffee should be served
      and 1 euro should be returned

  Scenario: Get refund from coffee machine
     Given the coffee machine is installed
      and 1 euro has been deposited
      when the refund button is pressed
      then 1 euro should be returned

  Scenario: Try to buy coffee when no coffees are left
     Given the coffee machine is installed
      and the coffee machine has 0 coffees
      and 1 euro has been deposited
      when the coffee button is pressed
      then no coffee should be served
      and an error message should be displayed
      and 1 euro should be returned

  Scenario: Try and get a refund when no money has been deposited
     Given the coffee machine is installed
      when the refund button is pressed
      then no money should be returned

  Scenario: Try to buy 2 coffees without removing one
     TODO
