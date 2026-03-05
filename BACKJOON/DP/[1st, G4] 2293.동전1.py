'''
    https://www.acmicpc.net/problem/2293

    N가지 종류의 동전, 각 동전의 가치는 다르다.
    동전을 적당히 사용해서 가치의 합이 k원이 되도록하는 경우의 수 구하기.

'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N, K = map(int, input().strip().split())
    value = [int(input().strip()) for _ in range(N)]

    # [1] DP
    dp = [0] * (K + 1)
    dp[0] = 1
    for v in value: # 1, 2, 5
        for i in range(v, K+1):
            dp[i] += dp[i-v]

    print(dp[K])




