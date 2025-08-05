def read_food_items(file_path):
    """
    Reads food items and their type (Veg/Non-Veg) from a file.

    File format:
    Each line must be in the format: ItemName,Type
    Example:
        Pizza,Veg
        Chicken Wings,Non-Veg

    Args:
        file_path (str): Path to the file.

    Returns:
        list of tuples: [(item_name, item_type), ...]
    """
    food_items = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    item, type_ = parts[0].strip(), parts[1].strip()
                    food_items.append((item, type_))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return food_items

def classify_food_items(food_items):
    """
    Classifies food items into Veg and Non-Veg lists.

    Args:
        food_items (list): List of tuples (item_name, item_type)

    Returns:
        dict: {'Veg': [...], 'Non-Veg': [...]}
    """
    classification = {'Veg': [], 'Non-Veg': []}
    for item, type_ in food_items:
        if type_ == 'Veg':
            classification['Veg'].append(item)
        elif type_ == 'Non-Veg':
            classification['Non-Veg'].append(item)
    return classification

# ✅ Main Execution
if __name__ == "__main__":
    file_path = "food_items.txt"
    items = read_food_items(file_path)
    result = classify_food_items(items)

    print("\n--- Food Classification ---")
    print("Veg Items:", result['Veg'])
    print("Non-Veg Items:", result['Non-Veg'])
