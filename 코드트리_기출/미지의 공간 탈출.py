'''
    격자 : N x N
        - 격자 내 어딘가 M x M x M의 시간의 벽 존재

    빈 공간(0), 장애물(1), 타임머신의 위치(시작지점)(2), 시간의 벽의 위치(3), 탈출구(4)
        - 2에서 시작해 0을 통해 4로 이동

    시간 이상 현상
        - F개 존재
        - (ri, ci)
        - vi의 배수 턴마다 방향 di로 한 칸 씩 확산( 이동  X )
        - 빈 공간으로만 확산
        - 더이상 확산할 수 없을 경우 멈춤
        - 모든 시간 이상 현상은 서로 독립적이며 동시 확산
        - 방향 d: 동서남북/0,1,2,3

    출력
        - 탈출구까지 이동하는 최소 시간
        - 탈출 불가하면 -1 출력

    턴
        - 시간 이상 현상이 확산된 직후 타임머신 이동
        - 시간 이상 현상이 확산될 곳으로 이동할 수 없음.


'''
from collections import deque

def M_in_range(coord:tuple):
    x, y = coord
    return 0<=x<M and 0<=y<M

def N_in_range(coord:tuple):
    x, y = coord
    return 0<=x<N and 0<=y<N

def BFS_R(start:tuple, cnt):
    Q = deque()
    Q.append(start)
    visited_3d[0][start[1]][start[0]] = cnt + 1

    while Q:
        x, y = Q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if M_in_range((nx, ny)):
                if visited_3d[0][ny][nx] == 0 and M_MAP[0][ny][nx] == 0:
                    Q.append((nx,ny))
                    visited_3d[0][ny][nx] = visited_3d[0][y][x] + 1
            #
            elif len(Q) == 0:
                if nx == M:     # M_MAP[3] 북
                    nx, ny = 0, y
                    if visited_3d[3][ny][nx] == 0 and M_MAP[3][ny][nx] == 0:
                        BFS_U((nx,ny), visited_3d[0][y][x])

                elif nx < 0:    # M_MAP[2] 남
                    nx, ny = M-1, y
                    if visited_3d[2][ny][nx] == 0 and M_MAP[2][ny][nx] == 0:
                        BFS_D((nx,ny), visited_3d[0][y][x])

                elif ny < 0:    # M_MAP[4] 센터
                    nx, ny = M-1, x
                    if visited_3d[4][ny][nx] == 0 and M_MAP[4][ny][nx] == 0:
                        BFS_C((nx,ny), visited_3d[0][y][x])

def BFS_L(start:tuple, cnt):
    Q = deque()
    Q.append(start)
    visited_3d[1][start[1]][start[0]] = cnt + 1

    while Q:
        x, y = Q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if M_in_range((nx, ny)):
                if visited_3d[1][ny][nx] == 0 and M_MAP[1][ny][nx] == 0:
                    Q.append((nx,ny))
                    visited_3d[1][ny][nx] = visited_3d[1][y][x] + 1
            #
            elif len(Q) == 0:
                if nx < 0:     # M_MAP[3] 북
                    nx, ny = M-1, y
                    if visited_3d[3][ny][nx] == 0 and M_MAP[3][ny][nx] == 0:
                        BFS_U((nx,ny), visited_3d[1][y][x])

                elif nx == M:    # M_MAP[2] 남
                    nx, ny = 0, y
                    if visited_3d[2][ny][nx] == 0 and M_MAP[2][ny][nx] == 0:
                        BFS_D((nx,ny), visited_3d[1][y][x])

                elif ny < 0:    # M_MAP[4] 센터
                    nx, ny = 0, x
                    if visited_3d[4][ny][nx] == 0 and M_MAP[4][ny][nx] == 0:
                        BFS_C((nx,ny), visited_3d[1][y][x])

