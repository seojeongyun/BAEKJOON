# '''
# 격자 : M x N x H
#     - 접근할 땐 H N M 순일듯
#
# 익은 토마토 인접한 곳
#     - 안 익은 토마토는 익게 됨
#     - 인접: 상, 하, 좌, 우, 앞, 뒤
#
# 며칠이 지나면 토마토들이 모두 익는지 최소 일수 구하기 (BFS)
#
# 상자의 일부 칸에는 토마토가 들어있지 않을 수 있다.
#
# 저장될 때 부터 모든 토마토가 익어있는 상태이면 0을 출력
#     - min값이 1인 경우
#
# 토마토가 모두 익지 못하는 상황이면 -1
#     - BOX에 0이 존재하면
#
# 토마토
#     - 1은 익은 토마토
#     - 0은 익지 않은 토마토
#     - -1은 토마토가 들어있지 않은 칸
# '''
#
# from collections import deque
#
# def is_in_range(coord:tuple):
#     x, y, z = coord
#     return 0<=x<M and 0<=y<N and 0<=z<H
#
# def BFS(start:list):
#     while Q:
#         x, y, z = Q.popleft()
#         for dx, dy, dz in ((0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)):
#             nx, ny, nz = x+dx, y+dy, z+dz
#             if is_in_range((nx, ny, nz)):
#                 if visited[nz][ny][nx] == 0 and BOX[nz][ny][nx] == 0:
#                     BOX[nz][ny][nx] = 1
#                     visited[nz][ny][nx] = visited[z][y][x] + 1
#                     Q.append((nx, ny, nz))
#
# def print_status(BOX):
#     for h in BOX:
#         for r in h:
#             for c in r:
#                 print(c, end = ' ')
#             print()
#         print()
#
# if __name__ == '__main__':
#     global M,N,H,BOX,visited
#     M, N, H = tuple(map(int, input().split()))
#     # 가로, 세로, 높이
#     BOX = []
#     for _ in range(H):
#         GRID = [list(map(int, input().split())) for _ in range(N)]
#         BOX.append(GRID)
#
#     visited = []
#     for _ in range(H):
#         visited_grid = [[0] * M for _ in range(N)]
#         visited.append(visited_grid)
#
#     # 단지 번호 붙이기 상위호환
#     start = (0,0,0)
#     Q = deque()
#     x, y, z = start
#     #
#     cnt = 0
#     for height in range(H):
#         for row in range(N):
#             for col in range(M):
#                 nx, ny, nz = x + col, y + row, z + height
#                 # 박스 순회하며 익은 토마토를 만나는 경우 익지 않은 토마토(0)을 대상으로 BFS
#                 # 순회하면서 하면 안될 것 같음. 동시에 퍼지기 시작해야함.
#                 if visited[nz][ny][nx] == 0 and  BOX[nz][ny][nx] == 1:
#                     visited[nz][ny][nx] = 1
#                     Q.append((nx,ny,nz))
#                 elif visited[nz][ny][nx] == 0 and  BOX[nz][ny][nx] == 0:
#                     cnt += 1
#
#     if cnt == 0:
#         print_zero = True
#         print(0)
#
#     else:
#         BFS(Q)
#         #
#         max = 0
#         not_all = False
#         for i in range(len(visited)):
#             for j in range(len(visited[i])):
#                 for k in range(len(visited[i][j])):
#                     if max < visited[i][j][k]:
#                         max = visited[i][j][k]
#
#                     if BOX[i][j][k] == 0:
#                         not_all = True
#                         break
#                 if not_all: break
#             if not_all: break
#
#         if not_all:
#             print(-1)
#         else:
#             print(max - 1)
#
#     # print_status(BOX)

'''
격자 : M x N x H
    - 접근할 땐 H N M 순일듯

익은 토마토 인접한 곳
    - 안 익은 토마토는 익게 됨
    - 인접: 상, 하, 좌, 우, 앞, 뒤

며칠이 지나면 토마토들이 모두 익는지 최소 일수 구하기 (BFS)

상자의 일부 칸에는 토마토가 들어있지 않을 수 있다.

저장될 때 부터 모든 토마토가 익어있는 상태이면 0을 출력
    - min값이 1인 경우

토마토가 모두 익지 못하는 상황이면 -1
    - BOX에 0이 존재하면

토마토
    - 1은 익은 토마토
    - 0은 익지 않은 토마토
    - -1은 토마토가 들어있지 않은 칸
'''

from collections import deque

def is_in_range(coord:tuple):
    x, y, z = coord
    return 0<=x<M and 0<=y<N and 0<=z<H

def BFS(start:list, front:int):
    while front < len(Q):
        x, y, z = Q[front]
        front+=1
        for dx, dy, dz in ((0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)):
            nx, ny, nz = x+dx, y+dy, z+dz
            if is_in_range((nx, ny, nz)):
                if visited[nz][ny][nx] == 0 and BOX[nz][ny][nx] == 0:
                    BOX[nz][ny][nx] = 1
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    Q.append((nx, ny, nz))

def print_status(BOX):
    for h in BOX:
        for r in h:
            for c in r:
                print(c, end = ' ')
            print()
        print()

if __name__ == '__main__':
    global M,N,H,BOX,visited,Q
    M, N, H = tuple(map(int, input().split()))
    # 가로, 세로, 높이
    BOX = []
    for _ in range(H):
        GRID = [list(map(int, input().split())) for _ in range(N)]
        BOX.append(GRID)

    visited = []
    for _ in range(H):
        visited_grid = [[0] * M for _ in range(N)]
        visited.append(visited_grid)

    # 단지 번호 붙이기 상위호환
    start = (0,0,0)
    Q = []
    front = 0
    x, y, z = start
    #
    cnt = 0
    for height in range(H):
        for row in range(N):
            for col in range(M):
                nx, ny, nz = x + col, y + row, z + height
                # 박스 순회하며 익은 토마토를 만나는 경우 익지 않은 토마토(0)을 대상으로 BFS
                # 순회하면서 하면 안될 것 같음. 동시에 퍼지기 시작해야함.
                if visited[nz][ny][nx] == 0 and  BOX[nz][ny][nx] == 1:
                    visited[nz][ny][nx] = 1
                    Q.append((nx,ny,nz))

                elif visited[nz][ny][nx] == 0 and  BOX[nz][ny][nx] == 0:
                    cnt += 1

    if cnt == 0:
        print_zero = True
        print(0)

    else:
        BFS(Q, front)
        #
        max = 0
        not_all = False
        for i in range(len(visited)):
            for j in range(len(visited[i])):
                for k in range(len(visited[i][j])):
                    if max < visited[i][j][k]:
                        max = visited[i][j][k]

                    if BOX[i][j][k] == 0:
                        not_all = True
                        break
                if not_all: break
            if not_all: break

        if not_all:
            print(-1)
        else:
            print(max - 1)

    # print_status(BOX)