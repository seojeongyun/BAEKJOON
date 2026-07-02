'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120812
'''

from collections import defaultdict

def solution(array):
    counter = defaultdict(int)
    for i in array:
        counter[i] += 1

    most_val = max(list(counter.values()))
    saw = list(counter.values()).count(most_val)
    if saw > 1:
        return -1
    else:
        for k in counter.keys():
            if counter[k] == most_val:
                return k

'''
* 핵심 아이디어: 매 라운드마다 원소 하나씩 삭제, 가장 마지막에 살아남은 원소가 최빈값.
if i == 0: 조건이 마지막에 살아남은 원소인가? 를 묻는 조건이다.
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
    
'''