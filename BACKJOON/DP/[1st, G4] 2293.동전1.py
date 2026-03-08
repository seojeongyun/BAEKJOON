'''
    https://www.acmicpc.net/problem/2293

    N가지 종류의 동전, 각 동전의 가치는 다르다.
    동전을 적당히 사용해서 가치의 합이 k원이 되도록하는 경우의 수 구하기.

    해설: https://aia1235.tistory.com/33
    해설: https://velog.io/@rhdmstj17/%EB%B0%B1%EC%A4%80-2293%EB%B2%88-%EB%8F%99%EC%A0%84-1-python-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D
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




