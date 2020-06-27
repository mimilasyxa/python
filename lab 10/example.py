import sqlite3

conn = sqlite3.connect(r"books.sqlite")
c = conn.cursor()
print("<h3>Список книг</h3>")
c.execute('SELECT * FROM books')
row = c.fetchone()
print("<ol>")
while row is not None:
	print("<li> "+row[1]+" "+row[2]+" "+row[3])
	row = c.fetchone()
