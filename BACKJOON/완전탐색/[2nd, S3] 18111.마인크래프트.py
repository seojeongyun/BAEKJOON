'''
    격자: N x M

    동작:
        블록을 제거하여 인벤토리에 넣는다: 2초 소요
        인벤토리에서 블록을 꺼내 쌓는다:  1초 소

    땅고르기에 걸리는 최소 시간과 그 경우 땅의 높이 출력

    제한: 0 <= 땅높이 <= 256
'''

# 격자 크기 최대 250,000 -> 0~256까지 쌓는 경우 완전 탐색
# 1억회 미만이므로 가능

import sys

def flatten(tgt, B):
    time = 0
    remove_blocks = 0
    put_blocks = 0

    for row in MAP:
        for col in row:
            if col != tgt:
                if col > tgt:
                    remove_blocks += (col-tgt)
                else:
                    put_blocks += (tgt-col)

    if put_blocks > remove_blocks + B:
        time = -1

    else:
        time = put_blocks+ remove_blocks * 2

    return time

if __name__ == '__main__':
    input = sys.stdin.readline
    ANSW = []

    # [0] 입력: NxM 격자, B개 블록
    N, M, B = map(int, input().rstrip().split())
    MAP = [list(map(int, input().rstrip().split())) for _ in range(N)]

    # [1] 완전탐색: 0이 되는 경우부터 256이 되는 경우까지
    for tgt in range(257):
        time = flatten(tgt, B)
        if time >= 0:
            ANSW.append([time, tgt])

    ANSW.sort(key=lambda x: (x[0], -x[1]))

    print(*ANSW[0])




