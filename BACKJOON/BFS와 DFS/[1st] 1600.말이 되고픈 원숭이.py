'''
    격자: N x M
        0은 평지, 1은 장애물

    말: 장기에서 마의 움직임과 동일
        장애물을 뛰어넘을 수 있다.

    원숭이: K번만 말의 움직임 가능, 이후엔 상하좌우 한 칸

    출력: 원숭이가 좌상단 -> 우하단까지 이동하는 최단 경로
'''

import sys
from collections import deque

def in_range(i, j):
    return 0 <= i <= M-1 and 0 <= j <= N-1

def bfs(start):
    i, j, k = start
    DQ = deque()
    DQ.append(start)
    v[i][j][k] = 1

    while DQ:
        ci, cj, ck = DQ.popleft()
        # 종료 조건
        if (ci, cj) == (M-1, N-1):
            # return v[ci][cj][ck] -1
            return v[ck][ci][cj] - 1

        for di, dj in monkey:
            ni, nj = ci + di, cj + dj
            # if in_range(ni, nj) and v[ni][nj][ck] == 0 and MAP[ni][nj] == 0:
            if in_range(ni, nj) and v[ck][ni][nj] == 0 and MAP[ni][nj] == 0:
                # v[ni][nj][ck] = v[ci][cj][ck] + 1
                v[ck][ni][nj] = v[ck][ci][cj] + 1
                DQ.append((ni, nj, ck))

        # 말 이동 수보다 작을 경우에만 이동
        if ck < T:
            for di, dj in horse:
                hi, hj = ci+di, cj+dj
                if in_range(hi, hj) and v[ck+1][hi][hj] == 0 and MAP[hi][hj] == 0:
                    # v[hi][hj][ck+1] = v[ci][cj][ck] +1
                    v[ck + 1][hi][hj] = v[ck][ci][cj] + 1
                    DQ.append((hi, hj, ck+1))


    return -1

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0

    # [0] 입력
    T = int(input().rstrip())
    N, M = map(int, input().rstrip().split())
    MAP = [list(map(int, input().rstrip().split())) for _ in range(M)]

    # didj
    monkey = ((1, 0), (0, 1), (-1, 0), (0, -1))
    horse = ((2,-1),(2,1),(1,-2),(-1,-2),(-2,-1),(-2,1),(1,2),(-1,2))

    # bfs
    v = [[[0]*N for _ in range(M)] for _ in range(T+1)]
    # v = [[[0] * (T+1) for _ in range(N)] for _ in range(M)]
    start = (0,0,0)
    time = bfs(start)

    print(time)


'''
    특정 이동 방식에 횟수가 정해져있을 땐 3차원 배열을 활용한다.
    방문 처리 배열을 3차원으로 표현하는데, v[열][행][이동수]로 이해하면 된다.
        -> v = [[[0] * (T+1) for _ in range(N)] for _ in range(M)]
    v[이동수][열][행] : 개인적으로 이게 더 직관적
        -> [[[0]*N for _ in range(M)] for _ in range(T+1)]
'''