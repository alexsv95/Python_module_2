# Задача "Всё не так уж просто":

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,46]
primes = [] # список для простых чисел
not_primes = [] # список для не простых чисел

# Ver 1.1
for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2,i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print("Простые числа:", primes)
print("Не простые числа:", not_primes)


# Ver 1.0
# for i in range(len(numbers)):
#     dividers = [] # Создание списка, в который будем записывать все делите на число без остатка
#     if numbers[i] == 1:
#         continue
#     for j in range(1,numbers[i]+1):
#         if numbers[i] % j == 0: # Деление элемента из списка numbers на все значения от 1 до самого значения из спсика
#             dividers.append(j) # Запись делителей без остатка в список dividers
#     if len(dividers) == 2: # Проверка кол-во добавленных значений в список из цикла выше, если всего 2 значения в списке, значит это простое число
#         primes.append(numbers[i])
#     else:
#         not_primes.append(numbers[i])
#
# print("Простые числа:", primes)
# print("Не простые числа:", not_primes)





# for i in range(len(numbers)):
#     for j in range(1,max(numbers)+1):
#         if numbers[i] % j == 0:
#             print(j)
#     print(i)

# for i in range(len(numbers)):
#     for j in range(1,16):
#         if numbers[i] % j == 0:
#             count += 1
#             primes.append(numbers[i])
#         else:
#             not_primes.append(numbers[i])
# print("primes ",primes)
# print(not_primes)


# for i in range(len(numbers)):
#     for j in (1,16):
#         if numbers[i] % j:
#             primes.append(i)
#         else:
#             not_primes.append(i)
# print(primes)
# print(not_primes)
