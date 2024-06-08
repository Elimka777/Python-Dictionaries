# Initial service ticket structure
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to open a new service ticket
def open_ticket(ticket_id, customer_name, issue_description):
    if ticket_id not in service_tickets:
        service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
        print(f"Ticket {ticket_id} opened for {customer_name} with issue: {issue_description}")
    else:
        print(f"Ticket {ticket_id} already exists.")

# Function to update the status of an existing ticket
def update_ticket_status(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
        print(f"Ticket {ticket_id} status updated to {status}")
    else:
        print(f"Ticket {ticket_id} not found.")

# Function to display all tickets or filter by status
def display_tickets(status=None):
    for ticket_id, details in service_tickets.items():
        if status is None or details["Status"] == status:
            customer = details["Customer"]
            issue = details["Issue"]
            status = details["Status"]
            print(f"Ticket {ticket_id}: Customer: {customer}, Issue: {issue}, Status: {status}")

# Example usage
display_tickets()
print()

open_ticket("Ticket003", "Ella", "Account locked")
print()

update_ticket_status("Ticket001", "closed")
print()

display_tickets()
print()

display_tickets("open")
