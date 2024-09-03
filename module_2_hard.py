# Задание "Слишком древний шифр":


def password_selection(n): # Создание функции
    if n < 3 or n > 20: # Проверка полученного значения в функцию
        print("Необходимо ввести значение от 3 до 20")
    else:
        for i in range(n, n+1): # Записываем в i число n
            pair_numbers = [] # Создаем временный список, в который будем добавлять все уникальные пары для числа n
            for j in range(1, i):
                for k in range(1, i):
                    if i % (j + k) == 0:
                        if j >= k:
                            continue
                        pair_numbers.append(str(j))
                        pair_numbers.append(str(k))
            return pair_numbers


number = int(input('Введите число от 3 до 20: '))
result = password_selection(number)

if result == None:
    print()
else:
    print('Пароль для числа',number, '-', "".join(result))