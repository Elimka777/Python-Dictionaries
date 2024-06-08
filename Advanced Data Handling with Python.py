hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(room_number, customer_name):
    if hotel_rooms[room_number]["status"] == "available":
        hotel_rooms[room_number]["status"] = "booked"
        hotel_rooms[room_number]["customer"] = customer_name
        print(f"Room {room_number} successfully booked for {customer_name}.")
    else:
        print(f"Room {room_number} is already booked.")

# Function to check-out a customer
def check_out_room(room_number):
    if hotel_rooms[room_number]["status"] == "booked":
        hotel_rooms[room_number]["status"] = "available"
        customer_name = hotel_rooms[room_number]["customer"]
        hotel_rooms[room_number]["customer"] = ""
        print(f"Room {room_number} successfully checked out. {customer_name} has left the room.")
    else:
        print(f"Room {room_number} is already available.")

# Function to display the status of all rooms
def display_room_status():
    for room_number, details in hotel_rooms.items():
        status = details["status"]
        customer = details["customer"]
        print(f"Room {room_number}: {status}, Customer: {customer}")

# Example usage
display_room_status()
print()

book_room("101", "Miranda Ker")
print()

display_room_status()
print()

check_out_room("102")
print()

display_room_status()