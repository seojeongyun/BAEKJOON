'''
    그래프 탐색
        - 정점 (1 ~ N) 번호가 작은 것을 먼저 방문
            - DFS 탐색 결과 출력
            - BFS 탐색 결과 출력
'''

import sys
from collections import deque

def print_graph(graph):
    for row in graph:
        print(*row)

def DFS(start):
    DFS_ANSWER.append(start)
    VISITED[start] = 1

    for next in range(N+1):
        if GRAPH[start][next] and VISITED[next] == 0:
            DFS(next)

def BFS():
    DQ = deque([V])
    VISITED[V] = 1

    # 종료조건: DQ가 없을 때
    while DQ:
        curr = DQ.popleft()
        BFS_ANSWER.append(curr)
        for next in range(N+1):
            if GRAPH[curr][next] and VISITED[next] == 0:
                DQ.append(next)
                VISITED[next] = 1

if __name__ == '__main__':
    input = sys.stdin.readline
    DFS_ANSWER = []
    BFS_ANSWER = []
    #
    # [0] 입력
    LST = []
    N, M, V = map(int, input().rstrip().split())
    for _ in range(M):
        X, Y = map(int, input().rstrip().split())
        LST.append([X,Y])

    # [1] DFS
    GRAPH = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for lst in LST:
        x, y = lst[0], lst[1]
        GRAPH[y][x] = 1
        GRAPH[x][y] = 1

    VISITED = [0 for _ in range(N+1)]

    DFS(V)

    # [2] BFS
    VISITED = [0 for _ in range(N + 1)]
    BFS()

    for answ in [DFS_ANSWER, BFS_ANSWER]:
        print(*answ)