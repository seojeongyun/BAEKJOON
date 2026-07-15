'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120848
    [1] 팩토리얼 구하는 방법:재귀
'''


def factorial(i):
    if i == 1:
        return 1
    else:
        return i * factorial(i - 1)


def solution(n):
    answer = 0
    i = 1
    while True:
        if factorial(i) > n:
            answer = i - 1
            break
        i += 1
    return answer

'''
    나처럼 factorial값 구한 뒤 비교하면 resource 많이 사용
    아래처럼 구하면서 비교
    
    def solution(n):
        answer = 1
        factorial = 1
        while factorial <= n:
            answer += 1
            factorial = factorial * answer
        answer -= 1
        return answerㅍ
'''