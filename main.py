from views import *

print(f'1 - CREATE, 2 - LISTING, 3 - RETRIEVE, 4 - UPDATE, 5 - DELETE')
choice = input('Enter num of operation: 1, 2, 3, 4, 5: ')


def main():

    if choice == '1':
        print(create_data())
    elif choice == '2':
        print(listing())
    elif choice == '3':
        print(retrieve())
    elif choice == '4':
        print(update_data())
    elif choice == '5':
        print(delete_data())
    else:
        print('Not such operation!')

main()