def BFS_D(start:tuple, cnt):
    Q = deque()
    Q.append(start)
    visited_3d[2][start[1]][start[0]] = cnt + 1

    while Q:
        x, y = Q.popleft()
        for dx, dy in ((0,-1),(-1,0),(0,1),(1,0)):
            nx, ny = x+dx, y+dy
            if M_in_range((nx, ny)):
                if visited_3d[2][ny][nx] == 0 and M_MAP[2][ny][nx] == 0:
                    Q.append((nx,ny))
                    visited_3d[2][ny][nx] = visited_3d[2][y][x] + 1
            #
            elif len(Q) == 0:
                if nx == M:     # M_MAP[0] 동
                    nx, ny = 0, y
                    if visited_3d[0][ny][nx] == 0 and M_MAP[0][ny][nx] == 0:
                        BFS_R((nx,ny), visited_3d[2][y][x])

                elif nx < 0:    # M_MAP[1] 서
                    nx, ny = M-1, y
                    if visited_3d[1][ny][nx] == 0 and M_MAP[1][ny][nx] == 0:
                        BFS_L((nx,ny), visited_3d[2][y][x])

                elif ny < 0:    # M_MAP[4] 센터
                    nx, ny = x, M-1
                    if visited_3d[4][ny][nx] == 0 and M_MAP[4][ny][nx] == 0:
                        BFS_C((nx,ny), visited_3d[2][y][x])

def BFS_U(start:tuple, cnt):
    Q = deque()
    Q.append(start)
    visited_3d[3][start[1]][start[0]] = cnt + 1

    while Q:
        x, y = Q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if M_in_range((nx, ny)):
                if visited_3d[3][ny][nx] == 0 and M_MAP[3][ny][nx] == 0:
                    Q.append((nx,ny))
                    visited_3d[3][ny][nx] = visited_3d[3][y][x] + 1
            #
            elif len(Q) == 0:
                if nx < 0:     # M_MAP[0] 동
                    nx, ny = M-1, y
                    if visited_3d[0][ny][nx] == 0 and M_MAP[0][ny][nx] == 0:
                        BFS_R((nx,ny), visited_3d[3][y][x])

                elif nx == M:    # M_MAP[1] 서
                    nx, ny = 0, y
                    if visited_3d[1][ny][nx] == 0 and M_MAP[1][ny][nx] == 0:
                        BFS_L((nx,ny), visited_3d[3][y][x])

                elif ny < 0:    # M_MAP[4] 센터
                    nx, ny = (M-1)-x, 0
                    if visited_3d[4][ny][nx] == 0 and M_MAP[4][ny][nx] == 0:
                        BFS_C((nx,ny), visited_3d[3][y][x])

def BFS_C(start:tuple, cnt):
    Q = deque()
    Q.append(start)
    visited_3d[4][start[1]][start[0]] = cnt + 1

    while Q:
        x, y = Q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if M_in_range((nx, ny)):
                if visited_3d[4][ny][nx] == 0 and M_MAP[4][ny][nx] == 0:
                    Q.append((nx,ny))
                    visited_3d[4][ny][nx] = visited_3d[4][y][x] + 1
            #
            elif len(Q) == 0:
                if nx == M:     # M_MAP[0] 동
                    nx, ny = (M - 1) - y, 0
                    if visited_3d[0][ny][nx] == 0 and M_MAP[0][ny][nx] == 0:
                        BFS_R((nx,ny), visited_3d[4][y][x])
                elif nx < 0:    # M_MAP[1] 서
                    nx, ny = y, 0
                    if visited_3d[1][ny][nx] == 0 and M_MAP[1][ny][nx] == 0:
                        BFS_L((nx,ny), visited_3d[4][y][x])
                elif ny == M:   # M_MAP[2] 남
                    nx, ny = x, 0
                    if visited_3d[2][ny][nx] == 0 and M_MAP[2][ny][nx] == 0:
                        BFS_D((nx,ny), visited_3d[4][y][x])
                elif ny < 0:    # M_MAP[3] 북
                    nx, ny = (M - 1) - x, 0
                    if visited_3d[3][ny][nx] == 0 and M_MAP[3][ny][nx] == 0:
                        BFS_U((nx,ny), visited_3d[4][y][x])

def BFS_2d(start:tuple, end:tuple):
    Q = deque()
    Q.append(start)

    while Q:
        x, y = Q.popleft()
        if (x,y) == end:
            return visited_2d[end[1]][end[0]]

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N:     # 범위내
                if visited_2d[ny][nx] == 0: # 미방문
                    if N_MAP[ny][nx] == 0 or N_MAP[ny][nx] == 4:  # 빈 공간
                        Q.append((nx,ny))
                        visited_2d[ny][nx] = visited_2d[y][x] + 1

                elif visited_2d[ny][nx] > visited_2d[y][x]+1:
                    if N_MAP[ny][nx] == 0 or N_MAP[ny][nx] == 4:  # 빈 공간
                        Q.append((nx, ny))
                        visited_2d[ny][nx] = visited_2d[y][x] + 1
    return -1


