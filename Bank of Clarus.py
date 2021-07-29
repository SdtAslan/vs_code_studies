balance = 1000
while True:
    print("Welcome to the Bank Of Clarus", "\n", "\n", "Please select the action you want to take", "\n", "\n", "1-Balance inquiry", "\n", "2-Invest in", "\n", "3-Draft", "\n", "Press q to exit")
    x = str(input("Press any key"))
    if x == "1":
        print("Your Balance is:", balance)    
    elif x == "2":
        a = int(input("Add your money.Up to 40 pieces. Please entry amount"))
        balance = balance + a
        print("Your new balance is: ",balance)
    elif x == "3":
        b = int(input("Enter the amount you want to draft:"))
        if balance >= b:
            balance = balance -b
            print("Available balance is:", balance)
        else:
            print("Insufficient balance")
    elif x == "q":
        print("See you again")
        break
    else:
        print("Try again")
    question_ = str(input("Would you like to take another action? (press 'y' : yes, 'n' : no)"))
    if question_ == "y":
        True
    else:
        break