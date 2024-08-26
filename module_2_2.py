# Все ли равны?
first = input("Введите число: ")
second = input("Введите число: ")
third = input("Введите число: ")

if first == second == third:
    print(3) # Если все числа равны между собой, то вывести 3
    print(sqw)
    print(ds)
elif first == second or first == third or second == third:
    print(2) # Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
else:
    print(0) # Если равных чисел среди 3-х вообще нет, то вывести 0
