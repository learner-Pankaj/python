
def search_data(emp_name, target):
    emp_name.sort()
    left, right = 0, len(emp_name)-1
    while left <= right:
        mid = (left+right) // 2
        mid_val = emp_name[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid+1
        else : 
            right = mid - 1

    return -1

emp_name = ["Pankaj", "Lokesh", "Sharan", "Hrugved", "Naveen", "SK", "Shylesh", "Vipin", "Saurabh"]
target = input("Enter Name of the Employee : ")

index = search_data(emp_name, target)

if index != -1:
    print(f"{target} found on index {index}.")
else:
    print(f"{target} not in the list")