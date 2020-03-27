import math


size = 100
avg_yeild = 20
all_avg_yeild = 2000
sum_yeild = 0
for i in range(1, 8, 1):
    size = math.floor(size * 1.05)
    avg_yeild = avg_yeild * 1.02
    all_avg_yeild = math.floor(size * avg_yeild)
    sum_yeild += all_avg_yeild
    print(f"За {i} год было собрано {all_avg_yeild} центнеров ячменя с {size} гектар")
print(f"Всего {sum_yeild} центнеров")
