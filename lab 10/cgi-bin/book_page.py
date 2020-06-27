import cgi
import sys
import codecs
import sqlite3


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
form = cgi.FieldStorage()
name = form.getfirst("book_name", "none")
conn = sqlite3.connect(r"books.sqlite")
c = conn.cursor()
c.execute(f"SELECT * FROM books WHERE LOWER(title) LIKE LOWER('%{name}%')")

row = c.fetchone()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../style/style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Информация о книге</title>
</head>
<body>
<body>
    <div class="container">
        <div class="content">
<div class="item">
                <div class="picture">
                    <img src="../files/no_image.jpg">
                </div>""")
print("""<div class="description">""")
print("Тут должно было быть описание, но вместо этого вот номер этой книги в базе данных - " + str(row[0]))
print("""</div>
                <div class="buyout_menu">
                    <div class="name">""")
print("Название: <l>"+ row[2] +"</l>")
print("""</div>
					 <div class="author">""")
print("Автор: <l>"+ row[1] +"</l>")
print("""</div>
					 <div class="author">""")
print("Жанр: <l>"+ row[3] +"</l>")
print("""</div>

                    <button>Купить</button>
                </div>
            </div>            </div>
        </div>
    <script src="js/login.js"></script>
    <script src="js/shop.js"></script>
</body>
</html>
""") 


