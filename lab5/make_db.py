import sqlite3

connect = sqlite3.connect("books.sqlite")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS books
                (id INTEGER primary key autoincrement,
                author varchar,
                title varchar,
                genre varchar)""")
def add_book(author, title, genre):
    cursor.execute(f"""INSERT INTO books (author, title, genre)
                VALUES ('{author}', '{title}', '{genre}')""")

for i in range(10):
    add_book(input("Автор"), input("Название"), input("Жанр"))
    connect.commit()
cursor.execute("""SELECT * FROM books""")
print(cursor.fetchall())
cursor.close()
