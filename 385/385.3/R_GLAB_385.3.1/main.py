# R_GLAB_385.3.1 - contact list

# add contacts
# define a function called 'add_contact'
# get name, phone from the user
def add_contact():
    name = input('Enter contact name: ')
    phone = input('Enter contact phone: ')
    try:
        if len(name) == 0:
            raise ValueError('user must input a valid name.')
        if len(phone) == 0:
            raise ValueError('user must input a valid phone number.')
        with open('data/contacts.txt', mode='a') as f:
            f.write(f'{name}:{phone}\n')
            print(f'{name} has been added to your contacts!')
    except Exception as e:
        print(f'Error: {e}')

# view contacts
# quite out of application

# we use error handling, while loop python
# declare/defining a function called 'main', it should contain a while true: loop

def main():
    while True:
        # program logic
        print('==== Contact List Application ====')
        print('1. Add Contact')
        print('2. View Contacts')
        print('3. Quit')
        choice = input('Enter your choice: ')
        # control flow 'if' statement to control what actions the program takes
        if choice == '1':
            add_contact()
        elif choice == '2':
            print('view_contacts')
        elif choice == '3':
            print('goodbye.')
            break  # break out of the while loop and end your loop.
        else:
            print('Invalid choice. Please try again.')

# call the main function
# only run this file automatically if it is the main file
if __name__ == '__main__':
    main()

# view contacts
# define the view contact function
# use 'with' to open the file with the correct mode to read
