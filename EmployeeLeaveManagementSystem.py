# student/employee_leave_management.py

# Function 1: Get Employee Data
def get_employee_data():
    """
    Returns the employee data with leave balances.

    Returns:
        dict: Employee details including name and leave balance.
    """
    return {
        "E001": {"name": "John Doe", "leave_balance": 12},
        "E002": {"name": "Alice Smith", "leave_balance": 10},
        "E003": {"name": "Bob Johnson", "leave_balance": 8},
        "E004": {"name": "Emma Davis", "leave_balance": 15},
        "E005": {"name": "Michael Brown", "leave_balance": 5},
    }

# Function 2: Process Leave Requests
def process_leave_requests(employees, leave_requests):
    """
    Processes leave requests and updates employee leave balances.

    Args:
        employees (dict): Employee data with leave balances.
        leave_requests (list): List of tuples containing employee ID and requested leave days.

    Returns:
        list: Leave request summary messages.
    """
    leave_summary = []
    for emp_id, leave_days in leave_requests:
        if emp_id not in employees:
            leave_summary.append(f"Employee ID {emp_id} not found.")
        elif leave_days < 0:
            leave_summary.append(f"Invalid leave request for {employees[emp_id]['name']}. Negative days not allowed.")
        elif employees[emp_id]["leave_balance"] >= leave_days:
            employees[emp_id]["leave_balance"] -= leave_days
            leave_summary.append(
                f"{employees[emp_id]['name']} granted {leave_days} days leave. Remaining: {employees[emp_id]['leave_balance']} days"
            )
        else:
            leave_summary.append(f"{employees[emp_id]['name']} leave request denied. Insufficient balance.")
    return leave_summary

# Main Execution
def main():
    """
    Main function to handle leave management operations.
    """
    employees = get_employee_data()
    leave_requests = [
        ("E001", 3),
        ("E003", 2),
        ("E005", 4),
        ("E002", 1),
        ("E004", 5),
        ("E999", 3),
        ("E003", -2)
    ]

    leave_summary = process_leave_requests(employees, leave_requests)

    print("\n--- Leave Management Summary ---")
    for status in leave_summary:
        print(status)


if __name__ == "__main__":
    main()
