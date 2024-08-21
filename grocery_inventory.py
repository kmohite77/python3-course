import json

inventory = {"Apples": {"Price": 1.50, "Stock": 10},
             "Bananas": {"Price": 1.00, "Stock": 12},
             "Eggs": {"Price": 3.00, "Stock": 7},
             "Milk": {"Price": 3.50, "Stock": 20},
             "Oranges": {"Price": 0.75, "Stock": 35},
             "Avocados": {"Price": 2.50, "Stock": 5}
            }
print(inventory['Avocados']['Price'])
print(inventory['Milk']['Stock'])

inventory.update({"Celery": {"Price":1.25, "Stock":15}})
print(inventory)


inventory_updated = json.dumps(inventory, indent=4)
print(inventory_updated)


def process_shopping_list(inventory, groceryList=["Apples", "Eggs", "Milk", "Avocados", "Broccoli", "Celery", "Cherries"]):
    Total_cost = 0
    for key in inventory.keys():
        if key in groceryList:
            #print(key, "is/are available")
            #print(inventory[key]['Stock'])
            print(inventory[key]['Stock'],"no of ", key, "is/are available")
            price_item = inventory[key]['Stock'] * inventory[key]['Price']
            print("cost of",key,"is",price_item)
            print("\n")
            Total_cost = Total_cost + price_item 
        else:
            print(key, "is/are not available")
            print("\n")
     
    print("Total cost of available items is", Total_cost)

process_shopping_list(inventory, groceryList=["Apples", "Eggs", "Milk", "Avocados", "Broccoli", "Celery", "Cherries"])    