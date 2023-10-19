file_path = "Coin_Count.txt"

while True:
    try:
        start_option = int(input("Enter '1' to begin counting coins or '2' to list existing data: "))
    except ValueError:
        print("Please input a valid number")
        continue

    if start_option == 1:
        #Continues on with the code so that the user can count another bag
        break

    elif start_option == 2:
        # Allows the user to list the existing data
        with open(file_path, "r") as f:
            data_lines = f.readlines()
            data_lines = [line.strip().split() for line in data_lines]

            # Update accuracy and convert it to a float
            for line in data_lines:
                line[-1] = float(line[-1].rstrip('%'))

            # Sort the data by accuracy from highest to lowest
            data_lines.sort(key=lambda x: x[-1], reverse=True)

            print("Volunteer name | Coin Type | Bag Weight | Accuracy")
            for line in data_lines:
                print(f"{line[0]} | {line[1]} | {line[2]} | {line[4]:.1f}%")

        exit()  # Exits the program so that the other code isnt executed
    else:
        print("You need to input '1' or '2' to proceed")


# Reads the txt file and creates variables for all the data in the txt file
try:
    with open(file_path, "r") as f:
        file_contents = f.read()

        lines = file_contents.split('\n')

        for line in lines:
            data = line.split()

            if len(data) == 4:
                volunteer_name, user_coin_type, bag_weight_input, accuracy = data
                volunteer_name = volunteer_name.strip()
                user_coin_type = float(user_coin_type)
                bag_weight_input = float(bag_weight_input)
                accuracy = float(accuracy.rstrip('%'))
except FileNotFoundError:
    print(f"File '{file_path}' not found. Starting with empty data.")

# Data for the coins and bags
coins_info = {
    0.01: [1, 3.56],  # first column is the coin type
    0.02: [1, 7.12],  # second column is the bag value
    0.05: [5, 2.35],  # third column is the coin weight
    0.10: [5, 6.50],
    0.20: [10, 5.00],
    0.50: [10, 8.00],
    1.00: [20, 8.75],
    2.00: [20, 12.00]
}

# Variables that are used to calculate the volunteer's accuracy and total bags counted as well as the total bag value
errors = 0
correct_bags = 0
bags_checked = 0
total_bag_value = 0

# Assigns variables to each value in the dictionary
for key, value in coins_info.items():
    coin_type = key
    bag_value = value[0]
    coin_weight = value[1]

    #calculates the expected bag weight of the coin
    bag_weight = (bag_value / coin_type) * coin_weight
    value.append(bag_weight)


volunteer_name_input = input("Input Volunteer name: ").lower()


name_exists = False
user_coin_type = None

for line in lines:
    data = line.split()
    if len(data) == 4:
        name, existing_coin_type_str, bag_weight_input, accuracy_str = data
        if name == volunteer_name_input:
            name_exists = True
            user_coin_type = float(existing_coin_type_str)
            print(f"Using existing coin type: {user_coin_type}")
            break

# If the name doesn't exist or the existing coin type is invalid then it will prompt for the coin type
if not name_exists or user_coin_type not in coins_info:
    while True:
        try:
            user_coin_type = float(input("Input coin type (e.g., 0.5 for pence or 1 for pounds): "))
        except ValueError:
            print("Invalid input. Please try again!")
            continue

        if user_coin_type not in coins_info:
            print("Coin type: INVALID")
        else:
            print("Coin type: VALID")
            break

# Calculate bag_weight based on the user inputs
bag_weight = (coins_info[user_coin_type][0] / user_coin_type) * coins_info[user_coin_type][1]

# Reset bags_checked, errors, and correct_bags at the beginning of each run so that values arent repeated and create invalid data
bags_checked = 0
errors = 0
correct_bags = 0

