import pandas as pd

employee_ids = [101, 102, 103, 104]
employee_names = ["Alice", "Bob", "Charlie", "Diana"]
leaves_taken = [5, 2, 8, 1]
leave_df = pd.DataFrame({
    "Employee ID": employee_ids,
    "Name": employee_names,
    "Leaves Taken": leaves_taken
})

def total_leaves_taken(df):
    return df["Leaves Taken"].sum()

def employees_exceeding_leaves(df, limit=5):
    return df[df["Leaves Taken"] > limit]

def average_leaves_taken(df):
    if len(df) == 0:
        return 0
    return df["Leaves Taken"].mean()

if __name__ == "__main__":
    print("Total Leaves Taken:", total_leaves_taken(leave_df))

    print("\nEmployees with Leaves > 5:")
    print(employees_exceeding_leaves(leave_df, limit=5))

    print("\nAverage Leaves Taken:", average_leaves_taken(leave_df))
