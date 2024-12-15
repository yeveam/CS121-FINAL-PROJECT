rooms = [
    "101", "102", "103", "104", "105", "106", "201", "202",
    "COMPUTER LABORATORY 1", "COMPUTER LABORATORY 2", "COMPUTER LABORATORY 3",
    "COMPUTER LABORATORY 4", "COMPUTER LABORATORY 5", "COMPUTER LABORATORY 6",
    "SMART ROOM", "EDL", "ITL", "501", "502", "503", "504", "505", "506"
]

room_availability = {room: True for room in rooms}

def handle_login():
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "admin":
        print("Login successful!")
        return True
    elif username == "guest" and password == "guest":
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

def show_available_rooms():
    print("Available Rooms:")
    for room, available in room_availability.items():
        if available:
            print(f"Room: {room} - Available")

def reserve_room():
    room_name = input("Enter Room Name to Reserve: ")
    if room_name in room_availability:
        if room_availability[room_name]:
            room_availability[room_name] = False
            print(f"{room_name} has been reserved.")
        else:
            print(f"{room_name} is already reserved.")
    else:
        print(f"Room {room_name} not found.")

def cancel_reservation():
    room_name = input("Enter Room Name to Cancel Reservation: ")
    if room_name in room_availability:
        if not room_availability[room_name]:
            room_availability[room_name] = True
            print(f"Reservation for {room_name} has been canceled.")
        else:
            print(f"{room_name} is not reserved.")
    else:
        print(f"Room {room_name} not found.")

def show_reserved_rooms():
    print("Reserved Rooms:")
    for room, available in room_availability.items():
        if not available:
            print(f"Room: {room} - Reserved")

def main():
    logged_in = False

    while not logged_in:
        logged_in = handle_login()

    while True:
        print("\nWelcome to CICS Reservation Room!")
        print("1. View Available Rooms")
        print("2. Reserve Room")
        print("3. Cancel Reservation")
        print("4. View Reserved Rooms")
        print("5. Exit")
        choice = int(input("\nENTER CHOICE: "))

        if choice == 1:
            show_available_rooms()
        elif choice == 2:
            reserve_room()
        elif choice == 3:
            cancel_reservation()
        elif choice == 4:
            show_reserved_rooms()
        elif choice == 5:
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
