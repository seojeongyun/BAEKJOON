'''
    격자: N x N
        (1) 먼지가 있거나
            - 먼지의 양: p (1~100), -1인 경우 물건이 위치
        (2) 먼지가 없거나
        (3) 물건이 위치할 수 있음

    동작 (L회 반복)
        - 청소기의 이동
            - 각각의 로봇 청소기는 순서대로 이동 거리가 가장 가까운 '오염된 격자로 이동'
            - 물건, 청소기가 있는 격자로는 이동 불가능
            - 가까운 격자가 여러개
                - 우선순위: (r,c)

        - 청소
            - 청소기가 바라보는 방향을 기준으로 후방 제외 나머지 청소
            - 상하좌우 중 네 격자에서 청소할 수 있는 먼지량이 가장 큰 방향에서 청소를 시작
                - 격자마다 청소할 수 있는 최대 먼지량 20 -> 가장 크다 == 80
                - 합이 같은 방향 여러개
                    - 우선순위: 우 하 좌 상
            - 청소기마다 순서대로 진행

        - 먼지 축적
            - 모든 격자에 동시에 5씩 추가

        - 먼지 확산
            - 깨끗한 격자에 주변 4방향 격자의 먼지량 합을 10으로 나눈 만큼 확산
            - 소수점 아래 수 버림
            - 모든 깨끗한 격자에 대해 동시에 확산 진행

        - 출력
            - 전체 공간의 총 먼지량
            - 전체 공간에 먼지가 없으면 0 출력
'''

from collections import deque
#
def print_status(arr):
    for row in arr:
        for col in row:
            print(f"{col:^4}", end="")
        print()

def in_range(r,c):
    return 0<= r < N and 0 <= c < N

def move_to_clst_pos():
    for i, robot in enumerate(ROBOT): # 로봇 순차적으로 이동
        ci, cj = robot

        # 최단거리 찾는 함수 실행 -> 최단거리 좌표 추출
        ROBOT_MAP[ci][cj] = 0
        ti, tj = find_clst_pos(ci, cj, ROBOT)
        ROBOT_MAP[ti][tj] = 1
        # 로봇 좌표 업데이트
        if -1 in (ti, tj):
            pass
        else:
            ROBOT[i] = [ti, tj]

def find_clst_pos(ci, cj, ROBOT):
    # 각각의 청소기는 visited를 독립적으로 계산해야 함
    visited = [[0] * N for _ in range(N)]
    visited[ci][cj] = 1
    #
    DQ = deque()
    DQ.append([ci, cj])
    #
    clst_dist = -1
    best_pos = (ci, cj)
    #
    if MAP[ci][cj]> 0:  # 자기 자신 위에 먼지가 있는 경우 (테스트 2회 째 부터 적용)
        return ci, cj
    #
    while DQ:
        ci, cj = DQ.popleft()
        #
        # 네 방향, 범위내, 미방문, 갈 수 있는 길이면
        for di, dj in ((-1,0), (0,-1), (0,1), (1,0)):   # 우선순위 r 작 -> c 작
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and visited[ni][nj] == 0 and MAP[ni][nj] != -1 and ROBOT_MAP[ni][nj] != 1:
                if clst_dist != -1 and visited[ni][nj] > clst_dist:
                    break
                visited[ni][nj] = visited[ci][cj] + 1
                DQ.append([ni, nj])
                if MAP[ni][nj] > 0:         # ni, nj에 먼지가 있을 경우에
                    if clst_dist == -1:     # 먼지를 처음 만난 거라면
                        clst_dist = visited[ni][nj]   # 현재 dist를 가장 가까운 거리로 설정
                        best_pos = (ni, nj)           # 현재 ni, nj를 best pos 설정

                    elif visited[ni][nj] == clst_dist:  # 처음 만난 게 아니라, 동일 거리 다른 좌표라면,
                        if best_pos > (ni, nj):         # best_pos와 현재 좌표(ni, nj)를 비교해 행번호, 열번호 작은걸 best_pos로 사용
                            best_pos = (ni, nj)

    return best_pos

def cleaning():
    '''
    [알고리즘]
      - 청소는 순서대로 진행
      - 네 방향 순회하며 네 격자의 먼지량 합 구한다.
        - 순회 순서: 우 하 좌 상
        - if sum == 80: break
      - 결정된 방향으로 네 격자 청소(-20)
    '''
    #
    for ci, cj in ROBOT:  # 로봇
        candidate_dir = []
        for robot_dir in (1, 2, 3, 4):  # 우,하,좌,상 : 청소기가 바라보는 방향
            dust_sum = 0
            for arr_dir in (0, 1, 2, 3):  # 상, 우, 하, 좌: 네 격자 좌표 순회
                ni, nj = ci + di[arr_dir], cj + dj[arr_dir]
                if (robot_dir == 1 and arr_dir == 3) or (robot_dir == 2 and arr_dir == 0) or \
                    (robot_dir == 3 and arr_dir == 1) or (robot_dir == 4 and arr_dir == 2):
                    ni, nj = ci, cj
                if in_range(ni, nj) and MAP[ni][nj] > 0:
                    dust = MAP[ni][nj] if MAP[ni][nj] <= 20 else 20
                    dust_sum += dust
            candidate_dir.append((robot_dir,dust_sum))
        #
        # dust 내림차순, dir 오름차순
        candidate_dir.sort(key=lambda x: (-x[1], x[0]))
        dir, _ = candidate_dir[0]

        for arr_dir in (0, 1, 2, 3):  # 네 격자 좌표 순회
            ni, nj = ci + di[arr_dir], cj + dj[arr_dir]
            if (dir == 1 and arr_dir == 3) or (dir == 2 and arr_dir == 0) or \
                    (dir == 3 and arr_dir == 1) or (dir == 4 and arr_dir == 2):
                ni, nj = ci, cj
            if in_range(ni, nj) and MAP[ni][nj] > 0:
                dust = MAP[ni][nj] if MAP[ni][nj] <= 20 else 20
                MAP[ni][nj] -= dust

