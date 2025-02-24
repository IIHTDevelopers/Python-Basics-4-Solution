# student/food_delivery.py

def get_menu():
    """
    Returns the menu with item prices.
    """
    return {
            "Pizza": 8.50,  # $8.50
            "Burger": 5.00,  # $5.00
            "Pasta": 7.25,  # $7.25
            "Fries": 3.50,  # $3.50
            "Cola": 2.00  # $2.00
    }

def calculate_bill(orders, menu):
    """
    Calculates the total bill and provides an order summary.

    Args:
        orders (list): List of tuples containing item and quantity.
        menu (dict): Dictionary containing menu items and prices.

    Returns:
        tuple: Total bill and order summary.
    """
    total_bill = 0
    order_summary = []
    for item, qty in orders:
        cost = menu[item] * qty
        total_bill += cost
        order_summary.append(f"{item} x{qty} = ${cost:.2f}")
    return total_bill, order_summary

def save_order(order_summary, total_bill, filename="food_orders.txt"):
    """
    Saves the order summary and total bill to a file.

    Args:
        order_summary (list): List of strings summarizing the order.
        total_bill (float): Total bill amount.
        filename (str): Name of the file to save the order.

    Returns:
        str: Filename after successful save.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write("\n".join(order_summary) + f"\nTotal Bill: ${total_bill:.2f}\n\n")
    return filename

def main():
    """
    Main function to execute the order processing flow.
    """
    food_menu = get_menu()
    orders = [
        ("Pizza", 2),
        ("Burger", 1),
        ("Pasta", 3),
        ("Fries", 2),
        ("Cola", 2)
    ]
    total_bill, order_summary = calculate_bill(orders, food_menu)

    print("\n--- Order Summary ---")
    for order in order_summary:
        print(order)
    print(f"Total Bill: ${total_bill:.2f}")

    save_order(order_summary, total_bill)
    print("\nOrder details appended to 'food_orders.txt'.")

if __name__ == "__main__":
    main()
