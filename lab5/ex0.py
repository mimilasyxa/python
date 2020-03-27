import sqlite3

connect = sqlite3.connect("books.sqlite")
cursor = connect.cursor()

def add_book(author, title, genre):
    cursor.execute(f"""INSERT INTO books (author, title, genre)
                VALUES ('{author}', '{title}', '{genre}')""")

def delete_book(row, value):
    cursor.execute(f"""DELETE FROM books WHERE {row} == {value}""")

def show_authors_books(author):
    cursor.execute(f"""SELECT * FROM books WHERE author == {author}""")
    print(cursor.fetchall())

def show_n_books(number):
    cursor.execute(f"""SELECT * FROM books LIMIT {number}""")
    print(cursor.fetchall())

def update_row(row, old_value, new_value):
    cursor.execute(f"""UPDATE books SET {row} == {new_value} WHERE {row} == {old_value}""")

while True:
    action = int(input("""Что вы хотите сделать?
1) Добавить книгу
2) Удалить книгу
3) Показать все книги автора
4) Показать первые N книг
5) Обновить одно из значений книги
"""))
    if action == 1:
        add_book(input("Имя автора\n"), input("Название книги\n"), input("Жанр\n"))
    if action == 2:
        delete_book(input("Введите ряд по которому будет удаляться книга (uthor, title, genre)\n"), input("Введите значение этого ряда\n"))
    if action == 3:
        show_authors_books(input("Введите автора"))
    if action == 4:
        show_n_books(input("Введите количество книг которое нужно показать\n"))
    if action == 5:
        update_row(input("Введите ряд по которому будет обновляться книга\n", input("Ввведите старое значение ряда\n"), input("Введите новое значение ряда\n")))
    if action == 0:
        break
    connect.commit()
