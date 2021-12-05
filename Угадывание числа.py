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