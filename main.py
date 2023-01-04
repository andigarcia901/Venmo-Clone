user_one = {
    'user one account details': [
        {
            "full name" : "Snoopy",
            "username" : "JoeCool",
            "password" : "password123",
            "account balance" : 100,
            "connected banks": [
                ("Bank of America", 200)
            ]
        
        }
    ]
}
user_two = {
    'user two account details': [
        {
            "full name" : "Woodstock",
            "username" : "LittleBird",
            "password" : "bestfriend123",
            "account balance" : 150,
            "connected banks" :[
                ("Wells Fargo", 250)
            ]
        }
    ]
}

def get_username():
    username = input("Please enter username: ")
    if username == ['user one account details'][1]['username']:
        print("Username is correct.")
    else:
        print("Username is incorrect.")

get_username()

def get_password():
    password = input("Please enter passowrd: ")
    if password == user_one ["user one account details"][2]['password']:
        print("You have successfully logged in.")
    else:
        print("Password is incorrect.")

get_password()
print('')
print(f'Your account balance is ')




