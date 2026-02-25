'''
    N+1일 째 되는 날 퇴사
        남은 N일 동안 최대한 많은 상담

    T_i: 상담 완료에 걸리는 시간
        시작날짜 포함, N+1일을 넘지 않도록

    P_i: 금액

    최대 수익을 구하시오.

    * 상담 시작일 + 상담일이
'''


# N <= 15, 한다, 안한다로 BT하면 2^15밖에 안되니까 가능하다.
import sys

def dfs(n, P):
    global ANSW

    if n >= N+1:
        ANSW = max(P, ANSW)
        return

    # 한다
    if n + TP_dct[n][0] <= N+1:
        dfs(n + TP_dct[n][0], P + TP_dct[n][1])

    # 안한다
    dfs(n + 1, P)

if __name__ == '__main__':
    input = sys.stdin.readline
    ANSW = 0

    # [0] 입력
    N = int(input().rstrip())
    TP_dct = {}
    for i in range(1, N+1):
        T,P = map(int, input().rstrip().split())
        TP_dct[i] = [T, P]

    # [1] 백트래킹
    # n: 현재 날짜
    dfs(1, 0)

    print(ANSW)