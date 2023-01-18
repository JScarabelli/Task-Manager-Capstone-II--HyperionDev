# compulsory task part 1

# =====importing libraries===========
# to clear the interpreter console.

# ====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

# I have not deleted the pseudo-code as a comment guide for the file.
# global variable and granted to run code.
user_name = "admin"
granted = False


# This function allows new users to be added inside the register function
def grant():
    global granted
    granted = True

# prompt option to the user:
def main():
    global option
    print("\nMain Menu")
    print("══════════")
    print("Type 1 - Register (only admin)")
    print("Type 2 - Login")

    while True:
        print()
        option = input("Choose an option: ")
        if option in ["1", "2"]:
            break


# this function will prompt the user with option to login or register.
def access(option):

    while option == "2":
        user_name = input("Please enter your username: ")
        user_password = input("Please enter your password: ")
        login(user_name, user_password)
    else:
        user_name = input("Please create your username: ")
        user_password = input("Please create your password: ")
        #register(user_name, user_password)

        # confirming that the passwords match.
        while True:
            confirm_password = input("Confirm your Password: ")
            if confirm_password == user_password:
                break
            else:
                print("Passwords do not match!")
                print("Please try again")


# this function will allow to login as admin or if you are already registered.
def login(user_name, user_password):

    # checking the user to validate its entry.
    success = False
    file = open("user.txt", "r")
    for i in file:
         a, b = i.split(",")
         b = b.strip()
         if a == user_name and b == user_password:
            success = True
            break
    file.close()

    if success:
        print("\nLogin Successful")
        menu()
    else:
        print("wrong username or password")


# adding user information to user.txt file and split them with white space and creating a new line.
def register(user_name, user_password):
    file = open("user.txt", "a")
    file.write(f"\n{user_name}, {user_password}")
    grant()


# this function is to manipulate data from tasks.txt file.
def menu():

    while True:
        # presenting the menu to the user and
        # making sure that the user input is coneverted to lower case.
        print(f"══════════════════════\n")
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        s - Statistics
        e - Exit
        : ''').lower()

        if menu == 'r':
            '''In this block you will write code to add a new user to the user.txt file
                    - You can follow the following steps:
                        - Request input of a new username
                        - Request input of a new password
                        - Request input of password confirmation.
                        - Check if the new password and confirmed password are the same.
                        - If they are the same, add them to the user.txt file,
                        - Otherwise you present a relevant message.'''

            global user_name
            print(f"══════════════════════\n")
            if user_name == "admin":
                new_user_login = False
                new_user_name = input("Please enter a username: ")

            while new_user_login == False:

                new_user_password = input("Please enter a password: ")
                validate = input("Please confirm password: ")

                if new_user_password == validate:
                    new_user_login = True

                if new_user_password != validate:
                    print("password did not match. Please Try again")

                if new_user_password == validate:
                    print("password matches. New user created")

                    append = open("user.txt", "a")
                    append.write(f"\n{new_user_name}, {validate}")
                    append.close()


                if user_name != "admin":
                    print("Only admin can add a new user.")

        elif menu == 'a':
            '''In this block you will put code that will allow a user to add a new task to task.txt file
            - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

            # appending new task to the task.txt file.
            with open("tasks.txt", "a") as file:
                print("\n══════════════════")
                new_user = input("Please enter a username of the person whom the task is assigned to: ").lower()
                new_title = input("\nPlease enter a title of a task: ").lower()
                new_description = input("\nPlease enter a description of the task: ").lower()
                new_assigned_date = input("\nPlease enter the due date of the task: ").lower()
                current_date = input("\nPlease enter the current date: ").lower()
                new_completion = "No"
                file.write(f"\n{new_user}, {new_title}, {new_description}, {new_assigned_date}, "
                           f"{current_date}, {new_completion}")
                print("══════════════════\n")

        elif menu == "va":

            '''In this block you will put code so that the program will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
            You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

            # print out the task.txt data in format requested using the split function.
            tasks_read = open("tasks.txt", "r")
            data = tasks_read.readlines()

            # using enumerate to display the number of the task, starting at 1.
            for pos, line in enumerate(data, 1):
                split_data = line.split(", ")

                output = f"\n════════[{pos}]══════════\n"
                output += f"Assigned to:\t{split_data[0]}\n"
                output += f"Task:\t\t{split_data[1]}\n"
                output += f"Description: \t{split_data[2]}\n"
                output += f"assigned Date: \t{split_data[3]}\n"
                output += f"Due date: \t{split_data[4]}\n"
                output += f"Is completed: \t{split_data[5]}\n"
                output += f"══════════════════════\n"

                print(output)

        elif menu == 'vm':

            '''In this block you will put code the that will read the task from task.txt file and
            print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
            You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

            tasks_read = open("tasks.txt", "r")
            for line in tasks_read:
                Assigned, Task, Description, assigned_Date, date, completed = line.split(", ")

                if user_name == Assigned:

                    output = f"\n══════════════════\n"
                    output += f"Assigned to:\t{Assigned}\n"
                    output += f"Task:\t\t{Task}\n"
                    output += f"Description: \t{Description}\n"
                    output += f"assigned Date: \t{assigned_Date}\n"
                    output += f"Due date: \t{date}\n"
                    output += f"Is completed: \t{completed}\n"
                    output += f"══════════════════════\n"

                    print(output)
            tasks_read.close()

        # counting the number of tasks and users.
        elif menu == "s":

            # as we have 1 user per line counted the total number of lines.
            with open("user.txt", "r") as file:
                data = file.read()
                lines = data.split("\n")
            num_users = 0
            for users in lines:
                if users:
                    num_users += 1

            # as we have 1 task per line counted the total number of lines.
            with open("tasks.txt", "r") as file_1:
                data = file_1.read()
                lines = data.split("\n")
            num_tasks = 0
            for tasks in lines:
                if tasks:
                    num_tasks += 1

            print("\nStatistics")
            print(f"════════════")
            print(f"Numbers of tasks: {num_tasks}\n")
            print(f"Numbers of Users: {num_users}")
            print(f"\n════════════")

        elif menu == 'e':

            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")

# looking forward for your feedback.


main()
access(option)


