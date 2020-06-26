import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


form = cgi.FieldStorage()
name = form.getfirst("name", "не задано")
lastname = form.getfirst("lastname", "")
login = form.getfirst("login", "")
password = form.getfirst("password","")
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
print(f"""<p>Поздравляем {lastname} {name}, вы успешно прошли регистрацию под логином {login}</p>""")
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