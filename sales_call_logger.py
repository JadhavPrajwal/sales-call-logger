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
