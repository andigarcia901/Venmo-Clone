user_one = {
            "full_name" : "Snoopy",
            "username" : "JoeCool",
            "password" : "password123",
            "account_balance" : 100,
            "connected_banks": [
                ("Bank of America", 200)
            ]
        
        }
    

user_two = {
            "full_name" : "Woodstock",
            "username" : "LittleBird",
            "password" : "bestfriend123",
            "account_balance" : 150,
            "connected_banks" :[
                ("Wells Fargo", 250)
            ]
        }
   

def check_user():
    username_verified = False
    password_verified = False
    while username_verified == False:
        username = input("Please enter username: ")
        if username == user_one['username']:
            print("Username is correct.")
            username_verified = True
        else:
            print("Username is incorrect.")
    while password_verified == False:
        user_password = input("Please enter password: ")
        if user_password == user_one['password']:
            print("Password is correct.")
            password_verified = True
        else:
            print("Password is incorrect.")
    if username_verified == True and password_verified == True:
        print("")
        print(f"Welcome {user_one['full_name']}!")
        print('')
        print(f"Your current account balance is: {user_one['account_balance']}.")
        print('')
        print(f"Your connected bank and available funds are: {user_one['connected_banks']}.")

check_user()

def transfer_money():
    would_like_to_transfer_money = False
    while would_like_to_transfer_money == False:
        ask_user = input(f"Would you like to transfer money to {user_two['full_name']}? (Y/N) ")
        if ask_user == "Y":
            print("Beginning your transaction...")
            would_like_to_transfer_money = True
        else:
            print("Transaction cancelled.")
        
transfer_money()

currently_available = user_one["account_balance"]
def amount_to_transfer():
    transfer_amount_available = False
    while transfer_amount_available == False:
        ask_user = int(input("How much money would you like to transfer?"))
        if ask_user <= currently_available:
            print("Transfering the requested amount...")
            transfer_amount_available = True
        else:
            print("Insufficient funds.  Please enter a smaller amount to transfer.")
            transfer_amount_available = False

amount_to_transfer()

        



