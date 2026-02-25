'''
    격자: N x N
        - 도로(0)와 도로가 아닌 곳(1) 존재
        - 메두사의 집(Sr,Sc), 공원(Er,Ec)
        - 도로만을 따라 집에서 공원까지 최단경로로 이동

    - M명의 전사
        - 전사들의 초기 위치 (Ri, Ci)

    - 상호작용
        - 전사들이 움직이기 전에 그들을 바라봄으로써 돌로 만들어 움직임을 멈출 수 있음
            - 메두사가 바라보는 방향에 대한 관리가 필요
'''

from collections import deque
import math

def print_statue(MAP):
    for row in MAP:
        for col in row:
            print(col, end='')
        print()

def distance(start:tuple, end:tuple):
    sy, sx = start
    ey, ex = end

    diff_y = abs(sy-ey)
    diff_x = abs(sx-ex)

    return  diff_x + diff_y

def in_range(coord:tuple):
    y, x = coord
    return 0<=x<N and 0<=y<N

def BFS(start:tuple, end:tuple):
    Q = deque()
    Q.append(start)
    visited[start[0]][start[1]] = start

    while Q:
        y, x = Q.popleft()

        if (y,x) == end:
            route = []
            py, px = visited[y][x]
            while (py,px) != start:
                route.append([py, px])
                py,px = visited[py][px]
            return route[::-1]

        for dy, dx in ((-1,0), (1,0), (0,-1), (0,1)):
            ny, nx = y+dy, x+dx
            if in_range((ny, nx)):
                if visited[ny][nx] == 0 and MAP[ny][nx] == 0:
                    Q.append((ny, nx))
                    visited[ny][nx] = (y,x)

    return -1


def make_seen_area(start:tuple, dir):
    mr, mc = start

    if dir == 0:  # 상
        # 상
        u_seen_coord = []
        for i, d_mr in enumerate(range(0, N)):
            ln_mc = mc - i
            rn_mc = mc + i
            up_n_mr = mr - d_mr
            if 0 <= up_n_mr < N and up_n_mr == mr - 1:
                u_seen_coord.append([up_n_mr, mc])
            if 0 <= ln_mc < N and 0 <= up_n_mr < N and i != 0:
                u_seen_coord.append([up_n_mr, ln_mc])
            if 0 <= rn_mc < N and 0 <= up_n_mr < N and i != 0:
                u_seen_coord.append([up_n_mr, rn_mc])
        for r, c in u_seen_coord:
            nr, nc = r-1, c
            while in_range((nr, nc)):
                u_seen_coord.append([nr, nc])
                nr, nc = nr-1, nc
        return u_seen_coord

    elif dir == 4:  # 하
        # 하
        d_seen_coord = []
        for i, d_mr in enumerate(range(0, N)):
            ln_mc = mc - i
            rn_mc = mc + i
            down_n_mr = mr + d_mr
            if 0 <= down_n_mr < N and down_n_mr == mr + 1:
                d_seen_coord.append([down_n_mr, mc])
            if 0 <= ln_mc < N and 0 <= down_n_mr < N and i != 0:
                d_seen_coord.append([down_n_mr, ln_mc])
            if 0 <= rn_mc < N and 0 <= down_n_mr < N and i != 0:
                d_seen_coord.append([down_n_mr, rn_mc])
        for r, c in d_seen_coord:
            nr, nc = r+1, c
            while in_range((nr, nc)):
                d_seen_coord.append([nr, nc])
                nr, nc = nr+1, nc
        return d_seen_coord

    elif dir == 6: # 좌
        # 좌
        l_seen_coord = []
        for i, d_mc in enumerate(range(0, N)):
            ln_mc = mc - d_mc
            up_n_mr = mr - i
            down_n_mr = mr + i
            if 0 <= ln_mc < N and ln_mc == mc - 1:
                l_seen_coord.append([mr, ln_mc])
            if 0 <= up_n_mr < N and 0 <= ln_mc < N and i != 0:
                l_seen_coord.append([up_n_mr, ln_mc])
            if 0 <= down_n_mr < N and 0 <= ln_mc < N and i != 0:
                l_seen_coord.append([down_n_mr, ln_mc])
        for r, c in l_seen_coord:
            nr, nc = r, c - 1
            while in_range((nr, nc)):
                l_seen_coord.append([nr, nc])
                nr, nc = nr, nc - 1
        return l_seen_coord

    elif dir == 2: # 우
        r_seen_coord = []
        for i, d_mc in enumerate(range(0, N)):
            rn_mc = mc + d_mc
            up_n_mr = mr - i
            down_n_mr = mr + i
            if 0 <= rn_mc < N and rn_mc == mc + 1:
                r_seen_coord.append([mr, rn_mc])
            if 0 <= up_n_mr < N and 0 <= rn_mc < N and i != 0:
                r_seen_coord.append([up_n_mr, rn_mc])
            if 0 <= down_n_mr < N and 0 <= rn_mc < N and i != 0:
                r_seen_coord.append([down_n_mr, rn_mc])

        for r,c in r_seen_coord:
            nr, nc = r, c + 1
            while in_range((nr,nc)):
                r_seen_coord.append([nr,nc])
                nr, nc = nr, nc + 1
        return r_seen_coord


    else:
        raise ValueError('not implement in make_seen_area func')

