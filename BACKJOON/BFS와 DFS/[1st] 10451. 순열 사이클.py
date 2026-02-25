'''
    순열을 표현할 수 있는 방법
        - 배열
            1 2 3 4 5 6 7 8
            3 2 7 8 1 4 5 6

        - 순열 사이클 (문제지 Figure 1 참고)
            1 3 5 7
            2
            4 8 6

    출력: N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수 구하기
'''

import sys

def DFS(start):
    VISITED[start] = 1
    next = PERM[start-1]

    if VISITED[next] == 0:
        DFS(next)

if __name__ == '__main__':
    input = sys.stdin.readline
    ANSW_LST = []
    # [0] TC 입력
    T = int(input().rstrip())

    # [1] TC 반복
    for _ in range(T):
        ANSW = 0

        # [2] 정수, 수열 입력
        N = int(input().rstrip())
        PERM = list(map(int, input().rstrip().split()))

        # DFS
        VISITED = [0] * (N+1)
        for i in range(1, N+1):
            if VISITED[i] == 0:
                DFS(i)
                ANSW += 1

        ANSW_LST.append(ANSW)

    for answ in ANSW_LST:
        print(answ)


