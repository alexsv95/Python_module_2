# Задание "Слишком древний шифр":
from operator import concat
from os.path import split

numbers_key = {}

for i in range(3, 21):
    for j in range(1, i):
        for k in range(1, i):
            if (j + k) % i == 0:
                if j >= k:
                    continue
                print(f'{i} - {j}{k}')