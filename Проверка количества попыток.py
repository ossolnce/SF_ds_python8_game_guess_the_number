import numpy as np
from numpy import random

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали списоконлайн переводчик чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    count = 0   # счетчик попыток
    prdict_number_min = 1  # нижняя граница поиска числа
    prdict_number_max = 101  # верхняя граница поиска числа
    
    while True:
        count+=1
        
        prdict_number = (prdict_number_max + prdict_number_min) // 2

        if number > prdict_number:
            prdict_number_min = prdict_number  # смещение нижней границы поиска числа

        elif number < prdict_number:
            prdict_number_max = prdict_number  # смещение верхней границы поиска числа

        else:
            break

    # Ваш код заканчивается здесь

    return count

print('Run benchmarking for game_core_v3: ', end='')

score_game(game_core_v3)