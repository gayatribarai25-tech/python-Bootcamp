# Manage store order and inventory
'''You have a Prices dictionary with 5 items and their prices
You have an out_of_stock set with 2 of the items (from the Prices dictionary)
You have an Order list, that has list of orders (list of items)
Loop through the Order list
for each order, if it is out of stock, print unavailable
else, keep a running total ( get the price from the Prices dictionary)
Print the final order value
'''
Store = {
    "rice":35,
    "potato":40,
    "salt":15,
    "juice":20,
    "biscuit":50
}

out_of_stock= {"juice","biscuit"}

order = ["rice","potato","salt","juice","biscuit"]
total = 0
for items in order:
        if items in out_of_stock:
            print(items, "is unavailable.")
        else:
            total+=Store[items]
print("Final order value:",total)
