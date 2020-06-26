import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


form = cgi.FieldStorage()
n1 = form.getfirst("name_1", "не задано")
n2 = form.getfirst("name_2", "")
yl = form.getfirst("you_like", "")
#yl=[]
#yl = form.getlist("you_like")

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
n=n1+" "+n2
print("<p>добрый день, {}".format(n))
print("</p>")

#print(yl)

if yl=="choco":
	print("<p>мы знаем, что вам нравится шоколад </p>") 
if yl=="kookies": 
	print("<p>мы знаем, что вам нравится печенье </p>")
if yl=="icecream":
	print("<p>мы знаем, что вам нравится мороженное </p>")

print("""</main>
   <aside class="sidebar">
    
    </aside>

    <aside class="twin">
        
    </aside>
    <aside class="twin">
        
    </aside>

    <footer class="colophon grid">
        
    </footer>
</div>
</body>
        </html>""")