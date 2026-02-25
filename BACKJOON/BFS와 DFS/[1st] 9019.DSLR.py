'''
    네 개의 명령어는 레지스터에 저장된 n을 변환
        - D: 2n 저장, 결과가 9,999보다 크면 n%10,000 저장
        - S: n-1을 저장, n=0이면 9,999가 저장됨
        - L: 왼쪽으로 rotate
        - R: 오른쪽으로 rotate

    레지스터
        - 0 <= n <= 10,000의 10진수 저장

    서로 다른 두 정수 A와 B
    A를 B로 바꾸는 최소한의 명령어 생성하는 프로그램

    * n의 자릿수로 0이 포함된 경우 주의
        1000 -- L --> 0001 = 1
        1000 -- R --> 0100 = 100
'''

import sys
import time
from collections import deque

# sys.setrecursionlimit(10**7)

def DSLR(func, A):
    if func == 'D':
        output = 2 * A if 2 * A < 10000 else 2 * A % 10000
        return output

    if func == 'S':
        output = A - 1 if A != 0 else 9999
        return output

    if func == 'L': # 1234 -> 2341
        return A % 1000 * 10 + A // 1000

    if func == 'R': # 1234 -> 4123
        return A // 10 + A % 10 * 1000

def bfs(A):
    q = deque()
    q.append([A, ''])
    v[A] = 1

    while q:
        num, cmd = q.popleft()
        if num == B:
            return cmd

        for func in ('D', 'S', 'L', 'R'):
            if func == 'D':
                output = 2 * num if 2 * num < 10000 else 2 * num % 10000

            if func == 'S':
                output = num - 1 if num != 0 else 9999

            if func == 'L':  # 1234 -> 2341
                output = num % 1000 * 10 + num // 1000

            if func == 'R':  # 1234 -> 4123
                output = num // 10 + num % 10 * 1000

            if not v[output]:
                v[output] = 1
                q.append([output, cmd + func])

        # for func in ('D', 'S', 'L', 'R'):
        #     if not v[DSLR(func, num)]:
        #         v[DSLR(func, num)] = 1
        #         q.append([DSLR(func, num), cmd + func])
    return -1

if __name__ == '__main__':
    input = sys.stdin.readline
    ANSW = []

    # [0] TC 입력
    T = int(input().rstrip())

    for _ in range(T):
        A, B = map(int, input().strip().split())
        v = [0] * 10001
        ANSW.append(bfs(A))

    for answ in ANSW:
        print(answ)

'''
1
1 16

1
1001 1000
'''

'''
    시간 복잡도: O(E) + O(V)
        E = 4
        V = 
'''