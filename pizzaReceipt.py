def generateReceipt(pizzaOrder):
        sum = 0 #sum before calculating tax and receipt total.
        pizzaCounter = 1

        #a list of tuples with the base price and any additional charges associated with each size of pizza.
        PRICING = [('S', 7.99, 0.50 ), ('M', 9.99, 0.75), ('L', 11.99, 1.00), ('XL', 13.99, 1.25)]
        #Using the PRICING list, determine the appropriate base and extra costs.

        if not pizzaOrder:
                print("You did not order anything")

        else:
                print("Your order: ")
                for pizza in pizzaOrder:
                        baseCost, addCost = 0, 0
                        size, toppings = pizza[0],pizza[1]
                        numToppings = len(toppings)
                        toppingsCount = len(toppings)
        
                        if size == 'S':
                                baseCost = PRICING[0][1]
                                while toppingsCount > 3:
                                        addCost += PRICING[0][2]
                                        cost = PRICING[0][2]
                                        toppingsCount -= 1
                                        #while statement adds the total cost if the toppings are more than 3 to the variable addCost and then we subtract 1 from toppingsCount.
                                        
                        elif size == 'M':
                                baseCost = PRICING[1][1]
                                while toppingsCount > 3:
                                        addCost += PRICING[1][2]
                                        cost = PRICING[1][2]
                                        toppingsCount -= 1
                        elif size == 'L':
                                baseCost = PRICING[2][1]
                                while toppingsCount > 3:
                                        addCost += PRICING[2][2]
                                        cost = PRICING[2][2]
                                        toppingsCount -= 1
                        elif size == 'XL':
                                baseCost = PRICING[3][1]
                                while toppingsCount > 3:
                                        addCost = addCost + PRICING[3][2]
                                        cost = PRICING[3][2]
                                        toppingsCount -= 1

                        sum = float(sum + baseCost + addCost) #sum now has the value of basecost and addcost. We add tax to sum for the total value.

                        print("Pizza {}: {} 				  {:.2f}".format(pizzaCounter, size, baseCost))

                        for top in toppings:
                                print("- {}".format(top))

                        while numToppings > 3:
                                print("Extra Topping ({})		   {:.2f}".format(size, cost))
                                numToppings -= 1

                        pizzaCounter += 1

                print("Tax:					   {:.2f}".format(sum * 0.13))
                print("Total:					  {:.2f}".format(float(sum + (sum * 0.13))))

