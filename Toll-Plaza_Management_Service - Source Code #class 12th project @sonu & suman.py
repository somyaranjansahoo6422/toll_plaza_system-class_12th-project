toll_plazas = []

def add_toll_plaza(name, location, vehicle_type):
    toll_rate = calculate_toll_rate(vehicle_type)
    for plaza in toll_plazas:
        if plaza['name'] == name:
            print(f"Error: A toll plaza with the name '{name}' already exists.")
            return
    toll_plazas.append({'name': name, 'location': location, 'toll_rate': toll_rate})
    print("Toll plaza added successfully.")

def remove_toll_plaza(name):
    for plaza in toll_plazas:
        if plaza['name'] == name:
            toll_plazas.remove(plaza)
            print("Toll plaza removed successfully.")
            return
    print(f"No toll plaza found with the name '{name}'.")

def update_toll_plaza(name, location=None, vehicle_type=None):
    if not location and vehicle_type is None:
        print("No update values provided. Please specify a new location or vehicle type.")
        return

    for plaza in toll_plazas:
        if plaza['name'] == name:
            if location:
                plaza['location'] = location
            if vehicle_type:
                plaza['toll_rate'] = calculate_toll_rate(vehicle_type)
            print("Toll plaza updated successfully.")
            return
    print(f"No toll plaza found with the name '{name}'.")

def display_toll_plazas():
    if not toll_plazas:
        print("No toll plazas available.")
        return
    for plaza in toll_plazas:
        print(f"Name: {plaza['name']}, Location: {plaza['location']}, Toll Rate: {plaza['toll_rate']}")

def calculate_toll_rate(vehicle_type):
    toll_rates = {
        4: 100,
        6: 150,
        8: 210,
        10: 380,
        12: 560,
        14: 1030
    }
    return toll_rates.get(vehicle_type, 0)

def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input
        print("Invalid input. Please try again.")

def display_toll_plaza_table():
    total_toll_rate = sum(plaza['toll_rate'] for plaza in toll_plazas)
    print("---------------------------------------------")
    print("| {0:<10} | {1:<15} | {2:<10} |".format("Name", "Location", "Toll Rate"))
    print("---------------------------------------------")
    for plaza in toll_plazas:
        print("| {0:<10} | {1:<15} | ₹{2:<8} |".format(plaza['name'], plaza['location'], plaza['toll_rate']))
    print("---------------------------------------------")
    print("| {0:<10} | {1:<15} | ₹{2:<8} |".format("Total", "", total_toll_rate))
    print("---------------------------------------------")

def main():
    print("--------------------------------------------------------------------------------------")
    print("                                    Toll Plaza Management")
    print("--------------------------------------------------------------------------------------")
    while True:
        print("\n1. Add Toll Plaza")
        print("2. Remove Toll Plaza")
        print("3. Update Toll Plaza")
        print("4. Display Toll Plazas")
        print("5. Exit")

        choice = get_user_input("Enter your choice:")

        if choice == "1":
            name = get_user_input("Enter toll plaza no.:")
            location = get_user_input("Enter toll plaza location:")
            vehicle_type = int(get_user_input("Enter your vehicle type (4, 6, 8, 10, 12, 14):"))
            add_toll_plaza(name, location, vehicle_type)

        elif choice == "2":
            name = get_user_input("Enter toll plaza name:")
            remove_toll_plaza(name)

        elif choice == "3":
            name = get_user_input("Enter toll plaza name:")
            location = get_user_input("Enter new toll plaza location (optional):").strip()
            vehicle_type_input = get_user_input("Enter new vehicle type (optional):").strip()

            if vehicle_type_input:
                try:
                    vehicle_type = int(vehicle_type_input)
                except ValueError:
                    print("Invalid vehicle type. Please enter a number.")
                    continue
            else:
                vehicle_type = None

            update_toll_plaza(name, location if location else None, vehicle_type)

        elif choice == "4":
            print("="*86)
            print(" "*36, "Toll Plaza Table")
            print("="*86)
            display_toll_plaza_table()
            print("="*86)

        elif choice == "5":
            print("="*86)
            print(" "*36, "Thank You!")
            print(" "*34, "@ SEE_YOU_AGAIN...")
            print("="*86)
            break

if __name__ == "__main__":
    main()