def dust_acc():
    '''
    [알고리즘]
        MAP 순회하면서 -1도 아니고 0도 아닌 곳에 +5
    '''

    for i in range(N):
        for j in range(N):
            if MAP[i][j] != 0 and MAP[i][j] != -1:
                MAP[i][j] += 5


def dust_spread():
    '''
    [알고리즘]
    - BFS로 깨끗한 격자 순회 (0인 곳)
        - 격자의 상하좌우 조회, 먼지 합 / 10으로 MAP 갱신
            - 크기가 10 이상인 확산된 먼지로부터의 영향을 방지하기 위해 상하좌우 조회시 미방문인 곳만 반영
    '''
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 0:
                dust_sum = 0
                visited[i][j] = 1
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):  # 네 방향
                    ni, nj = i + di, j + dj
                    if in_range(ni, nj) and visited[ni][nj] == 0 and MAP[ni][nj] > 0:  # 범위 내, 미방문
                        dust_sum += MAP[ni][nj]
                MAP[i][j] = dust_sum // 10

import time
if __name__ == '__main__':
    # [0] 입력
    N, K, L = map(int, input().split()) # 격자 크기, 청소기 개수, 테스트 회수
    MAP = [list(map(int, input().split())) for _ in range(N)] # 먼지 관리할 N x N 격자
    ROBOT = [list(map(int, input().split())) for _ in range(K)] # 로봇 좌표
    ROBOT_MAP = [[0] * N for _ in range(N)]
    #
    # MAP 범위 0 ~ N-1 에 맞추어 전처리
    for i, robot in enumerate(ROBOT):
        ci, cj = robot
        ROBOT[i] = [ci-1, cj-1]
        ROBOT_MAP[ci-1][cj-1] = 1

    #
    di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]

    # [1] 동작 (L회 반복)
    for l in range(L):
        answ = 0
        ''' 
        청소기의 이동
            - 각각의 로봇 청소기는 순서대로 이동 거리가 가장 가까운 '오염된 격자로 이동'
            - 물건, 청소기가 있는 격자로는 이동 불가능
            - 가까운 격자가 여러개
                - 우선순위: (r,c)
          
        [알고리즘]
            - BFS 사용
                - 조건: 범위내, 네방향, 미방문, -1도 아니고 다른 청소기 좌표도 아닐때
                    - 0도 아니고 -1도 아닌 값을 처음으로 만날 때, 그 순서에서의 값을 리스트에 저장하고 (r,c) 가장 낮은 거 고름
                - 해당 좌표를 ROBOT에 업데이트
        '''
        move_to_clst_pos()
        # print_status(MAP)
        '''
        청소
            - 청소기가 바라보는 방향을 기준으로 후방 제외 나머지 청소
            - 상하좌우 중 네 격자에서 청소할 수 있는 먼지량이 가장 큰 방향에서 청소를 시작
                - 격자마다 청소할 수 있는 최대 먼지량 20 -> 가장 크다 == 80
                - 합이 같은 방향 여러개
                    - 우선순위: 우 하 좌 상
            - 청소기마다 순서대로 진행
          
          [알고리즘]
          - 네 방향 순회하며 네 격자의 먼지량 합 구한다.
            - 순회 순서: 우 하 좌 상
            - if sum == 80: break
          - 결정된 방향으로 네 격자 청소(-20)
        '''
        cleaning()
        # print_status(MAP)


        '''
        - 먼지 축적
            - 모든 격자에 동시에 5씩 추가
        
        [알고리즘]
            MAP 순회하면서 -1도 아니고 ROBOT 좌표도 아니고 0도 아닌 곳에 +5
        '''
        dust_acc()
        # print_status(MAP)



        '''
        - 먼지 확산
            - 깨끗한 격자에 주변 4방향 격자의 먼지량 합을 10으로 나눈 만큼 확산
            - 소수점 아래 수 버림
            - 모든 깨끗한 격자에 대해 동시에 확산 진행
        
        [알고리즘]
            - BFS로 깨끗한 격자 순회 (0인 곳)
                - 격자의 상하좌우 조회, 먼지 합 / 10으로 MAP 갱신
                    - 크기가 10 이상인 확산된 먼지로부터의 영향을 방지하기 위해 상하좌우 조회시 미방문인 곳만 반영
        '''
        dust_spread()
        # print_status(MAP)



        for i in range(N):
            for j in range(N):
                if MAP[i][j] != -1:
                    answ += MAP[i][j]

        print(answ)

