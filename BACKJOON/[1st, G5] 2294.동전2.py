'''
    https://www.acmicpc.net/problem/2294

    n가지 종류의 동전
        동전을 적당히 사용해서 가치의 합이 k원이 되도록
        동전의 개수가 최소가 되도록
    각 동전은 몇 개라도 사용할 수 있다.

    입력:
        n, k ( 1 <= n <= 100, 1 <= k <= 10000)
        n개의 줄에는 각각의 동전의 가치 1 <= 가치 <= 100000

    출력:
        첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.
'''

import sys
from collections import deque

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = sys.maxsize

    # [0] 입력
    N, K = map(int, input().strip().split())
    value = [int(input()) for _ in range(N)]
    value.sort()

    # [1]
    remain = K
    while True:
        for i in range(N-1, -1, -1):
            if remain-value[i] > 0:
                remain -= value[i]
                break

    print(answ)

'''
TC1
3 15
1
5
12

TC2
3 22
3
4
10

TC3
4 18
1
2
3
4
'''