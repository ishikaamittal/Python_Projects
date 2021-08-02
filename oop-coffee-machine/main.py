import coffee_maker
import menu
import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = money_machine.MoneyMachine()
coffee_maker = coffee_maker.CoffeeMaker()
menu = menu.Menu()

machine_working = True
while machine_working:
    options = menu.get_items()
    order = (input(f"What will you like to have  {options} ?"))
    if order == "off":
        machine_working = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        find_drink = menu.find_drink(order)
        resources = coffee_maker.is_resource_sufficient(find_drink)
        do_payment = money_machine.make_payment(find_drink.cost)
        if resources and do_payment:
            coffee_ready = coffee_maker.make_coffee(find_drink)