def check_Password(s):
    capital_letter = any(char.isupper() for char in s)
    small_letter = any(char.isupper() for char in s)
    digit = any(char.isdigit() for char in s)
    special_char = any(not char.isalnum() for char in s) #not alpha numeric is a special character
    if(capital_letter & small_letter & digit & special_char):
        return True
    else :
        return False

uname = input("Enter Username :: ")
password = input("Enter Password :: ")

check = check_Password(password)
if(check == True) & (len(password)>=6) & (len(password)<=32):
    print("\nWelcome %s \n"% uname)
else:
    print("\nWrong Password!!! \nTry Again!!!\n")
