def insertion_sort(numbers):
    answer = list()
    for new in numbers:
        if answer:  # 不是空的
            is_insert = False
            for index, num in enumerate(answer):  # enumerate 同時給你編號跟對應編號的值
                if new < num:
                    is_insert = True
                    answer = answer[:index] + [new] + answer[index:]
                    break
            if not is_insert:
                answer = answer + [new]
        else:  # 第一張牌
            answer = [new]
    return answer


if __name__ == '__main__':
    numbers = [40, 30, 50, 60, 20]
    answer = insertion_sort(numbers)
    print(answer)

# answer = [30, 40, 50, 60]
# new = 20
# if answer:  # 不是空的
#     is_insert = False
#     for index, num in enumerate(answer):  # enumerate 同時給你編號跟對應編號的值
#         if new < num:
#             is_insert = True
#             answer = answer[:index] + [new] + answer[index:]
#             break
#     if not is_insert:
#         answer = answer + [new]
# else:
#     answer = [new]
# print(answer)
