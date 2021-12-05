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
    a = 1  # нижняя граница поиска числа
    b = 101 # верхняя граница поиска числа
    
    while True:
        count+=1
        x1 = int(a + 0.382 * (b - a))
        x2 = int(b - 0.382 * (b - a))
        
            
        if number > x1:
            a = x1
        if number < x1:
            b = x1
        if number > x2:
            a = x2
        if number < x2:
            b = x2
            
        else:
            break

    # Ваш код заканчивается здесь

    return count

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)