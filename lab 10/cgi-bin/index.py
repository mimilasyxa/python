import cgi
import sys
import codecs
import sqlite3


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
form = cgi.FieldStorage()
genre = form.getfirst("genre", "none")
search_btn = form.getfirst("btn", "none")


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
<title>Обработка форм</title>
<meta charset="utf-8">
<link rel="stylesheet" href="/L7.css">
</head>
<body>
<div class="site">
    <header class="masthead">
        <h2 class="site-title">Результат обработки</h2>
    </header>
    <main id="content" class="main-content">
	""") 

conn = sqlite3.connect("books.sqlite")
c = conn.cursor()
print("<h3>Список книг</h3>")

if genre == "none":
    c.execute('SELECT * FROM books')
else:
    c.execute(f"SELECT * FROM books WHERE LOWER(genre) LIKE LOWER('%{genre}%')")
if search_btn == "expanded":
    name = form.getfirst("name", "")
    author = form.getfirst("author", "")
    genre_b = form.getfirst("genre", "")
    c.execute(f"SELECT * FROM books WHERE title LIKE ('%{name}%') AND author LIKE ('%{author}%') AND genre LIKE ('%{genre_b}%')")
if search_btn == "delete":
    name = form.getfirst("name", "")
    author = form.getfirst("author", "")
    genre_b = form.getfirst("genre", "")
    c.execute(f"DELETE FROM books WHERE title = '{name}' AND author='{author}' AND genre='{genre_b}'")
if search_btn == "add":
    name = form.getfirst("name", "")
    author = form.getfirst("author", "")
    genre_b = form.getfirst("genre", "")
    c.execute(f"""INSERT INTO books (author, title, genre)
                VALUES ('{author}', '{name}', '{genre}')""")
conn.commit()

row = c.fetchone()
print("<form action='../cgi-bin/book_page.py'>")
print("<ol>")
while row is not None:
	print("<li> "+row[1]+" "+row[2]+" "+row[3] + "<button name='book_name' type='submit' value="+  row[2] +">Страница книги</button>")
	row = c.fetchone()
print("</ol>")
print("</form>")
print("""</main>
   <aside class="sidebar">
       <form action="/cgi-bin/index.py">
       <button type="submit" name="genre" value="none">Все книги</button>
       <button type="submit" name="genre" value="Ужасы">Ужасы</button>
       <button type="submit" name="genre" value="классика">Классика</button>
       <button type="submit" name="genre" value="фэнтези">Фэнтези</button>
       <button type="submit" name="genre" value="приключения">Приключения</button>
       <button type="submit" name="genre" value="Историческая">История</button>
       </form>
       <button class="search">Дополнительное меню</button>
       <form class="hide form_search" action="../cgi-bin/index.py">
       <input name = "name" placeholder="Название">
       <input name = "author" placeholder="Автор">
       <input name = "genre" placeholder="Жанр">
       <button type="submit" name = "btn" value="expanded">Поиск</button>
       <button type="submit" name = "btn" value="delete">Удалить</button>
       <button type="submit" name = "btn" value="add">Добавить</button>
       *Все поля должны быть заполнены только при удалении
       </form>
    </aside>

    <aside class="twin">
    </aside>

    <aside class="twin">
    </aside>

    <footer class="colophon grid">
    </footer>
</div>
<script src="../js/index.js"></script>
</body>
        </html>""")


