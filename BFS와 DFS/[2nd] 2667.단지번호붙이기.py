'''
    # 미생물 연구에서 처럼 BFS로 군집 분류

    격자: N x N
        - 1 = 집
        - 0 = 빈 곳

    단지: 상하좌우로 집이 연결 되어 있다.

    출력:
        - 첫 번째 줄엔 단지의 수
        - 각 단지 내 집의 수를 오름차순으로 정렬하여 한 줄에 하나 씩
'''

import sys
from collections import deque

sys.setrecursionlimit(10**6)

def print_map(map):
    for row in map:
        print(*row)

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

def bfs(i, j):
    houses = 1
    DQ = deque()
    DQ.append((i, j))
    V[i][j] = 1

    while DQ:
        ci, cj = DQ.popleft()
        for dir in range(4):
            ni, nj = ci + di[dir], cj + dj[dir]
            if in_range(ni, nj) and V[ni][nj] == 0 and MAP[ni][nj] == 1:
                DQ.append((ni, nj))
                V[ni][nj] = V[i][j] + 1
                houses += 1

    return houses

def dfs(i, j):
    houses = 1
    V[i][j] = 1
    ci, cj = i, j

    for dir in range(4):
        ni, nj = ci + di[dir], cj + dj[dir]
        if in_range(ni, nj) and V[ni][nj] == 0 and MAP[ni][nj] == 1:
            V[ni][nj] = 1
            houses += dfs(ni, nj)

    return houses

def search():
    # [1: MAP 순회하면서 미방문 지점부터 bfs 적용]
    for i in range(N):
        for j in range(N):
            if V[i][j] == 0 and MAP[i][j] == 1:
                houses = dfs(i, j)
                if houses > 0:
                    ANSW.append(houses)

if __name__ == '__main__':
    input = sys.stdin.readline
    ANSW = []

    # [0] 입력
    N = int(input().rstrip())
    MAP = [[0 for _ in range(N)] for _ in range(N)]

    for row in range(N):
        ROW = input().rstrip()
        for col in range(len(ROW)):
            if ROW[col] == '1':
                MAP[row][col] = 1

    # [1] BFS
    V = [[0 for _ in range(N)] for _ in range(N)]
    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

    search()

    ANSW.sort()
    print(len(ANSW))
    for answ in ANSW:
        print(answ)