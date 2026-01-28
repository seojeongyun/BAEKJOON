'''
문제 구성
    - Map은 N x M의 배열
    - 1은 이동할 수 있는 칸
    - 0은 이동할 수 없는 칸
        -출발: (1,1)
        -도착: (N,M)
    - 이동해야하는 최소의 칸 수

입력
    - 첫째 줄에 N,M
    - N개의 줄에는 M개의 정수가 붙어서 제공

출력
    - 첫째 줄에 지나야하는 최소의 칸 수

자료구조
    - A(NxM) 배열
    - graph, visited
    - Queue

알고리즘
    - DFS
    - BFS
        - 100 x 100의 경우를 생각하면 BFS가 좋을듯
        - 둘 다 구현해볼 거긴 함
'''


def is_in_range(coord):
    x, y = coord
    return 0 <= x < M and 0 <= y < N

def DFS(coord:tuple):
    x, y = coord

    # if x == M-1 and y == N - 1:
    #     return visited[N - 1][M - 1]

    for dir_num in range(4):
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        if is_in_range((nx,ny)):
            if visited[ny][nx] == False and A[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                A[ny][nx] = A[y][x] -1
                DFS((nx,ny))

    return visited[N - 1][M - 1]

def BFS(coord:tuple):
    # Q 생성
    Q = []
    # Q에 좌표 담기
    Q.append(coord)
    #
    while len(Q) > 0:
        x, y = Q.pop(0)

        if x == M - 1 and y == N - 1:
            return visited[N-1][M-1]

        # 4 방향 탐색
        for dir_num in range(4):
            nx, ny = x + dx[dir_num], y + dy[dir_num]
            # 조건: range 안에 있고
            if is_in_range((nx,ny)):
                # 조건: A[ny][nx] == 1 and visited[ny][nx] == False
                if A[ny][nx] == 1 and visited[ny][nx] == False:
                    Q.append((nx,ny))
                    visited[ny][nx] = visited[y][x] + 1
                    A[ny][nx] = A[y][x] - 1
    # return visited[N-1][M-1]


def print_status(A):
    for row in A:
        for col in row:
            print(col, end=' ')
        print()

if __name__ == '__main__':
    global N, M, A, dx, dy
    N, M = map(int, input().split())
    maze = [list(input()) for _ in range(N)]
    A = [[None] * M for _ in range(N)]
    for row, row_val in enumerate(maze):
        for col, col_val in enumerate(row_val):
            A[row][col] = int(col_val)

    visited = [[False] * M for _ in range(N)]
    dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
    # dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    start = (0,0)

    # DFS
    # visited[start[0]][start[1]] = 1
    # clst_dist = DFS(coord=start)
    # #
    # print(clst_dist)
    # print_status(A)
    # #
    # #
    # # BFS
    # A = [[None] * M for _ in range(N)]
    # for row, row_val in enumerate(maze):
    #     for col, col_val in enumerate(row_val):
    #         A[row][col] = int(col_val)
    #
    # visited = [[False] * M for _ in range(N)]
    visited[start[0]][start[1]] = 1
    clst_dist = BFS(coord=start)
    # #
    print(clst_dist)
    # print_status(A)