
class todo:
    def __init__(self):
        pass

    def add_task(self):
        pass

    def view_task(self):
        pass

    def mark_complete(self):
        pass

    def delete_task(self):
        pass

def main():

    todoObj = todo()
    print("\n====TO-DO List====\n")
    print("\n1. Add Task\n2. View Task\n3. Mark Complete\n4. Delete Task\n5. Exit\n")

    choice = input("Enter your choice :: ")
    while True:
        match choice:
            case "1":
                todoObj.add_task()
            case "2":
                todoObj.view_task()
            case "3":
                todoObj.mark_complete()
            case "4":
                todoObj.delete_task()
            case "5":
                print("\nExiting the System, Bye\n")
                break
            case _:
                print("Enter a valid choice, Thankyou")
        
if __name__ == "__main__":
    main()
