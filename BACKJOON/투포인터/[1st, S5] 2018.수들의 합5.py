'''
    https://www.acmicpc.net/problem/2018

    2 / 32

    자연수 N은 몇 개의 연속된 자연수의 합으로 나타낼 수 있다
    자연수 N(1 ≤ N ≤ 10,000,000)에 대해,이 N을 몇 개의 자연수의 합으로 나타낼 수 있는지 가지수를 알고 싶다
        - 사용하는 자연수는 N 이하

    ex)
        15를 나타내는 방법은 15, 7+8, 4+5+6, 1+2+3+4+5의 4가지가 있다.
        반면에 10을 나타내는 방법은 10, 1+2+3+4의 2가지

    입력:
        첫 줄에 정수 N

    출력:
        가지수
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0

    # [0] 입력
    N = int(input().strip())

    # [1] 투포인터
    start, end = 0, 0
    current_sum = 0
    while True:
        if current_sum >= N:
            if current_sum == N:
                answ += 1
            current_sum -= start+1
            start += 1
        elif end == N:
            break

        else:
            current_sum += end+1
            end += 1

    print(answ)