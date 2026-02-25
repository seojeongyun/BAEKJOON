'''
    직사각형: N x M
        - 각 칸에는 한 자리 숫자가 적혀있다.

    꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형 찾기
'''

import sys

def in_range(coord):
    i, j = coord
    return 0 <= i < N and 0 <= j < M

if __name__ == '__main__':
    # [0] 입력
    input = sys.stdin.readline
    N, M = map(int, input().rstrip().split())
    MAP = [input().rstrip() for _ in range(N)]
    max_len = min(N, M)
    answ = 0

    # [1] 완전 탐색
    for len in range(max_len):
        for i in range(N):
            for j in range(M):
                ul, bl, br, ur = (i,j), (i+len, j), (i+len, j+len), (i, j+len)
                if in_range(ul) and in_range(bl) and in_range(br) and in_range(ur):
                    if MAP[ul[0]][ul[1]] == MAP[bl[0]][bl[1]] == MAP[br[0]][br[1]] == MAP[ur[0]][ur[1]]:
                        answ = max(answ, (len+1)**2)

    print(answ)

