def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[0]
        left_part = list()
        right_part = list()
        for num in numbers[1:]:
            if num < pivot:
                left_part.append(num)
            else:
                right_part.append(num)
        print(f"{left_part} [{pivot}] {right_part}")
        return quick_sort(left_part) + [pivot] + quick_sort(right_part)


if __name__ == "__main__":
    numbers = [50, 90, 70, 20, 10, 30, 40, 60, 80]
    quick_sort(numbers)
