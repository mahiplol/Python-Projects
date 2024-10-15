from genericpath import getsize
from pizzaReceipt import *

def orderList():
    
    def getSize():
    #to obtain the proper size input, use while loop.
        while True:
            sizeInput = input("Choose a size: S, M, L, XL: ").upper()
            if sizeInput in ("S", "M", "L", "XL"):
                break
        return str(sizeInput)

    TOPPING = ("ONION", "SPINACH", "HAM", "TOMATO", "BROCCOLI", "BACON", "GREEN PEPPER",
            "PINEAPPLE", "GROUND BEEF", "MUSHROOM", "HOT PEPPER", "CHICKEN", "OLIVE",
            "PEPPERONI", "SAUSAGE")

    customerOrder = []

    #converting the input to lower case to account for case sensitivity.
    orderInput = input("Do you want to order a pizza? ").lower()

    if orderInput in ("no", "q", ""):
        generateReceipt(customerOrder)
    
    elif orderInput in ('yes' or 'y'):

        while True:
            pizza = (getSize(), []) #tuple pizza containing the size of the pizza, and an empty list for toppings.

            #while loop to ask the user for their toppings
            while True:
                toppingInput = input('\nType in one of our toppings to add it to your pizza. '
                                    '\nTo see the list of toppings, enter "LIST". '
                                    'When you are done adding toppings, enter "X"').upper()
                if toppingInput.upper() == 'LIST':
                    print("\n('ONION', ", "'TOMATO', ", "'GREEN PEPPER', ", "'MUSHROOM', ", "'OLIVE', ", "'SPINACH', ",
                        "'BROCCOLI', \n","'PINEAPPLE', ", "'HOT PEPPER', ", "'PEPPERONI', ", "'HAM', ", "'BACON', ", "'GROUND BEEF', ", "'CHICKEN', \n",
                        "'SAUSAGE')")
           
                elif toppingInput in TOPPING:
                    pizza[1].append(toppingInput)
                    print("\nAdded",toppingInput,"to your pizza.")
                elif toppingInput == "X":
                    break
                else:
                    print("Invalid Topping")

            customerOrder.append(pizza)

            continueInput = input("Do you want to continue ordering? ").lower()
            if continueInput in ('no', 'q'):
                generateReceipt(customerOrder)
                quit()
print(orderList())
