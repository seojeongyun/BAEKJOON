'''
    https://www.acmicpc.net/problem/9663

    격자: N x N
    퀸 N개를 서로 공격할 수 없게 놓기

    출력: 퀸을 놓는 방법의 수
'''

import sys
from email.utils import collapse_rfc2231_value


def dfs(r):
    global answ

    # 종료 조건 및 정답 처리
    if r == N:
        answ += 1
        return

    for c in range(N):
        if not col_v[c] and not ul_v[r+c] and not ur_v[r-c]:
            col_v[c] = ul_v[r - c] = ur_v[r - c] = 1
            dfs(r+1)
            col_v[c] = ul_v[r + c] = ur_v[r - c] = 0

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0

    # [0] 입력
    N = int(input().strip())
    col_v = [0] * N
    ul_v = [0] * (2*N -1)
    ur_v = [0] * (2*N -1)

    # [1] 백트래킹
    dfs(0)

    print(answ)



'''
    [7분 20초] 메인 idea 설명
    N x N 격자에서 대각선 방향에 하나라도 기물이 놓여있는지 여부를 체크하는 방법
    https://www.youtube.com/watch?v=1Bh6DBcKgOc&list=PLodgw23vNd_UFQeV8GQtVHrT38VWE6iJv&index=2
'''