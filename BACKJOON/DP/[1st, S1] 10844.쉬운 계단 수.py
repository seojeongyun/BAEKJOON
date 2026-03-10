'''
    https://www.acmicpc.net/problem/10844

    1 / 256

    계단 수: 인접한 모든 자리의 차이가 1

    N이 주어질 때, 길이가 N인 계단 수가 총 몇 개인지 구하시오
    0으로 시작하는 수는 계단 수가 아니다.

    해설: https://www.youtube.com/watch?v=SPVOKqMDerQ
'''

import sys

def print_map(map):
    for row in map:
        print(*row)

if __name__ == '__main__':
    input = sys.stdin.readline
    MOD = 1000000000

    # [0] 입력
    N = int(input().strip())

    # [1] DP
    dp = [[0] * 12 for _ in range(N+1)]
    # dp[1] 초기화
    dp[1][2:-1] = [1] * 9

    # [2] dp
    for i in range(2, N+1):
        for j in range(1, 11):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    # print(sum(dp[N]))
    print(sum(dp[N]) % MOD)

