bag_checked = 0 #counter for how many bags each volunteer has counted
errors = 0 #error counter to calculate each volunteers accuracy

def coin_types():
    coin_list= {
        "1p":[3.56, 1.00], #first collumn is the coin type
        "2p":[7.12, 1.00], #second collumn is the coin  weight
        "5p":[2.35, 5.00], #third collumn is the correct bag weight
        "10p":[6.40, 5.00],
        "20p":[5.00, 10.00],
        "50p":[8.00, 10.00],
        "£1":[8.75, 20.00],
        "£2":[12.00, 20.00]
    } #all coin weights are in grams
      #all bag weights are in £


def userinputs():
    volunteer_name = input ("Input your name: ")
    user_coin_type = input("Input coin type (eg. 5p or £1): ")
    user_bag_weight = float(input("Input the weight of the bag: "))
    return volunteer_name, user_coin_type, user_bag_weight


def calculations():
    global bag_checked
    global errors #allows for the variables to be updated not just in the def calculations()

    volunteer_name, user_coin_type, user_bag_weight = userinputs() # pulls out the user inputs from the previous def statement

    while True: #checkes if the coin type inputted is a valid option
        if user_coin_type in coin_types:
            break
        print("Coin type: INVALID")
        print("Please try again")
    print("Coin type: VALID")