from insertion_sort import insertion_sort
from merge_sort import merge


def tim_sort(numbers):
    if len(numbers) <= 32:
        return insertion_sort(numbers)
    else:
        mid_index = len(numbers)//2
        left_part = numbers[:mid_index]
        right_part = numbers[mid_index:]
        sorted_left_part = tim_sort(left_part)
        sorted_right_part = tim_sort(right_part)
        result = merge(sorted_left_part, sorted_right_part)
        return result


if __name__ == '__main__':
    import random
    import time
    numbers = random.choices(range(100000), k=8192)  # 可以數字大一點，多測幾次

    start_time = time.time()
    result = tim_sort(numbers)
    print("Timsort: ", time.time() - start_time)
    assert result == sorted(numbers), print('Wrong answer!!!')
    print("Success!!")
