'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120909

    제곱수 판별하기

    float_type.is_integer()
'''

import math

def solution(n):
    return 1 if int(math.sqrt(n)) ** 2 == n else 2

'''
다른 사람 풀이
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2
    
def solution(n):
    if n**(1/2) == int(n**(1/2)) :
        return 1
    else :
        return 2
'''