import time

#Get time in current hour in 24 hour format
current_hour = time.localtime().tm_hour

if 6 <= current_hour <= 18:
    print("Its day outside.")
else :
    print("Its dark outside.")


