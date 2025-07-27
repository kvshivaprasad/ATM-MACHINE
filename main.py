# ATM MACHINE
# Set initial user details
user_amount = 10000
user_pin = 123  # Default ATM PIN
start_machine = True
user_name = input("ENTER YOUR NAME PLEASE: ")
user_detail = {"user name" : user_name , "Current Balance" : user_amount}
print("-----------WELCOME-----------")

# Main ATM loop

while start_machine:
    Enter_pin = int(input("ENTER YOUR 3 DIGIT PIN: "))
    if Enter_pin == user_pin:
        print(f"Select any option, {user_name}!")
        option = input("A: Withdraw , B: Deposit , C: Change PIN , D: Check Balance , E: Exit : ").lower()
        if option == "a": # Withdraw money
            withdraw_amount = float(input("Enter withdraw amount: "))
            if withdraw_amount <= user_amount:
                user_amount -= withdraw_amount
                print(f"Withdraw succesfull, {user_name}!")
                print(f"Current Balance: ₹{user_amount:.2f}")
            else:
                print("Insufficient balance.")
        elif option == "b": # Deposit money
            depo_amount = float(input("Enter deposit amount: "))
            user_amount += depo_amount
            print(f"Deposit successful, {user_name}!")
            print(f"Current Balance: ₹{user_amount:.2f}")
        elif option == "c": # Change PIN
            Enter_pin = int(input("ENTER YOUR OLD 3 DIGIT PIN: "))
            if Enter_pin == user_pin:  
               new_pin = int(input("Enter your new PIN: "))
               print("PIN successfully changed!")
               user_pin = new_pin 
            else:
                print("Wrong PIN")
        elif option == "d": # Check balance
            print(f"Balance: ₹{user_amount}")
        elif option == "e": # Exit ATM
            start_machine = False
        else:
            print("Option does not match. please try again.")
    else:    
     print("Wrong PIN. Try again. ") 
       
       # Print account slip 
print("-----------Slip---------------")
print("YOUR BANK ACCOUNT DETAILS....")
for key , value in user_detail.items():
    if key == "Current Balance":
     print(f"{key:10} : ${value:.2f}")
    else:
      print(f"{key:10} : {value}")          
print("-----------THANK YOU----------")