def count_worriers(start:tuple):
    # 시야에 들어오는 전사 좌표 저장 -> len으로 전사 수 파악 -> 방향 파악 -> 방향 내 전사들 이동 불가
    #

    seen_MAP_lst = []
    seen_cnt_lst = []
    tlst = []
    mr, mc = start[0], start[1]
    #
    for dir in (0, 4, 6, 2):
        seen_MAP = [[0] * N for _ in range(N)]
        seen_cnt = 0
        seen_w_lst = []  # 이 안에 있는 전사들을 대상으로 가려진 부분 처리
        seen_coords = make_seen_area(start, dir)
        for r, c in seen_coords:
            seen_MAP[r][c] = 1
        seen_MAP_lst.append(seen_MAP)
        for r, c in W:
            if seen_MAP[r][c] == 1:
                seen_cnt += W_MAP[r][c]
                seen_w_lst.append([r,c])
        tlst.append(seen_w_lst)
        seen_cnt_lst.append(seen_cnt) # 0,1,2,3 상하좌우
        # dir 방향으로 seen_w_list에 있는 전사들 뒷부분 2처리
    # max_val = -1
    # max_idx = -1
    # for i, cnt in enumerate(seen_cnt_lst):
    #     if cnt > max_val:
    #         max_val = cnt
    #         max_idx = i


    stone_lst = []
    dir_dict = {'0':0, '1':4, '2':6, '3':2}

    for i in range(4):
        num_stone = -1
        max_stone = 0
        dir = dir_dict[str(i)]
        seen_MAP = seen_MAP_lst[i]
        for seen_w_coord in tlst[i]:
            r, c = seen_w_coord
            nr, nc = r + dy[dir], c + dx[dir]
            make_safety_area(nr, nc, dir, seen_MAP)

            if dir == 0:
                if c < mc:
                    nr, nc = r + dy[7], c + dx[7]
                    while in_range((nr,nc)):
                        make_safety_area(nr,nc,dir, seen_MAP)
                        nr, nc = nr + dy[7], nc + dx[7]
                elif c > mc:
                    nr, nc = r + dy[1], c + dx[1]
                    while in_range((nr, nc)):
                        make_safety_area(nr, nc, dir, seen_MAP)
                        nr, nc = nr + dy[1], nc + dx[1]

            elif dir == 4:
                if c < mc:
                    nr, nc = r + dy[5], c + dx[5]
                    while in_range((nr,nc)):
                        make_safety_area(nr,nc,dir, seen_MAP)
                        nr, nc = nr + dy[5], nc + dx[5]
                elif c > mc:
                    nr, nc = r + dy[3], c + dx[3]
                    while in_range((nr, nc)):
                        make_safety_area(nr, nc, dir, seen_MAP)
                        nr, nc = nr + dy[3], nc + dx[3]

            elif dir == 6:
                if r < mr:
                    nr, nc = r + dy[7], c + dx[7]
                    while in_range((nr,nc)):
                        make_safety_area(nr,nc,dir, seen_MAP)
                        nr, nc = nr + dy[7], nc + dx[7]
                elif r > mr:
                    nr, nc = r + dy[5], c + dx[5]
                    while in_range((nr, nc)):
                        make_safety_area(nr, nc, dir, seen_MAP)
                        nr, nc = nr + dy[5], nc + dx[5]

            elif dir == 2:
                if r < mr:
                    nr, nc = r + dy[1], c + dx[1]
                    while in_range((nr, nc)):
                        make_safety_area(nr,nc,dir, seen_MAP)
                        nr, nc = nr + dy[1], nc + dx[1]
                elif r > mr:
                    nr, nc = r + dy[3], c + dx[3]
                    while in_range((nr, nc)):
                        make_safety_area(nr, nc, dir, seen_MAP)
                        nr, nc = nr + dy[3], nc + dx[3]

        for seen_w_coord in tlst[i]:
            r,c=seen_w_coord
            if seen_MAP[r][c] != 2:
                num_stone += 1
            if max_stone < num_stone:
                max_stone = num_stone

        stone_lst.append(max_stone)
    max_val = max(stone_lst)
    dir = stone_lst.index(max_val)


    return max_val, seen_MAP_lst[dir]

def make_safety_area(r, c, dir, seen_MAP):
    # nr, nc = r + dy[dir], c + dx[dir]
    nr, nc = r, c
    while in_range((nr, nc)):
        seen_MAP[nr][nc] = 2
        nr, nc = nr + dy[dir], nc + dx[dir]

#  move, attack_cnt = move_w(W, mr,mc)
def move_w(W, mr, mc, seen_MAP):
    attack_cnt = 0
    move_cnt = 0
