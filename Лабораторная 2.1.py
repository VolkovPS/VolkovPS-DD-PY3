"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    min_current = arr[0]
    min_index = 0

    for i in range(0, len(arr)):
        if arr[i] < min_current:
            min_current = arr[i]
            min_index = i
        else:
            i += 1

    return min_index
