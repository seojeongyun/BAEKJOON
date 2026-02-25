'''
    https://www.acmicpc.net/problem/22864

    1 / 1024

    한 시간 단위로 일을 하거나 쉬어도 된다.
        - 일하면 피로도 +A, 일은 -B만큼 처리
        - 쉬면 피로도는 -C, 피로도가 음수가 되면 0이 됨

    피로도를 M을 넘지 않게 일을 하려고 한다.
        M을 넘기면 번아웃이

    입력:
        - 첫 번째 줄에 A,B,C,M
        - 처음 피로도는 0

    출력:
        - 얼마나 많은 일을 할 수 있는지
'''

import sys
sys.setrecursionlimit(10**7)

# def dfs(hour, task, stress):
#     global answ
#
#     # 종료 조건 및 정답 처리
#     if hour == 0 and stress < M:
#         answ = max(answ, task)
#
#     # 일을 한다
#     if stress < M:
#         dfs(hour-1, task+B, stress+A)
#
#     # 일을 안한다
#     if stress >= 0:
#         dfs(hour-1, task, stress-C)

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0

    # [0] 입력
    A,B,C,M = map(int, input().strip().split())
    hour = 24
    stress = 0

    # # [1] 백트래킹
    # dfs(24, 0, 0)

    # 그리디
    # 현재 M 이상인가 ? -> 쉰다.
    # M 미만인가 ? -> 일한다.

    for i in range(hour):

        if A + stress <= M:
            answ += B
            stress += A

        else:
            stress -= C
            stress = 0 if stress < 0 else stress

    print(answ)