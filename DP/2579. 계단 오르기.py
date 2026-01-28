'''
    시작지점에서 도착까지 이동하는 게임
        - 계단을 밟으면 해당 계단에 적힌 점수를 획득

    규칙
        - 한 번에 한 계단 혹은 두 계단 씩 오를 수 있음
        - 연속된 세 개의 계단을 모두 밟아서는 안된다.
        - 도착 계단은 반드시 밟아야한다.

    총 점수의 최댓값을 구하는 프로그램

    * DP 알고리즘은 규칙성을 찾는 게 핵심
'''



if __name__ == '__main__':
    N = int(input())
    score = [0] + [int(input()) for _ in range(N)]
    dp = [[0] * 3 for _ in range(N+1)]

    for i in range(1, N+1):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = dp[i-1][0] + score[i]
        dp[i][2] = dp[i-1][1] + score[i]

    print(max(dp[N][1:3]))



