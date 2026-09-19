# Event Handling Application
import datetime
# 

# add_event
def add_event():
    # Input that asks the name of the event
    event_name = input('enter the event name: ')
    # input that asks the date (YYY-MM-DD)
    date_input = input('enter the event date (YYYY-MM-DD): ')

    try:
        event_date = datetime.datetime.strftime(date_input, '%Y-%m-%d')
        print(event_date)
    except ValueError as e:
        print('Invalide Date Formate. Please use YYYY-MM-DD')
        return
# list_event
def list_events():
    print('list events')
    
# quite application
# prompt the user for input
def main():
    while True:
        print('\nEvent Management System')
        print('1. Add Event')
        print('2. List Events')
        print('3. Quite')

        choice = input('Enter your choice: ')

        if choice == '1':
            print('Add event')
        elif choice == '2':
            print('list events')
        elif choice == '3':
            print('Goodbye')
            break
        else:
            print('invalid choice. Choose again.')
            

if __name__ == '__main__':
    main()