# 돌로 변하지 않은 전사들은 메두사를 향해 최대 두 칸 이동, 이동 중 다른 전사와 칸을 공유할 수 있음
    for W_idx in range(len(W) - 1, -1, -1):
        c_dist = distance((W[W_idx]), (mr,mc))
        #
        r,c = W[W_idx]
        if seen_MAP[r][c] == 1:
            continue
        for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr, nc = r+dr, c+dc
            n_dist = distance((nr,nc), (mr,mc))
            if in_range((nr,nc)):
                # if seen_MAP[nr][nc] != 1 and n_dist < c_dist:
                if n_dist < c_dist:
                    W[W_idx] = [nr,nc]
                    move_cnt += 1
                    if W[W_idx] == [mr, mc]:
                        W.pop(W_idx)
                        attack_cnt += 1
                    break

    for W_idx in range(len(W) - 1, -1, -1):
        c_dist = distance((W[W_idx]), (mr, mc))
        r, c = W[W_idx]
        if seen_MAP[r][c] == 1:
            continue
        for dr, dc in ((0,-1),(0,1),(-1,0),(1,0)):
            nr, nc = r+dr, c+dc
            n_dist = distance((nr,nc), (mr,mc))
            if in_range((nr,nc)):
                # if seen_MAP[nr][nc] != 1 and n_dist < c_dist:
                if n_dist < c_dist:
                    W[W_idx] = [nr,nc]
                    move_cnt += 1
                    if W[W_idx] == [mr, mc]:
                        W.pop(W_idx)
                        attack_cnt += 1
                    break
    return move_cnt, attack_cnt
# 격자 내, 메두사 시야에 들어오는 곳으로는 이동 불가
# 첫 번째 이동
# 메두사와의 거리를 줄일 수 있는 방향으로 한 칸, 거리 동일하면 상하좌우 우선순위
# 두 번째 이동
# 메두사와의 거리를 줄일 수 있는 방향으로 한 칸 더 이동, 거리 동일하면 좌우상하 우선순위

if __name__ == '__main__':
    # [0] 입력
    N, M = list(map(int, input().split()))
    sr, sc, er, ec = list(map(int, input().split()))
    W_coord = list(map(int, input().split()))
    W = []
    for i in range(M):
        r,c = W_coord[i*2:i*2+2]
        W.append([r,c])

    MAP = [list(map(int, input().split())) for _ in range(N)]

    # visited 배열
    visited = [[0] * N for _ in range(N)]

    # 메두사 시야 맵 생성, 전사 맵 생성 및 전사 좌표 등록
    W_MAP = [[0] * N for _ in range(N)]
    for r, c in W:
        W_MAP[r][c] += 1

    # 메두사의 현재 위치 좌표
    mr, mc = sr, sc

    # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
    dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

    # [1] 메두사의 이동 (BFS)
    route = BFS((sr, sc), (er, ec))
    if route == -1:
        print(-1)
    else:
        # 턴 시작
        for mr, mc in route: # 메두사: 공원까지 최단 경로로 한 칸 이동
            # 메두사가 이동한 칸에 전사 존재 -> 전사 사망
            for W_idx in range(len(W)-1, -1, -1):
                if W[W_idx] == [mr, mc]:
                    W.pop(W_idx)

        # [2] 메두사의 시선
            # 상하좌우중 전사를 가장 많이 볼 수 있는 방향을 바라봄
                # 해당 방향이 여러개면 우선순위 상하좌우
            # 메두사가 본 전사는 돌로 변해 현재 턴에 이동 불가, 다음 턴에 돌에서 풀려남
                # 둘 이상의 전사가 같은 칸에 위치 -> 해당 칸 전사들 모두 돌로 변함
            # 바라보는 방향으로 90도의 시야각 (좌우 45도씩)
            # 특정 전사에 의해 메두사에게 가려진 전사는 돌로 변하지 않음
                # 8방향 중 한 방향에 전사가 위치해있으면 그 뒤는 메두사에게 안보임

            num_stone, seen_MAP = count_worriers((mr, mc))  # 이동 불가 시킬 좌표 return해주는 함수
            # print_statue(seen_MAP)
        # [3] 전사들의 이동
            move, attack_cnt = move_w(W, mr,mc, seen_MAP)
            # 돌로 변하지 않은 전사들은 메두사를 향해 최대 두 칸 이동, 이동 중 다른 전사와 칸을 공유할 수 있음
                # 격자 내, 메두사 시야에 들어오는 곳으로는 이동 불가
                # 첫 번째 이동
                    # 메두사와의 거리를 줄일 수 있는 방향으로 한 칸, 거리 동일하면 상하좌우 우선순위
                # 두 번째 이동
                    # 메두사와의 거리를 줄일 수 있는 방향으로 한 칸 더 이동, 거리 동일하면 좌우상하 우선순위
            print(move, num_stone, attack_cnt)
        print(0)
    # [4] 전사의 공격
        # 메두사와 같은 칸 -> 전사 사라짐

    # 거리 -> 맨해튼 거리 사용

