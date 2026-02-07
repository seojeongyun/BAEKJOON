'''
    https://www.acmicpc.net/problem/1427

    2/128

    출력: 주어진 수에 대해 각 자리수를 내림차순으로 정렬

    N <= 10억
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N = list(input().strip())

    # [1] 정렬
    N.sort(key=lambda x: -1*int(x))

    # [2] 출력
    print(''.join(N))