'''
    방향 없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하시오.
'''

import sys
from collections import deque

sys.setrecursionlimit(10**7)

def print_map(MAP):
    for row in MAP:
        print(*row)

def DFS(start):
    V[start] = 1

    for next in range(1, N+1):
        if V[next] == 0 and GRAPH[start][next] == 1:
            V[next] = 1
            DFS(next)

def BFS(start):
    DQ = deque()
    DQ.append(start)
    V[start] = 1

    while DQ:
        c = DQ.popleft()
        for next in range(1, N+1):
            if V[next] == 0 and GRAPH[c][next] == 1:
                V[next] = 1
                DQ.append(next)

def search():
    global ANSW

    # 순회
    for i in range(1,N+1):
        if V[i] == 0:
            ANSW += 1
            DFS(i)

    return ANSW


if __name__ == '__main__':
    input = sys.stdin.readline
    ANSW = 0

    # [0] 입력
    N, M = map(int, input().rstrip().split())
    GRAPH = [[0] * (N + 1) for _ in range(N + 1)]
    GRAPH_DBG = [[0] * (N + 1) for _ in range(N + 1)]
    V = [0] * (N+1)

    for _ in range(M):
        X, Y = map(int, input().rstrip().split())
        GRAPH[X][Y] = 1
        GRAPH[Y][X] = 1

    # [1] 순회
    ANSW = search()

    print(ANSW)
