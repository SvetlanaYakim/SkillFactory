import numpy as np


def random_number() -> int:
    """Компьютер загадывает целое число от 1 до 100.
       Функция, справляется с угадыванием меньше чем за 20 попыток.

    Args:
        None

    Returns:
        int: Число попыток
    """
    count = 0
    mid, min, max = 0, 0, 100

    random_number = np.random.randint(1, 101)  # предполагаемое число

    while mid != random_number:
        mid = round(min + max)/2
        if mid > random_number:
            max = mid
        else:
            min = mid
        count += 1
    return count

def score_game(random_number) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_number ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали списоконлайн переводчик чисел

    for number in random_array:
        count_ls.append(random_number())

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
score_game(random_number)