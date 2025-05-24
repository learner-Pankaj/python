class bankSystem:
    def __init__(self):
        pass

    def create_account(self):
         print("Account Created")

    def check_balance(self):
        print("Available Balance :: ")

    def deposit(self):
        print("You deposited :: ")

    def withdraw(self):
        print("you withdrawn :: ")

    def transfer(self):
        print("you transfered to NAME")


def main():
    bank_system = bankSystem()
    while True:
        print("\n1. Create Account\n2. Check Balance\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Exit")
        choice = input("Enter your choice : ")

        match choice:
            case "1":
                bank_system.create_account()
        
            case "2":
                bank_system.check_balance()
                
            case "3":
                bank_system.deposit()
                
            case "4":
                bank_system.withdraw()
                
            case "5":
                bank_system.transfer()
                
            case "6":
                print("\nExiting System, Bye\n")
                break
            case _:
                print("Choose correct option, Try again")

if __name__ == "__main__":
    main()
