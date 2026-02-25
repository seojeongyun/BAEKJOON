'''
    피보나치 수: f(n) = f(n-1) + f(n-2) , n >= 2
    f(0) = 0
    f(1) = 1

    n이 주어졌을 때 n번째 피보나치 수를 구하는 프로그램
'''

if __name__ == '__main__':
    N = int(input())
    dp = [0,1]
    for i in range(2, N+1):
        dp.append(dp[i-1]+dp[i-2])

    print(dp[-1])





