print("""Здравствуйте!
Данная программа предназначена для определения того, является
ли год високосным""")#Выводим приветствие и предназначение программы
num = int(input("Введите число, которое определяет год:"))#Команда для ввода переменной
if ((num%4 == 0) and (num%100 !=0)) or (num%400 == 0):
    year = "LEAP"#вводим новую переменную и присваиваем её соответственное значение
else:#В других случаях год не високосный
    year = "COMMON"#вводим новую переменную и присваиваем её соответственное значение
print(year)#вывод результатa
print(input("Нажмите клавишу \"Enter\" для окончания работы программы"))#Команда для окончания программы
