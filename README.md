# Sales Call Logger

A simple Python script to log and track sales call details for business development teams. This tool allows you to log sales calls, view call history, and export the call data to a CSV file.

## Features
- **Log Client Calls**: Allows you to input client name, call date, outcome, and next steps.
- **View Call History**: Displays a list of all logged calls with details such as outcome and next steps.
- **Export to CSV**: Exports the logged calls to a CSV file for easy reporting and sharing.
- **Interactive CLI**: A simple command-line interface (CLI) to interact with the tool.

## The Python Code

```python
import csv
from datetime import datetime

# Initialize call log list
call_logs = []

# Log a sales call
def log_call(client_name, call_date, outcome, next_steps):
    call = {
        "Client Name": client_name,
        "Call Date": call_date,
        "Outcome": outcome,
        "Next Steps": next_steps
    }
    call_logs.append(call)
    print("Call logged successfully!")

# View call history
def view_calls():
    print("\n--- Sales Call History ---")
    if not call_logs:
        print("No calls logged yet.")
    else:
        for i, call in enumerate(call_logs, 1):
            print(f"{i}. Client: {call['Client Name']}, Date: {call['Call Date']}, Outcome: {call['Outcome']}, Next Steps: {call['Next Steps']}")

# Export call logs to CSV
def export_to_csv(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Client Name", "Call Date", "Outcome", "Next Steps"])
        writer.writeheader()
        writer.writerows(call_logs)
    print(f"Call logs exported to {filename} successfully!")

# Menu
while True:
    print("\n--- Sales Call Logger ---")
    print("1. Log a Sales Call")
    print("2. View Call History")
    print("3. Export Call Logs to CSV")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        client_name = input("Enter Client Name: ")
        call_date = input("Enter Call Date (YYYY-MM-DD): ")
        outcome = input("Enter Call Outcome (e.g., Interested, Not Interested, Follow-Up Needed): ")
        next_steps = input("Enter Next Steps: ")
        log_call(client_name, call_date, outcome, next_steps)
    elif choice == "2":
        view_calls()
    elif choice == "3":
        filename = input("Enter filename (e.g., calls.csv): ")
        export_to_csv(filename)
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
```
## How to Run the Script
1. Ensure that Python 3.x is installed on your machine.
2. Download the Python script sales_call_logger.py from the repository.
3. Open your terminal or command prompt.
4. Navigate to the folder where the sales_call_logger.py file is located.
5. Run the script using the following command:
```
python sales_call_logger.py
```
6. Follow the interactive menu to log calls, view the call history, or export the call logs to a CSV file.

## Code Output 
### Example Menu Output:
```
--- Sales Call Logger ---
1. Log a Sales Call
2. View Call History
3. Export Call Logs to CSV
4. Exit
Choose an option: 1
Enter Client Name: ABC Corp
Enter Call Date (YYYY-MM-DD): 2025-01-19
Enter Call Outcome (e.g., Interested, Not Interested, Follow-Up Needed): Interested
Enter Next Steps: Schedule a demo
Call logged successfully!
```
### Example of Call History Output:
```
--- Sales Call History ---
1. Client: ABC Corp, Date: 2025-01-19, Outcome: Interested, Next Steps: Schedule a demo
```
### Example of Exported CSV:
```
Client Name, Call Date, Outcome, Next Steps
ABC Corp, 2025-01-19, Interested, Schedule a demo
```
## Conclusion
The Sales Call Logger is a simple yet effective tool to help business development teams keep track of their client calls and follow-ups. By using this Python script, teams can efficiently log and organize sales interactions, track outcomes, and easily export call data for reporting or further analysis.

This project demonstrates how basic Python skills can be applied to improve task management in a real-world business context, especially in sales and customer relationship management.


