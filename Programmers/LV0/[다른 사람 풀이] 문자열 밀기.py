'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120921
    [1] deque의 rotate
    [2] find 함수
'''

def solution(A, B):
    for i in range(len(A)):
        if A == B:
            return i
        A = A[-1]+A[:-1]
    return -1

'''
    [1] rotate
    from collections import deque

    def solution(A, B):
        a, b = deque(A), deque(B)
        for cnt in range(0, len(A)):
            if a == b:
                return cnt
            a.rotate(1)
        return -1
'''

'''
    [2] find 함수
    solution=lambda a,b:(b*2).find(a)
'''