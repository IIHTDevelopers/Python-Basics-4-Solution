import pandas as pd

#  Initial blood bank data
blood_groups = ["A+", "B+", "O-", "AB-"]
units_available = [10, 8, 4, 3]
blood_df = pd.DataFrame({
    "Blood Group": blood_groups,
    "Units Available": units_available
})



#  Function 2: Get total blood units
def total_units(df):
    return df["Units Available"].sum()

#  Function 3: Find groups with units below threshold
def low_stock_groups(df, threshold=5):
    return df[df["Units Available"] < threshold]

if __name__ == "__main__":
  
    # Total units
    total = total_units(blood_df)
    print("Total Units:", total)

    # Blood groups in low supply
    low_stock = low_stock_groups(blood_df, threshold=5)
    print("\nBlood Groups with Low Stock:")
    print(low_stock)
