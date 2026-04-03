'''
    https://www.acmicpc.net/problem/9655

    1 / 128

    탁자 위에 N개의 돌
        - 턴을 번갈아가며 돌을 1개 또는 3개 가져감
        - 마지막 돌을 가져가는 사람이 게임을 이김

    두 사람이 게임을 '완벽하게' 진행 + 상근이가 먼저 시작할 때 이기는 사람을 구하시오.

    입력: N
    출력: 상근이가 이기면 SK, 창영이가 이기면 CY
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N = int(input().strip())

    # [1] turn 계산
    # turn이 홀수면 다음 차례는 창영, 짝수면 다음 차례는 상근
    turn = N // 3

    # [2] 나머지 계산
    # 가능한 경우의 수 0, 1, 2
    # 0이면 현재 turn의 사람이 우승
    # 1이면 다음 turn의 사람이 우승
    # 2이면 현재 turn의 사람이 우승(다다음 이니까 현재 턴)
    remainder = N % 3
    if remainder == 0 or remainder == 2:
        if turn % 2 == 0:
            print('CY')
        else:
            print('SK')

    if remainder == 1:
        if turn % 2 == 0:
            print('SK')
        else:
            print('CY')