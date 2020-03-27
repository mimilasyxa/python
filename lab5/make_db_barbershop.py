import sqlite3

connect = sqlite3.connect("barbershop.sqlite")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS barbershop
                (id INTEGER primary key autoincrement,
                name varchar,
                service varchar,
                cost int)""")
def add_book(name, service, cost):
    cursor.execute(f"""INSERT INTO barbershop (name, service, cost)
                VALUES ('{name}', '{service}', '{cost}')""")

for i in range(4):
    add_book(input("Фамилия клиента\n"), input("Название услуги\n"), int(input("Цена услуги")))
    connect.commit()
cursor.execute("""SELECT * FROM barbershop""")
print(cursor.fetchall())
cursor.close()
