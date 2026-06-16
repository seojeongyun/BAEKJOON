'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120814
'''

import sys

def solution(n):
    answer = int(n//7)+1 if n%7 != 0 else int(n/7)
    return answer

for i in range(1,101):
    print(i, solution(i))