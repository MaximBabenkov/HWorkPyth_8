import csv

def add(i):
    with open('data.csv','a+',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)


def view():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)    
    return data

def delete(i):
    def save(j):
        with open('data.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)
            
    new_list = []
    telephone = i

    with open('data.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                if element == telephone:
                    new_list.remove(row)
    save(new_list)

def update(i):

    def update_newlist(j):
        with open('data.csv','w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)


    new_list = []
    telephone = i[0]

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == telephone:
                    surname = i[1]
                    name = i[2]
                    telephone = i[3]
                    description = i[4]
                    data = [surname,name,telephone,description]
                    index = new_list.index(row)
                    new_list[index] = data
    update_newlist(new_list)

def search(i):
    data = []
    telephone = i
    with open('data.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == telephone:
                    data.append(row)
    return data