# CJ version 1
what = input ("Укажите действие (+, -): ")

a = float (input("Введи первое число: "))
b = float (input ("Введи второе число: "))

if what == "+":
        с = a + b 
        print ("Результат: " +str(c))
elif what == "-": 
        c = a -  b
        print ("Результат: " +str(c))
else: 
              print ("Выбрана неверная операция")
