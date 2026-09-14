# R_GLAB_385.3.1 - contact list

# ✅ Add contacts
# define a function called 'add_contact'
# Get name, phone from the user
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")

    try:
        if len(name) == 0:
           raise ValueError('User must input a valid name.')

        if len(phone) == 0:
            raise ValueError('User must input a valid phone number.')

        with open('data/contacts.txt', mode='a') as f:
            f.write(f'{name}: {phone}\n')

        print(f'✅ {name} has been added to your contacts!')

    except ValueError as e:
        print(f'❌ Value Error: {e}')

    except Exception as e:
        print(f'❌ Error: {e}')


# View Contacts
# ✅ define the view contact funtion
# create the basic try/except block
# use 'with' to open the file with the correct mode to read
def view_contacts():
    try:
        with open('data/contacts.txt', 'r') as f:
            contacts = f.readlines()

            if not contacts:
                print('Your list is empty')
            else:
                for person in contacts:
                    print(person)

    except FileNotFoundError as e:
        print(f'❌ File Not Found: your path was not found')

    except Exception as e:
        print(f'❌ Error: {e}')

# Declare/defining a function called 'main', it should contain a while True: loop
def main():
    while True:
        # Program logic, asks user what step to take
        print('\n==== ☎️ Contact List Application ☎️ ====')
        print('1.   Add Contact.')
        print('2.   View Contacts.')
        print('3.   Quit.')

        # Get choice from user. All user input info is a string
        choice = input('Enter your choice: ')

        # Control Flow 'If' statement, to control what actions the program takes
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print('👋 Goodbye')
            break # Break you out of a loop. End your loop.
        else:
            print('❌ Invalid Choice. Please try again.')


# # Call the main function
# Only run this file automatically if it is the main file
if __name__ == '__main__':
    main()

# view contacts
# define the view contact function
# use 'with' to open the file with the correct mode to read
