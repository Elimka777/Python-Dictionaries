import copy

# Given sales data
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

# Create a deep copy of the weekly_sales dictionary
copied_sales = copy.deepcopy(weekly_sales)

# Update the sales figure for "Electronics" in "Week 2" to 18000 in the copied data
copied_sales["Week 2"]["Electronics"] = 18000

# Display the original and copied sales data to show the update
print("Original Sales Data:")
print(weekly_sales)
print()

print("Copied Sales Data with Updated 'Electronics' in 'Week 2':")
print(copied_sales)
