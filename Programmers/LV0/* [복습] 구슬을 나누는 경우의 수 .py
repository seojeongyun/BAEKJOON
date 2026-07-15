'''
https://school.programmers.co.kr/learn/courses/30/lessons/120840
'''

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def solution(balls, share):
    answer = factorial(balls) / (factorial(share) * factorial(balls-share))
    return answer

'''
    처음에 재귀로 풀었는데 재귀 반복 회수 때문에 런타임 에러 발생하여 포문으로 변경
    import sys
    sys.setrecursionlimit(10**6)
    
    def factorial(i):
        if i == 1:
            return 1
        else:
            return i * factorial(i - 1)
        
    def solution(balls, share):
        answer = factorial(balls) / (factorial(share) * factorial(balls-share))
        return answer
'''