coins_info = {
    0.01: [1, 3.56],# first collum is the coin type
    0.02: [1, 7.12],# second collum is the bag value
    0.05: [5, 2.35],# third collum is the coin weight
    0.10: [5, 6.50],
    0.20: [10, 5.00],
    0.50: [10, 8.00],
    1.00: [20, 8.75],
    2.00: [20, 12.00]
}

#variables that are used to calculate the volunteers accuracy and total bags counted aswell as the total bag value
errors = 0
correct_bags = 0
bags_checked = 0
total_bag_value = 0


for key, value in coins_info.items():
    coin_type = key
    coin_info = value
    bag_value = value[0]
    coin_weight = value[1]

    bag_weight = (bag_value / coin_type) * coin_weight
    coin_info.append(bag_weight)


volunteer_name = input("Input Volunteer name: ").lower()

#Checks that the user inputs the correct coin type
while True:
    try:
        user_coin_type = float(input("Input coin type (eg. 0.5 for pence or 1 for pounds): "))
    except ValueError:
        print("Invalid input please try again!")
        continue

    if user_coin_type not in coins_info:
        print("Coin type: INVALID")
        continue
    else:
        print("Coin type: VALID")

    bag_weight = (coins_info[user_coin_type][0] / user_coin_type) * coins_info[user_coin_type][1]
    break

#Checks how many coins the user needs to take out and what their total is
while True:
    try:
        bag_weight_input = float(input("Input bag weight in gramms: "))
    except ValueError:
        print("Please input a valid number")
        continue

    if bag_weight_input > bag_weight:
        extra = (bag_weight_input - bag_weight) / coin_weight
        print(f"You should remove {round(extra)} coins (approx)") #the letter f formats the variable extra and rounds it to the nearest intager
        errors += 1
        bags_checked += 1
        total_bag_value += (extra + bag_value)
        total_bag_value = round(total_bag_value,2)
        break

    elif bag_weight_input < bag_weight:
        not_enough = (bag_weight- bag_weight_input) / coin_weight
        print(f"You should add {round(not_enough)} coins")
        errors += 1
        bags_checked += 1
        total_bag_value += (bag_value - not_enough)
        total_bag_value = round(total_bag_value,2)
        break

    else:
        print("You have entered the correct ammount of coins into the bag")
        correct_bags += 1
        bags_checked += 1
        total_bag_value += bag_value
        break

while True:
    try:
        user_option = int(input("Enter '1' if you would like to see the number of bags checked and '2' if you would like to see the total value or '3' to exit the program: "))
    except ValueError:
        print("Please input a valid number")
        continue

    if user_option == 1:
        print("Bags checked:",bags_checked)
        break

    elif user_option == 2:
        print("Total bag value:",total_bag_value)
        break

    elif user_option == 3:
        print("!Exiting program!")
        exit()
    else:
        print("You need to input '1' or '2' to get your desired output")


#calculates the volunteers accuracy
accuracy = (errors/ bags_checked) * 100


txt_file_info = {
    volunteer_name : [user_coin_type, bag_weight_input, accuracy],
}
print(txt_file_info)

with open("Coin_Count_data.txt", "a") as file:
    json.dump(txt_file_info, file)
