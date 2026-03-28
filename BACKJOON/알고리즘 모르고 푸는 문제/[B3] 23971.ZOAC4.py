'''
    한 명씩 앉을 수 있는 테이블이 행마다 W개씩 H행
    모든 참가자는 세로로N칸 또는 가로로M칸 이상 비우고 앉아야함
    = 다른 모든 참가자와 세로줄 번호의 차가 N보다 크거나
    가로줄 번호의 차가 M보다 큰 곳에만 앉을 수 있다.

    최대 몇 명 수용할 수 있는지 구하시오.

    입력:
        - H,W,N,M이 공백으로 (0 ~ 50000)

    출력:
        - 최대 인원 수
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    x_answ = 0
    y_answ = 0
    # [0] 입력
    H, W, N, M = map(int, input().strip().split())

    for x in range(W):
        if x % (M+1) == 0:
            x_answ += 1

    for y in range(H):
        if y % (N+1) == 0:
            y_answ += 1

    print(x_answ*y_answ)

'''
TC1
4 4 3 2 

TC2
4 4 1 2 

TC3
4 4 2 2

TC4
1 1 1 1

TC5
2 2 1 1 

TC6
5 4 2 2 
'''