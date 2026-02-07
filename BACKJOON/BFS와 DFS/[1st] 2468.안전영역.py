'''
    격자: N x N
        - 각 cell 별로 값을 가짐
        - 주어진 값보다 작은 값을 갖는 cell은 deactive

    출력: active 군집의 최대 개수(값을 self로 바꿔가면서 test해야 하나봄)
'''

import sys
from collections import deque

def print_map(map):
    for row in map:
        print(*row)

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

def bfs(i, j):
    global height

    DQ = deque()
    DQ.append((i,j))

    while DQ:
        ci, cj = DQ.popleft()
        for di, dj in ((1,0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci+di, cj+dj
            if in_range(ni, nj) and V[ni][nj] == 0 and MAP[ni][nj] > height:
                DQ.append((ni, nj))
                V[ni][nj] = 1

if __name__ == '__main__':
    input = sys.stdin.readline
    ANSW_LST = []

    # [0] 입력
    N = int(input().rstrip())
    MAP = [list(map(int, input().rstrip().split())) for _ in range(N)]
    height = 0
    max_height = 0

    for row in MAP:
        max_height = max(max_height, max(row))

    while height <= max_height:
        ANSW = 0
        V = [[0] * N for _ in range(N)]

        # [1] deactive 지역에 대해서 V = 1로 마킹
        for i in range(N):
            for j in range(N):
                if MAP[i][j] <= height:
                    V[i][j] = 1

        # [2] BFS로 군집 개수 확인
        for i in range(N):
            for j in range(N):
                if V[i][j] == 0:
                    V[i][j] = 1
                    bfs(i,j)
                    ANSW += 1

        ANSW_LST.append(ANSW)
        height += 1

    print(max(ANSW_LST))