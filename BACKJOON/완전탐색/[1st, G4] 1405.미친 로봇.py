'''
    https://www.acmicpc.net/problem/1405

    1 / 128

    로봇이 평면 위에서 N번의 행동
        - 각 행동에서 로봇은 4개 방향 중 하나를 선택 후 이동
        - 같은 곳을 한 번 보다 많이 이동하지 않을 때, 로봇의 이동 경로가 단순하다.
            - 예를들어 EENE와 ENW는 단순, ENWS와 WWWWSNE는 단순하지 않다
                - 방향 X, 같은 좌표를 두 번 이상 지나면 단순하지 않은것.

    입력:
        - 첫째 줄에 N, 동-서-남-북으로 이동할 확률이 주어짐
            - 1 <= N <= 14
            - 0 <= Prob <= 100
    출력:
        로봇의 이동 경로가 단순할 확률
'''

import sys

# 전체를 다 돌아도 2^24, v로 관리하니 2^24 미만
def dfs(lst, dir_lst, cnt):
    global answ

    # 종료 조건 및 정답 처리
    if cnt == P:
        # 확률 구하고
        prob = 1
        for dir in dir_lst:
            prob *= Prob[dir]
        answ += prob
        return

    for i, (di, dj) in dir_cit.items():
        ci, cj = lst[-1][0]+di, lst[-1][1]+dj
        if not v[ci][cj]:
            v[ci][cj] = 1
            dfs(lst+[[ci,cj]], dir_lst+[i], cnt+1)
            v[ci][cj] = 0


if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0

    # [0] 입력
    P, E, W, S, N = list(map(int, input().strip().split()))
    Prob = [E/100, W/100, S/100, N/100]
    dir_cit = {
        0 : (1,0),
        1 : (-1,0),
        2 : (0,1),
        3 : (0,-1)
    }
    # [1] 백트래킹
    v = [[0]*(2*P + 2) for _ in range(2*P+2)]
    v[(2*P + 2)//2][(2*P + 2)//2] = 1
    dfs([[(2*P + 2)//2,(2*P + 2)//2]], [], 0)

    print(answ)