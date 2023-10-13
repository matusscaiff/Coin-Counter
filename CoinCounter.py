coins_info = {
    0.01: [1, 3.56],
    0.02: [1, 7.12],
    0.05: [5, 2.35],
    0.10: [5, 6.50],
    0.20: [10, 5.00],
    0.50: [10, 8.00],
    1.00: [20, 8.75],
    2.00: [20, 12.00]
}

errors = 0
correct_bags = 0

# coin_type: [bag_value, coin_weight]

for key, value in coins_info.items():
    coin_type = key
    coin_info = value
    bag_value = value[0]
    coin_weight = value[1]

    # number_of_coins = bag_value / coin_type
    bag_weight = (bag_value / coin_type) * coin_weight
    coin_info.append(bag_weight)

#coin_type: [bag_value, coin_weight]

#Checks that the user inputs the correct coin type
while True:
    try:
        coin_type_input = float(input("Input coin type (eg. 0.5 for pence or 1 for pounds): "))
    except ValueError:
        print("Invalid input please try again!")
        continue

    if coin_type_input not in coins_info:
        print("Coin type: INVALID")
        continue
    else:
        print("Coin type: VALID")

    # uses the user input to get the correct information for the coin type e.g 0.01: dictionary[]
    correct_coin_info = coins_info[coin_type_input]

    coin_weight = correct_coin_info[2]
    break

while True:
    try:
        bag_weight_input = float(input("Input bag weight: "))
    except ValueError:
        print("Please input a valid number")
        continue
    excess = (bag_weight_input - bag_weight) / coin_weight
    print(f"You should remove {round(excess)} coins (approx)")
    correct_bags += 1
    print(correct_bags)
