'''
    https://www.acmicpc.net/problem/11728

    1.5 / 256

    정렬되어 있는 두 배열 A, B
    배열을 합친 후 정렬해서 출력

    입력:
        첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M (1 ≤ N, M ≤ 1,000,000)
        둘째 줄에는 배열 A의 내용
        셋째 줄에는 배열 B의 내용

    출력:
        첫째 줄에 두 배열을 합친 후 정렬한 결과
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))

    # [1] 풀이 1. sort
    # answ = A+B
    # answ.sort()

    # [2] 풀이 2. 투포인터
    answ = []
    a = 0
    b = 0
    while a != len(A) or b != len(B):
        if a == len(A):
            answ.append(B[b])
            b += 1

        elif b == len(B):
            answ.append(A[a])
            a += 1

        else:
            if A[a] < B[b]:
                answ.append(A[a])
                a += 1
            else:
                answ.append(B[b])
                b += 1

    print(*answ)
