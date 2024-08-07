import csv 


def add(data):
    with open('data.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def view():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def delete(key):
    updated_data = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            updated_data.append(row)
            for element in row:
                if element == key:
                    updated_data.remove(row)
    
    with open('data.csv','w+', newline='\n') as file:
        writer = csv.writer(file)
        for row in updated_data:
            writer.writerow(row)
            

def update(data):
    new_list = []
    new_data = []
    key = data[0]
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == key:
                    index = new_list.index(row)
                    name = data[1]
                    gender = data[2]
                    telephone = data[3]
                    email = data[4]
                    new_data = [name, gender, telephone, email]
                    new_list[index] = new_data

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in new_list:
            writer.writerow(row)


def search(key):
    list = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == key:
                    list.append(row)
    return list