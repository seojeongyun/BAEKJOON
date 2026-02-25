'''
    격자 : N x N
        - N^2명의 학생으로 구성
        - 초기: T, C, M 중 하나만 선택

    - 다른 학생에게 영향
        - 초코우유, 민트우유, 민트초코, 민트초코우유 신봉자 생김
        - 초기 신앙심 보유

    - Fij: 신봉하는 음식
    - Bij: 초기 신앙심
'''
from collections import deque

def in_range(coord:tuple):
    x, y = coord
    return 0<=x<N and 0<=y<N

def group():
    # 인접 학생과 신봉 음식이 완전 같으면 그룹 형성
    glst = []
    #
    visited = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            nF = F_MAP[y][x]
            if visited[y][x] == 0:
                tlst = BFS((x,y), visited, nF)
                # if len(tlst) > 2:
                #     glst.append(tlst)
                # else:
                #     continue
                glst.append(tlst)
    return glst
    # [[F, [c1, r1, B1], [c2, r2, B2] .. []]

def BFS(start:tuple, visited, nF):
    sx, sy = start[0], start[1]
    visited[sy][sx] = 1
    #
    Q = deque()
    Q.append(start)

    tlst = []
    tlst.append(nF)
    tlst.append([B_MAP[sy][sx], sy, sx])
    while Q:
        x, y = Q.popleft()
        # 4방향, v, FMAP, range
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if in_range((nx, ny)):
                if visited[ny][nx] == 0 and F_MAP[ny][nx] == nF:
                    visited[ny][nx] = nF
                    Q.append((nx,ny))
                    tlst.append([B_MAP[ny][nx], ny, nx])

    return tlst


def propagate(leader_lst):
    safety_mode = []
    dx, dy = [0,0,-1,1], [-1,1,0,0] # 0,1,2,3 : 상하좌우
    for leader in leader_lst: # lst = ['F', B, r, c]
        nF = leader[0]
        B = leader[1]
        r, c = leader[2], leader[3]
        #
        if [c, r] in safety_mode:
            continue

        B_MAP[r][c] = 1 # 전파자는 신앙심 1만 남기고
        X = B - 1       # 나머지를 간절함(x = B-1)으로 바꿔 전파
        #
        dir_num = B % 4 # 전파 방향 : B를 4로 나눈 나머지

        while True: # 간절함 0되면 종료
            r, c = r + dy[dir_num], c + dx[dir_num] # 전파 방향으로 한 칸 씩 이동하며 전파 시도
            if in_range((c, r)) == False or X <= 0: # 격자 이탈시 종료
                break
            #
            if F_MAP[r][c] == nF: # 전파 대상(전파당하는)이 전파자와 신봉음식이 완전 같으면 전파 스킵
                continue

            else: # 전파 대상과 신봉음식이 다르면 전파 진행
                safety_mode.append([c, r])
                if X > B_MAP[r][c]:     # 강한 전파
                    F_MAP[r][c] = nF    # 전파당하면 전파자의 신봉음식을 신봉하게 됨
                    B_MAP[r][c] += 1    # 전파 대상의 신앙심은 1 증가
                    X -= B_MAP[r][c]    # 전파자는 간절함이 y+1만큼 깎임


                elif X <= B_MAP[r][c]:  # 약한 전파 성공
                    F_MAP[r][c] |= nF     # 전파자 관심 음식의 기본 조합 + 전파대상 관심 음식을 합친 음식 신봉
                    B_MAP[r][c] += X    # 대상의 신앙심은 x만큼 증가
                    break


