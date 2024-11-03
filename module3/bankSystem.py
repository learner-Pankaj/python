# cash withdrawal
# cash credit
# change password

balance = 1000000.00
password = "12345678"

def cashWithdrawal(pswd, amount):
    global balance 
    if (pswd == password):
        if (amount < balance):
            balance -= amount
            print(f"\nWithdrawl Successful!!\nYour new balance is {balance}")
        else:
            print("Insufficient Balance")
    else:
        print("Wrong Password, Try again!!")

def cashCredit(amount):
    global balance
    balance += amount
    print(f"deposite successfull of Rs. {amount}")
    print(f"Your new Balance is {balance}")

def changePswd(oldPswd, newPswd):
    if password == oldPswd:
        oldPswd = newPswd
        print("Password successfully Updated.")
    else:
        print("Incorrect Password, Try Again!!!")

def main():
    while True:
        print("\n Bank System \n")
        print("1. Cash Withdrawal")
        print("2. Cash Deposite")
        print("3. Update Password")
        print("4. Exit")

        choice = int(input("Enter Choice your choice : "))
        global password

        if choice == 1:
            amount = float(input("Enter Amount :: "))

            cashWithdrawal(password, amount)
        
        elif choice == 2:
            amount = float(input("Enter Amount :: "))
            cashCredit(amount)

        elif choice == 3:
            oldPswd = input("Enter Old Password : ")
            newPswd = input("Enter New Password : ")
            changePswd(oldPswd, newPswd)

        elif choice == 4:
            print("Exiting the System, Thankyou!!!")
            break

        else:
            print("Please Enter valid choice!!!")

main()