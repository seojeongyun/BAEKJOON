'''

'''

import sys
sys.setrecursionlimit(10**7)
# def dfs(lst, n):
#     global answ
#     result = 0
#
#     if n == N:
#         answ = lst
#         return
#
#     for i in range(len(lst)-1, len(lst)-3, -1):
#         result += lst[i]
#
#     dfs(lst+[result], n+1)

def fibo(n):
    if n <= 2:
        return 1

    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = fibo(n - 1) + fibo(n - 2)
        return dp[n]

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N = int(input().strip())
    dp = [0] * N

    answ = fibo(N)

    print(answ)