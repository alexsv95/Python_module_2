def get_matrix(n, m, value):
    matrix = [] # создание пустого списка matrix внутри функции
    list_value = [] # Создание списка, в который будут добавляться значения value
    for i in range(m):
        list_value.append(value) # Добавление значения value в список list_value m раз
    for j in range(n):
        matrix.append(list_value) # Добавление списка list_value в список matrix n раз
    return matrix # Возврат списка matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)