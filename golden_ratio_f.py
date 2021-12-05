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
    b = 101  # верхняя граница поиска числа
    
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