# Checks how many coins the user needs to take out and what their total value for that specific coin is
while True:
    try:
        bag_weight_input = float(input("Input bag weight in grams: "))
    except ValueError:
        print("Please input a valid number")
        continue

    if bag_weight_input > bag_weight:
        extra = (bag_weight_input - bag_weight) / coin_weight
        print(f"You should remove {round(extra)} coins (approx)")
        errors += 1
        bags_checked += 1
        total_bag_value += (extra + bag_value)
        total_bag_value = round(total_bag_value, 2)
        break

    elif bag_weight_input < bag_weight:
        not_enough = (bag_weight - bag_weight_input) / coin_weight
        print(f"You should add {round(not_enough)} coins")
        errors += 1
        bags_checked += 1
        total_bag_value += (bag_value - not_enough)
        total_bag_value = round(total_bag_value, 2)
        break

    else:
        print("You have entered the correct amount of coins into the bag")
        correct_bags += 1
        bags_checked += 1
        total_bag_value += bag_value
        total_bag_value = round(total_bag_value, 2)
        break

# Calculate accuracy based on the current run
accuracy = (correct_bags / bags_checked) * 100

table_data = ["Volunteer name", "Coin Type", "Bag Weight", "Accuracy"]

# Check if the name is already in the txt file
# Check if the name and coin type combination exists
name_coin_type_found = False
data_lines = []

with open(file_path, "r") as f:
    for line in f:
        volunteer_name, user_coin_type_str, total_bag_value_str, bags_checked_str, accuracy_str = line.split()
        user_coin_type_existing = float(user_coin_type_str)

        if volunteer_name == volunteer_name_input and user_coin_type_existing == user_coin_type:
            name_coin_type_found = True
            total_bag_value_existing = float(total_bag_value_str)
            bags_checked_existing = int(bags_checked_str)
            accuracy_existing = float(accuracy_str.rstrip('%'))

            total_bag_value += total_bag_value_existing
            bags_checked += bags_checked_existing
            accuracy = (correct_bags / bags_checked) * 100  # Update accuracy
            accuracy += (bags_checked_existing / bags_checked) * accuracy_existing

            updated_data = f"{volunteer_name_input} {user_coin_type} {total_bag_value} {bags_checked} {accuracy:.1f}%"
            data_lines.append(updated_data)
        else:
            data_lines.append(line.strip())

# If the name and coin type combination was found then it will update the line
if name_coin_type_found:
    with open(file_path, "w") as f:
        for line in data_lines:
            f.write(f"{line}\n")

# If not found append a new line for data to be saved to
if not name_coin_type_found:
    with open(file_path, "a") as f:
        f.write(f"{volunteer_name_input} {user_coin_type} {total_bag_value} {bags_checked} {accuracy:.1f}%\n")

# Allows the user to choose whether they would like to see the number of bags checked or their total value aswell as all the saved data
while True:
    try:
        user_option = int(input("Enter '1' if you would like to see the number of bags checked, '2' to see the total value, '3' to exit the program, or '4' to list data by accuracy: "))
    except ValueError:
        print("Please input a valid number")
        continue

    if user_option == 1:
        print("Bags checked:", bags_checked)
        break

    elif user_option == 2:
        print("Total bag value:", total_bag_value)
        break

    elif user_option == 3:
        print("Exiting program!")
        exit() #allows the user to exit the program without seeing all the data

    elif user_option == 4:
        # List data sorted by accuracy
        with open(file_path, "r") as f:
            data_lines = f.readlines()
            data_lines = [line.strip().split() for line in data_lines]

            # Update accuracy and convert it to a float
            for line in data_lines:
                line[-1] = float(line[-1].rstrip('%'))
                volunteer_name = line[0]
                user_coin_type = float(line[1])
                bags_checked = int(line[3])
                accuracy = line[-1]

                # Calculate the total bag value for each line and store it in total_bag_value
                total_bag_value = (bags_checked * coins_info[user_coin_type][0]) + total_bag_value
                line.append(total_bag_value)
                line[-1] = round(line[-1], 2)

            # Sort the data by accuracy
            data_lines.sort(key=lambda x: x[-2], reverse=True)  # Sort by total bag value

            print("Volunteer name | Coin Type | Bag Weight | Accuracy | Total Bag Value")
            for line in data_lines:
                print(f"{line[0]} | {line[1]} | {line[2]} | {line[4]:.1f}% | {line[5]}")
        break

    else:
        print("You need to input '1', '2', '3', or '4' to get your desired output")
