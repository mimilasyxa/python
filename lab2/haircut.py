import datetime


clients = {"Фёдоров":
                [{'date': datetime.date(1993, 12, 12), 'service': "стрижка", 'cost': 400},
                 {'date': datetime.date(1994, 12, 12), 'service': "стрижка", 'cost': 200},
                 {'date': datetime.date(1995, 12, 21) , 'service': "окрашивание", 'cost': 500}],
           "Лофкес":
                [{'date': datetime.date(1991, 12, 21), 'service': "стрижка", 'cost': 500},
                 {'date': datetime.date(1996, 12, 21), 'service': "стрижка", 'cost': 600},
                 {'date': datetime.date(1998, 12, 21), 'service': "окрашивание", 'cost': 100}],
           "Лямкин":
                [{'date': datetime.date(1991, 12, 21), 'service': "стрижка", 'cost': 600},
                 {'date': datetime.date(1992, 12, 21), 'service': "стрижка", 'cost': 900},
                 {'date': datetime.date(1996, 12, 21), 'service': "окрашивание", 'cost': 1100}]}
clients_lastname = ["Фёдоров", "Лофкес", "Лямкин"]

def delete_client(lastname):
    del clients_lastname[clients_lastname.index(lastname):]
    del clients[lastname]
    
def add_client(lastname):
    clients[lastname] = []
    clients_lastname.append(lastname)
    
def add_service(lastname, date, service, cost):
    div_date = date.split(".")
    return clients[lastname].append({'date': datetime.date(int(div_date[0]), int(div_date[1]), int(div_date[2])), 'service': service, 'cost': cost})

def delete_service(lastname, service_number):
    del clients[lastname][service_number]

def find_latest_date(lastname):
    print(f"{lastname} был последний раз {clients[lastname][len(clients[lastname]) - 1]['date']}")

def oldest_client():
    date = 0
    for i in range(len(clients_lastname)):
        delta_date = (clients[clients_lastname[i]][len(clients[clients_lastname[i]]) - 1]["date"] - datetime.date(1991, 12, 21)).days
        if delta_date > date:
            date = delta_date
            name = clients_lastname[i]
    print(f"Последним клиентом был {name}")
            
        
def total_money_spent(lastname):
    sum = 0
    for i in range(len(clients[lastname])):
        sum += clients[lastname][i]["cost"]
    print(f"Клиент {lastname} за всё время потратил {sum} руб")

def find_rich_client():
    biggest_sum = 0
    for j in range(len(clients)):
        sum = 0
        for i in range(len(clients[clients_lastname[j]])):
            sum += clients[clients_lastname[j]][i]["cost"]
        if sum > biggest_sum:
            biggest_sum = sum
            richest_client = clients_lastname[j]
    print(f"Самым богатым клиентом является {richest_client}, потративший {biggest_sum} руб")

def find_commonest_client():
    number = 0
    for j in range(len(clients)):
        if len(clients[clients_lastname[j]]) > number:
            number = len(clients[clients_lastname[j]])
            client_name = clients_lastname[j]
    print(f"Самый частый клиент {client_name}")
            
while True:
    action = int(input("Что вы хотите сделать?\n 1) Добавить клиента\n 2) Удалить клиента\n \
3) Добавить услугу\n 4) Удалить услугу\n 5) Найти дату последнего обращения\n \
6) Узнать сколько всего потратил клиент\n 7) Найти самого давнего клиента\n 8) Найти самого богатого клиента\n 9) Найти самого частого клиента\n 0) Вывести список клиентов\n"))
    if action == 1:
        add_client(input("Введите фамилию клиента\n"))
    if action == 2:
        delete_client((input("Введите фамилию клиента\n")))
    if action == 3:
        add_service(input("Введите фамилию клиента\n"),input("Введите дату услуги\n"),input("Введите название услуги\n"),int(input("Введите стоимость услуги\n")))
    if action == 4:
        delete_service(input("Введите фамилию клиента\n"),int(input("Введите номер услуги\n"))- 1)
    if action == 5:
        find_latest_date(input("Введите фамилию клиента\n"))
    if action == 6:
        total_money_spent(input("Введите фамилию клиента\n"))
    if action == 7:
        oldest_client()
    if action == 8:
        find_rich_client()
    if action == 9:
        find_commonest_client()
    if action == 0:
        for key, value in clients.items():
          print("{0}: {1}".format(key,value))
