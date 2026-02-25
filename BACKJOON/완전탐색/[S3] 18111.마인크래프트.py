'''
    격자: N x M
    땅 고르기
        - 좌표 i,j의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
            - 2초 소모
        - 인벤토리에서 블록 하나를 꺼내 좌표 i,j의 가장 위에 있는 블록 위에 놓는다
            - 1초 소모

    땅 고르기에 걸리는 최소 시간과 땅의 높이 출력
    * 인벤토리에 B개의 블록 들어있고 땅의 높이는 0 <= H <= 256
'''

# 알고리즘: 완전탐색
# 땅 높이 0으로 고르는 경우의 시간
# 땅 높이 2로 고르는 경우의 시간
# ..
# 땅 높이 256으로 고르는 경우의 시간
# 위 시간들 중 최소시간 선택


import sys

def function(target, B):
    need_blocks_for_load = 0
    need_blocks_for_rm = 0

    for i in range(N):
        for j in range(M):
            if target > MAP[i][j]:
                need_blocks_for_load += target - MAP[i][j]

            else:
                need_blocks_for_rm += MAP[i][j] - target

    if need_blocks_for_rm + B < need_blocks_for_load:
        time = -1

    else:
        time = need_blocks_for_load + need_blocks_for_rm * 2

    return time

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M, B = map(int, input().rstrip().split())
    MAP = [list(map(int, input().rstrip().split())) for _ in range(N)]

    answ = []

    min_time = 21000000000
    for target in range(257):
        time = function(target, B)
        if time != -1:
            answ.append([time, target])
    answ.sort(key=lambda x: (x[0], -x[1]))

    print(*answ[0])