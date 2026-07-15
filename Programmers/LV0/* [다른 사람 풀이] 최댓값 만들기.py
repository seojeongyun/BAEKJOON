'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120862/solution_groups?language=python3
    나: 가능한 모든 경우의 수 O(N^2)
    다른 풀이: Sort 이후 가장 작은 두 수의 곱과 가장 큰 두 수의 곱을 비교 O(NlogN)
'''

import sys

def solution(numbers):
    answer = -sys.maxsize
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer = max(numbers[i]*numbers[j], answer)
    return answer

'''
    def solution(numbers):
        numbers = sorted(numbers)
        return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 
'''