if __name__ == '__main__':
    # [0] 입력
    N, T = list(map(int, input().split()))
    f_dict = {'T':1, 'C':2, 'M':4}
    F_MAP = [list(input()) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            F = F_MAP[y][x]
            if F == 'T': F_MAP[y][x] = f_dict[F]
            elif F == 'C': F_MAP[y][x] = f_dict[F]
            else: F_MAP[y][x] = f_dict[F]
    B_MAP = [list(map(int, input().split())) for _ in range(N)]


    # [1] T일 동안 진행
    for T in range(T):
    # [2] 아침
        # 모든 학생은 신앙심 1 획득
        for y in range(N):
            for x in range(N):
                B_MAP[y][x] += 1

    # [3] 점심
        # 인접 학생과 신봉 음식이 완전 같으면 그룹 형성
        glst = group()
        # [[F, [B1, r1, c1], [B2, r2, c2] .. []]이 여러개
        #
        # 그룹 내에서 대표자 한 명 선정
            # 선정 기준: 신앙심 가장 큰 -> rk 가장 작은 -> ck 가장 작은

        leader_lst = []
        for lst in glst:
            max = (0, 0, 0)
            F = lst[0]
            for student in lst[1:]:
                B, r, c = student
                student_ = tuple((B, -1 * r, -1 * c))
                if max < student_:
                    max = tuple((student_[0], student_[1], student_[2]))
            leader_lst.append(list((F, max[0], -1 * max[1], -1 * max[2])))
            # in leader_lst, ['F', B, r, c]

        # print(leader_lst)
        # 그룹원은 대표자에게 신앙심 1씩 넘김
            # 대표자 신앙심 : 그룹원 수 -1 만큼 추가
        # for lst in glst:
        #     for student in lst[1:]:
        #         student_lst = [lst[0]] + student
        #         if student_lst not in leader_lst:
        #             _, B, r, c = student_lst
        #             B_MAP[r][c] -= 1
        #         else:
        #             _, B, r, c = student_lst
        #             B_MAP[r][c] += len(lst[1:]) - 1

        leader_pos = [[r,c] for _, _, r, c in leader_lst]

        for lst in glst:
            for student in lst[1:]:
                sr, sc = student[1], student[2]
                if [sr, sc] in leader_pos:
                    B_MAP[sr][sc] += len(lst[1:]) - 1
                else:
                    B_MAP[sr][sc] -= 1

        for idx in range(len(leader_lst)):
            r, c = leader_lst[idx][2], leader_lst[idx][3]
            leader_lst[idx][1] = B_MAP[r][c]

        # print(B_MAP)
        # [4] 저녁
        # 각 그룹의 대표자들이 신앙을 전파
        single_leader_lst = []
        multi_leader_lst = []
        triple_leader_lst = []

        # 순서
            # 단일 - 민트 T, 초코 C, 우유 M
            # 이중 - 초코우유CM, 민트우유TM, 민트초코TC
            # 삼중 - 민트초코우유TCM

        #
        # 같은 그룹 내에서 순서 / (초코우유 신앙의 서로 다른 두 그룹이 존재할 수 있음)
            # 대표자의 신앙심이 높은 순 -> 대표자 r 작은 -> 대표자 c 작은

        group_dict = {
            'single': [1,2,4],
            'multi' : [1|2, 1|4, 2|4],
            'triple' : [1|2|4]
        }
        for leader in leader_lst:
            F = leader[0]
            if F in group_dict['single']:
                single_leader_lst.append(leader)
            elif F in group_dict['multi']:
                multi_leader_lst.append(leader)
            else:
                triple_leader_lst.append(leader)

        single_leader_lst.sort(key=lambda x: (-x[1], x[2], x[3]))
        multi_leader_lst.sort(key=lambda x: (-x[1], x[2], x[3]))
        triple_leader_lst.sort(key=lambda x: (-x[1], x[2], x[3]))

        leader_lst = single_leader_lst + multi_leader_lst + triple_leader_lst
        # print(leader_lst)
        propagate(leader_lst)

        # score t, c, m, cm, tm, tc, tmc
        score_t, score_c, score_m, score_cm, score_tm, score_tc, score_tmc = 0, 0, 0, 0, 0, 0, 0
        for r in range(N):
            for c in range(N):
                if F_MAP[r][c] == 7:
                    score_tmc += B_MAP[r][c]
                elif  F_MAP[r][c] == 6:
                    score_cm += B_MAP[r][c]
                elif F_MAP[r][c] == 5:
                    score_tm += B_MAP[r][c]
                elif F_MAP[r][c] == 3:
                    score_tc += B_MAP[r][c]
                elif F_MAP[r][c] == 1:
                    score_t += B_MAP[r][c]
                elif F_MAP[r][c] == 2:
                    score_c += B_MAP[r][c]
                elif F_MAP[r][c] == 4:
                    score_m += B_MAP[r][c]
        #     f_dict = {'T':1, 'C':2, 'M':4} 민트, 초코, 우유
        print(score_tmc, score_tc, score_tm, score_cm, score_m, score_c, score_t)
