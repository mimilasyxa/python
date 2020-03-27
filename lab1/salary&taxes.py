percent = 10
input_salary = open("salary.txt", "r")
output_salary = open("salary_after_taxes.txt", 'w')
for money in input_salary:
    salary = int(money)
    salary += salary * (percent / 100)
    taxes_ret = salary * 0.06
    taxes_fin = (salary - 12130 - taxes_ret) * 0.13
    taxes_prof = salary * 0.01
    award = salary * (percent / 100)
    salary = salary - (taxes_ret + taxes_fin + taxes_prof) 
    output_salary.write(f"""при окладе {int(money)} после вычета налогов получится {salary}\n""")
    print(salary)
input_salary.close()
output_salary.close()

