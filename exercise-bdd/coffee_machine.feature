Feature: A coffee machine that dispenses coffee

  Scenario: run a simple test
     Given the coffee machine is installed
      and the coffee machine has coffee
      and I have deposited 1 euro
      when I press the coffee button
      then I should be served a coffee
