import random


def binar_search(target, sort_list):
    left = 0
    right = len(sort_list) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if sort_list[middle] == target:
            return middle
        elif sort_list[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    raise ValueError("Value not in sort_list")


