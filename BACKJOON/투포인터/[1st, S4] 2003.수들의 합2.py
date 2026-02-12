'''
    https://www.acmicpc.net/problem/2003

    0.5 / 128

    N개의 수로 된 수열
        - A[1], A[2], ... , A[N]

    이 수열의 i번째 수 부터 j번째 수까지의 합이 M이 되는 경우의 수 구하기

    입력:
        - 첫째 줄 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)
        - 다음 줄 수열이 공백으로 분리되어 주어짐 <= 30,000

    출력:
        경우의 수
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0

    # [0] 입력
    N, M = map(int, input().strip().split())
    data = list(map(int, input().strip().split()))

    # [1] 투포인터: O(N) = O(N) -> O(15000) < 0.5초
    start, end = 0, 0
    current_sum = 0
    while True:
        # A[x]는 자연수이기 때문에 M보다 크다면, end는 늘려봤자 계속 커지기만 함
        # 따라서, start를 오른쪽으로 한 칸 이동시켜서 다시 탐색.
        if current_sum >= M:
            if current_sum == M:
                answ += 1
            current_sum -= data[start]
            start += 1

        elif end == N:
            break

        else:
            current_sum += data[end]
            end += 1

    print(answ)


'''
TC 1
4 2
1 1 1 1

TC 2
10 5
1 2 3 4 2 5 3 1 1 2

TC 3
1 2
1

TC 4
6 3
1 1 1 1 1 1
'''