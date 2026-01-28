# '''
# -DFS 탐색
#     -우선순위(정점 번호 작은 것)
#     -방문 불가(종료)
# -초기화
# -BFS 탐색
#     -우선순위(정점 번호 작은 것)
#     -방문 불가(종료)
# '''
#
# def DFS(curr):
#     print(curr, end=' ')
#     for next in range(len(A)):
#         if A[curr][next] == 1 and visited[next] is None:
#             visited[next] = True
#             DFS(next)
#
# def BFS():
#     while (len(FIFO) > 0):
#         curr = FIFO.pop(0)
#         print(curr, end=' ')
#         visited[curr] = True
#         #
#         for next in range(len(A)):
#             if A[curr][next] == 1 and visited[next] is None:
#                 visited[next] = True
#                 FIFO.append(next)
#
# if __name__ == '__main__':
#     global A
#     global FIFO
#     #
#     N, M, V = map(int, input().split())
#     A = [[None] * (N+1) for _ in range(N+1)]
#
#     for _ in range(M):
#         x, y = map(int, input().split())
#         A[x][y] = 1
#         A[y][x] = 1
#
#     visited = [None for _ in range(N+1)]
#     visited[V] = True
#     DFS(V)
#     #
#     #
#     print()
#     visited = [None for _ in range(N+1)]
#     #
#     #
#     FIFO = [V]
#     BFS()

def DFS(start):
    visited[start] = 1
    DFS_answ.append(start)
    for next in range(1, N+1):
        if arr[start][next] == 1 and visited[next] == 0:
            # visited[next] = 1
            DFS(next)

def BFS(start):
    Q = []
    Q.append(start)
    visited[start] = 1
    while Q:
        curr = Q.pop(0)
        BFS_answ.append(curr)
        for next in range(1, N+1):
            if arr[curr][next] == 1 and visited[next] == 0:
                visited[next] = 1
                Q.append(next)


if __name__ == '__main__':
    N, M, V = list(map(int, input().split()))
    data = [list(map(int, input().split())) for _ in range(M)]

    arr = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)

    for i, j in data:
        arr[i][j] = 1
        arr[j][i] = 1

    DFS_answ = []
    DFS(V)

    visited = [0] * (N+1)
    BFS_answ = []
    BFS(V)

    print(*DFS_answ)
    print(*BFS_answ)