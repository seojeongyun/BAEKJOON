'''
    격자: N x M
    미로
        - 1: 이동할 수 있는 칸
        - 0: 이동할 수 없는 칸
    출발 지점
        - (1,1)
    도착 지점
        - (N,M)

    출력: 지나야하는 최소의 칸수

    * 칸을 셀 때는 시작 위치와 도착 위치도 포함
'''

# 알고리즘: BFS

import sys
from collections import deque

def print_status(map):
    for row in map:
        print(*row)

def in_range(i, j):
    return 0 <= i < N and 0 <= j < M

def bfs(i, j):
    # [0] DQ, VISITED 셋업
    DQ = deque()
    DQ.append([i, j])
    VISITED[i][j] = 1

    while DQ:
        ci, cj = DQ.popleft() # i, j pop

        # 네 방향, 미방문, 범위내
        for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
            ni, nj = ci+di, cj+dj
            if in_range(ni, nj) and MAP[ni][nj] == 1 and VISITED[ni][nj] == 0:
                DQ.append([ni, nj])
                #
                VISITED[ni][nj] = VISITED[ci][cj] + 1

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력 및 초기 데이터 구축
    N, M = map(int, input().rstrip().split())
    MAP = []
    for _ in range(N):
        lst = []
        ROW = input().rstrip()
        for num in ROW:
            lst.append(int(num))
        MAP.append(lst)

    VISITED = [[0] * M for _ in range(N)]
    #
    i, j = 0, 0

    # [1] BFS
    bfs(i, j)

    # [2] 출력
    print(VISITED[N-1][M-1])