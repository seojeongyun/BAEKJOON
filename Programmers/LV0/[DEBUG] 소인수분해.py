'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120852

'''


def solution(n):
    answer = []
    div = 2

    while True:
        if n == 1 * div:
            answer.append(div)
            break
        if n % div == 0:
            answer.append(div)
            n = n // div
        else:
            div += 1

    lst = set(answer)
    return sorted(lst)

solution(72)