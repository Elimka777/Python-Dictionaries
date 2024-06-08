restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Coke": 2.65, "Ginger Ale": 2.50}   # Add a new category called "Beverages" with at least two items
restaurant_menu["Main Course"]["Steak"] = 17.99     # Update the price of "Steak" to 17.99.
del restaurant_menu["Starters"]["Bruschetta"]   # Remove "Bruschetta" from "Starters"
print(restaurant_menu)