import cgi
import sys
import codecs
import sqlite3


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

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

conn = sqlite3.connect(r"books.sqlite")
c = conn.cursor()
print("<h3>Список книг</h3>")
c.execute('SELECT * FROM books')
row = c.fetchone()
print("<ol>")
while row is not None:
	print("<li> "+row[1]+" "+row[2]+" "+row[3])
	row = c.fetchone()
print("</ol>")
print("""</main>
   <aside class="sidebar">
    </aside>
    <form action="/cgi-bin/index.py"
    <button type="submit></form>

    <aside class="twin">
    </aside>

    <aside class="twin">
    </aside>

    <footer class="colophon grid">
    </footer>
</div>
</body>
        </html>""")
