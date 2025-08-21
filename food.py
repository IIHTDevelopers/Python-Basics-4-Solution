def read_food_sales(file_path):
    """
    Reads food items with sales data from a text file.
    Each line format: FoodName,Category,Sales
    Returns: List of tuples [(FoodName, Category, Sales), ...]
    """
    items = []
    with open(file_path, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3:
                items.append((parts[0].strip(), parts[1].strip(), int(parts[2].strip())))
    return items


def find_lowest_sales_item(items):
    """
    Finds the food item with the lowest sales.
    Input: [(FoodName, Category, Sales), ...]
    Returns: (FoodName, Sales)
    """
    if not items:
        return None
    lowest = min(items, key=lambda x: x[2])
    return (lowest[0], lowest[2])