if __name__ == '__main__':
    N, M, F = list(map(int, input().split())) # 평면도 변, 시간의 벽 변, 시간 이상 현상 개수
    N_MAP = [list(map(int, input().split())) for _ in range(N)]

    # 시간의 벽의 동, 서, 남, 북, 윗면 단면도가 차례로 각 M줄 씩 주어짐 MxM이 M줄
    M_MAP = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)] # 0번 인덱스부터 동 -> 서 -> 남 -> 북 -> 위
    # M_MAP[0] = M x M

    F_list = [list(map(int, input().split())) for _ in range(F)] # 0번 인덱스에 [r0,c0,d0,v0] 존재

    # 출발 위치 탐색
    for r in range(M):
        for c in range(M):
            if M_MAP[4][r][c] == 2:
                start = (c, r)

    # 3d-visited
    visited_3d = [[[0] * M for _ in range(M)] for _ in range(5)]
    # 2 개의 MAP을 운영
        # [1] 시간의 벽
            # 3차원 BFS
                # M_MAP[0]에서 BFS
                    # BFS_C, BFS_L, BFS_R, BFS_U, BFS_D 함수로 구분
                    # if문 걸어서 range 이탈 여부에 따라 함수 선택
                    # 좌표는 ?
                        # center map의 좌표를 l,r,u,d map으로 옮겨가면서 전달

    BFS_C(start, 0) # 3D 출구 탐색

    # [2] BFS_2d start point 찾기
        # [2-1] N_MAP에서 start point 찾기
            # [2-1-1] 평면 상에서의 시간의 벽 좌표 탐색
    wall_coord = []
    for i in range(N):
        for j in range(N):
            if N_MAP[i][j] == 3:
                wall_coord.append([i, j])
            elif N_MAP[i][j] == 4:
                ex, ey = j, i

            # [2-1-2] 시간의 벽으로부터 상하좌우 탐색, N_MAP에서 뚫린 곳 좌표찾기
    x_range, y_range = [], []
    for y, x in wall_coord:
        if x not in x_range: x_range.append(x)
        if y not in y_range: y_range.append(y)

    for y, x in wall_coord:
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if N_MAP[ny][nx] == 0:
                sx, sy = nx, ny
                if (dx, dy) == (1,0):    # 동
                    dir = 0
                    idx = y_range.index(y)
                    cnt = visited_3d[dir][-1][M-1-idx]
                elif (dx, dy) == (-1, 0):    #서
                    dir = 1
                    idx = y_range.index(y)
                    cnt = visited_3d[dir][-1][idx]
                elif (dx, dy) == (0, 1):    # 남
                    dir = 2
                    idx = x_range.index(x)
                    cnt = visited_3d[dir][-1][idx]
                elif (dx, dy) == (0, -1):    # 북
                    dir = 3
                    idx = x_range.index(x)
                    cnt = visited_3d[dir][-1][M-1-idx]


    # 시간 이상 현상 정보 등록
    visited_2d = [[0] * N for _ in range(N)]
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    for r, c, d, v in F_list:
        visited_2d[r][c] = 1    # 어차피 바닥에 내려온 시점엔 cnt > 1이라서 1로 줘도 통과 못함
        for i in range(1, N):
            r, c = r+dr[d], c+dc[d]
            if 0 <= r < N and 0 <= c < N:  # 범위내면
                if N_MAP[r][c] == 0: # 0이면 확산
                    visited_2d[r][c] = i * v
                else:
                    break

    visited_2d[sy][sx] = cnt
    time = BFS_2d((sx,sy), (ex, ey))

    print(time)












    print()
                            # U,D,R,L MAP에서 Center로 이동, Center값 참조해서 행이나 열에 +1
                    # Center 값 참조할 땐 N_MAP에서 3의 위치 찾아서 좌표 구해야함.
        # [2] 평면
            # [2-1] 시간 이상 현상 관리
                # 평면 시작 지점에 BFS_3d의 cnt값 전달
                # BFS_2d 진행
                    # visited에 시간 미리 기록
                        # 해당 시간이 아니면 지나갈 수 있게 설계


