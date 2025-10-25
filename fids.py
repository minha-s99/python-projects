import time
import math



# =========================================
# Helper functions
# =========================================

def line():
    print("=" * 75)

def display_header():
    line()
    print("{:<10} {:<20} {:<10} {:<8} {:<15}".format("Flight", "Destination", "Time", "Gate", "Status"))
    line()

def display_all_flights():
    print("\n🛫 FLIGHT INFORMATION BOARD")
    display_header()
    for f in flights:
        print("{:<10} {:<20} {:<10} {:<8} {:<15}".format(
            f["Flight No"], f["Destination"], f["Time"], f["Gate"], f["Status"]
        ))
    line()

# =========================================
# Flight management functions
# =========================================

def add_flight():
    print("\n➕ Add New Flight")
    flight_no = input("Enter Flight Number: ").upper()  # stays uppercase
    dest = input("Enter Destination: ").title()
    time_ = input("Enter Departure Time (HH:MM): ")
    gate = input("Enter Gate: ").upper()
    status = input("Enter Status (On Time / Delayed / Boarding / Cancelled): ").title()
    new_flight = {"Flight No": flight_no, "Destination": dest, "Time": time_, "Gate": gate, "Status": status}
    flights.append(new_flight)
    print("✅ Flight added successfully!")

def update_status():
    print("\n✏️ Update Flight Status")
    flight_no = input("Enter Flight Number: ").upper()  # stays uppercase
    found = False
    for f in flights:
        if f["Flight No"] == flight_no:
            new_status = input("Enter new status (On Time / Delayed / Boarding / Cancelled): ").title()
            f["Status"] = new_status
            print("✅ Status updated successfully!")
            found = True
            break
    if not found:
        print("❌ Flight not found!")

def remove_flight():
    print("\n🗑️ Remove Flight")
    flight_no = input("Enter Flight Number to remove: ").upper()  # stays uppercase
    found = False
    for f in flights:
        if f["Flight No"] == flight_no:
            flights.remove(f)
            print("✅ Flight removed successfully!")
            found = True
            break
    if not found:
        print("❌ Flight not found!")

# =========================================
# Extra feature: Flight countdown
# =========================================

def calculate_time_diff(departure):
    """Calculate hours and minutes remaining from current time to departure."""
    try:
        h, m = map(int, departure.split(":"))
        current = time.localtime()
        current_mins = current.tm_hour * 60 + current.tm_min
        flight_mins = h * 60 + m
        diff = flight_mins - current_mins

        if diff < 0:
            return "Departed"
        else:
            hours = math.floor(diff / 60)
            mins = diff % 60
            return f"{hours} hr {mins} min remaining"
    except:
        return "Invalid Time Format"

def view_flight_details():
    print("\n🔍 View Flight Details")
    flight_no = input("Enter Flight Number: ").upper()  # stays uppercase
    found = False
    for f in flights:
        if f["Flight No"] == flight_no:
            line()
            print("FLIGHT DETAILS")
            line()
            print(f"Flight No     : {f['Flight No']}")
            print(f"Destination   : {f['Destination']}")
            print(f"Departure Time: {f['Time']}")
            print(f"Gate          : {f['Gate']}")
            print(f"Status        : {f['Status']}")
            print(f"Countdown     : {calculate_time_diff(f['Time'])}")
            line()
            found = True
            break
    if not found:
        print("❌ Flight not found!")

# =========================================
# Main Program Loop
# =========================================

def main():
    while True:
        print("\n--- ✈️ FLIGHT INFORMATION DISPLAY SYSTEM (FIDS) ---")
        print("1. View All Flights")
        print("2. View Flight Details")
        print("3. Add New Flight")
        print("4. Update Flight Status")
        print("5. Remove Flight")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_all_flights()
        elif choice == "2":
            view_flight_details()
        elif choice == "3":
            add_flight()
        elif choice == "4":
            update_status()
        elif choice == "5":
            remove_flight()
        elif choice == "6":
            print("\nThank you for using the FIDS system. Safe travels! 🛫")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")

        time.sleep(1.5)  # small pause for readability

# Run the program
flights = [
    {"Flight No": "AK102", "Destination": "Kuala Lumpur", "Time": "08:45", "Gate": "A2", "Status": "On Time"},
    {"Flight No": "MH234", "Destination": "Singapore", "Time": "09:15", "Gate": "B1", "Status": "Boarding"},
    {"Flight No": "QR567", "Destination": "Doha", "Time": "10:00", "Gate": "C3", "Status": "Delayed"},
    {"Flight No": "EK320", "Destination": "Dubai", "Time": "11:30", "Gate": "A5", "Status": "On Time"},
    {"Flight No": "SQ890", "Destination": "Bangkok", "Time": "12:00", "Gate": "B4", "Status": "Cancelled"}
]

main()
