# importing time to use at the end of the code, suspending the console window so it doesn't automatically close upon the execution of the function
import time

# creating a dictionairy to store each item with its price, more efficient than using loads of integers and strings, taking up variable names.
shopping_list = {'Apple':0.6,
                 'Bread':1.0,
                 'Chocolate':1.2,
                 'Cheese':2.1}

# this is where the magic happens
def finalPrice(shopping):

    # defining all of the variables here, the only one here that isn't going to be modified is fixed_vat which is a constant    

    totalprice = 0
    discount_amount = 0
    discount = 0
    fixed_vat = 0.2

    # iterating through the dictionairy and adding up the total price based on the values of each item (key).
    # the second for loop iterates and counts how many items are in the dictionary.
    
    for i in shopping.values():
        totalprice = totalprice + i   
    for n in shopping.keys():
        discount_amount = discount_amount + 1

    # this generates the discount rate given the amount of items being purchased. The boundaries are defined within the if/elif statements.
    
    if discount_amount >= 5 and discount_amount < 15:
        discount = 0.05
    elif discount_amount >= 15 and discount_amount < 30:
        discount = 0.1
    elif discount_amount >= 30:
        discount = 0.2

    # the totalprice is then modified to include the VAT and then the discount is applied, meaning the total price would be modified, unless there are 30+ items in the dictionary, then the discount cancels out the VAT

    totalprice = totalprice + (totalprice * fixed_vat)
    totalprice = totalprice - (totalprice * discount)

    # this just prints out all of the values. Ascii is used to make the end result look nice, other than that, it is just text modifying functions.

    print("Items______________________")
    for x in shopping.keys():
        print(x+": £"+str(shopping[x])+"0")
    print("\n" + "VAT: " + str(fixed_vat * 100) + "%")
    print("Discount: " + str(discount * 100) + "%")
    print("\n" + "Total Price: £"+ str(round(totalprice, 1))+"0")
    print("___________________________")

# calling the function here

finalPrice(shopping_list)

# making the console window sleep, so it doesn't close upon execution.

time.sleep(1000)
    
