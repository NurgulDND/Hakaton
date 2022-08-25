import json

FILE_CARS = 'data.json'

def listing():
    with open(FILE_CARS) as file:
        return json.load(file)


def retrieve():
    data = listing()
    id = int(input('Enter ID: '))
    one_car = list(filter(lambda x: x['id'] == id, data))
    if one_car:
        return one_car[0]
    else:
        return "Not such car!"


def get_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
        id += 1
    with open('id.txt', 'w') as file:
        file.write(str(id))
    return id


def create_data():
    data = listing()
    CARS = {
        'id': get_id(),
        'marka': input('Enter mark of car: '),
        'model': input('Enter model of car: '),
        'years': int(input('Enter date of established: ')),
        'description': input('Enter description: '),
        'price': float(input('Enter price: '))
    }
    data.append(CARS)
    with open(FILE_CARS, 'w') as file:
        json.dump(data, file)
    return 'CREATED'
    print(listing())

def update_data():
    data = listing()
    flag = False
    id = int(input('Enter id: '))
    car = list(filter(lambda x: x['id'] == id, data))

    if not id:
        return 'Not such car'
    index_ = data.index(car[0])
    choice = input('What would u like change: 1 - marka, 2 - model, 3 - years, 4 - description, 5 - price?')
    if choice == '1': 
        data[index_]['marka'] = input('Enter new mark of car: ')
        flag = True
    elif choice == '2':
        data[index_]['model'] = (input('Enter new model of car: '))
        flag = True
    elif choice == '3':
        data[index_]['years'] = int(input('Enter new date of car: '))
        flag = True
    elif choice == '4':
        data[index_]['description'] = (input('Enter new description of car: '))
        flag = True
    elif choice == '5':
        data[index_]['price'] = float(input('Enter new price of car: '))
        flag = True
    else:
        print('Not such line!')
    
    with open(FILE_CARS, 'w') as file:
        json.dump(data, file)    

    if flag:
        return 'UPDATED'
    else:
        return "NO CHANGES"


def delete_data():
    data = listing()
    id = int(input('Enter ID: '))
    car = list(filter(lambda x: x['id'] == id, data))

    if not car:
        return "Not such car!"
    
    index_ = data.index(car[0])
    data.pop(index_)
    json.dump(data, open(FILE_CARS, 'w'))
    return 'DELETED'





