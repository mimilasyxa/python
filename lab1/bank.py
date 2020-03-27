import math


money = int(input("Введите количество денег\n"))
credit_percent = float(input("Введите процент вклада\n"))
months = int(input("На сколько месяцев?\n"))
for i in range(months):
    money = math.floor(money * ( 1 + credit_percent / 100))
print(f"За {months} месяца(-ев) с процентом {credit_percent}  на счету будет {money} руб.")

