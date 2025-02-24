#blood_bank_management.py

import numpy as np
import pandas as pd

# Function 1: Get Blood Bank Data
def get_blood_bank_data():
    """
    Returns a DataFrame containing blood groups and units available.

    Returns:
        pandas.DataFrame: Blood group inventory.
    """
    blood_groups = np.array(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    units_available = np.array([10, 5, 8, 4, 15, 7, 6, 3])
    return pd.DataFrame({"Blood Group": blood_groups, "Units Available": units_available})

# Function 2: Add New Blood Group
def add_new_blood_group(blood_bank, blood_group, units):
    """
    Adds a new blood group and its units to the inventory.

    Args:
        blood_bank (pandas.DataFrame): DataFrame containing current blood bank inventory.
        blood_group (str): Blood group to be added.
        units (int): Initial units for the new blood group.

    Returns:
        pandas.DataFrame: Updated blood bank inventory.
    """
    new_entry = pd.DataFrame({"Blood Group": [blood_group], "Units Available": [units]})
    updated_blood_bank = pd.concat([blood_bank, new_entry], ignore_index=True)
    return updated_blood_bank


# Function 3: Get Total Units
def get_total_units(blood_bank):
    """
    Calculates the total number of blood units available.

    Args:
        blood_bank (pandas.DataFrame): DataFrame containing current blood bank inventory.

    Returns:
        int: Total number of units available.
    """
    total_units = blood_bank["Units Available"].sum()
    return total_units

# Function 4: Find Scarcity
def find_scarcity(blood_bank, threshold=5):
    """
    Identifies blood groups that are below a specified threshold.

    Args:
        blood_bank (pandas.DataFrame): DataFrame containing current blood bank inventory.
        threshold (int): The unit threshold to check for scarcity.

    Returns:
        pandas.DataFrame: Blood groups that are below the threshold.
    """
    scarcity = blood_bank[blood_bank["Units Available"] < threshold]
    return scarcity

# Main Execution
def main():
    """
    Main function to demonstrate blood bank functionalities.
    """
    blood_bank = get_blood_bank_data()

    # Adding a new blood group
    print("\n--- Adding New Blood Group ---")
    blood_bank = add_new_blood_group(blood_bank, "P+", 10)
    print(blood_bank)



    # Get total units
    print("\n--- Total Units Available ---")
    total_units = get_total_units(blood_bank)
    print("Total Units:", total_units)

    # Find scarcity
    print("\n--- Blood Groups in Scarcity ---")
    scarcity = find_scarcity(blood_bank, threshold=5)
    print(scarcity)

if __name__ == "__main__":
    main()
