'''
    https://www.acmicpc.net/problem/1920

    1 / 128

    N개의 정수에 대해 X라는 정수가 존재하는지 알아내는 프로그램 작성

    입력
        N(1 ≤ N ≤ 100,000)
        N개의 정수 A[1], A[2], …, A[N]
        다음 줄에는 M(1 ≤ M ≤ 100,000)
        다음 줄에는 M개의 수
            M개의 수가 A안에 존재하는지 알아내면 된다.
'''

import sys
from collections import defaultdict

if __name__ == '__main__':
    input = sys.stdin.readline
    num_counter = defaultdict(int)
    answ = []

    # [0] 입력
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    M = int(input().strip())
    B = list(map(int, input().strip().split()))

    # [1] 숫자 카운트
    for a in A:
        num_counter[a] += 1

    # [2] 정답 처리
    for b in B:
        if num_counter[b]:
            answ.append(1)
        else:
            answ.append(0)


    # [3] 출력
    for val in answ:
        print(val)

'''
    TC 1
    1
    0
    1
    0
    
    0
    
    TC 2
    3
    1 1 2
    3
    2 3 4
    
'''