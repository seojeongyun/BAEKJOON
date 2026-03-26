'''
    피보나치 함수: 0 1 1 2 3 5 8 13 21 34 55
    3
    2 1

    2
    1 0

    4   32    21   10  10  3 2
    입력:
        - T
        - T개의 줄에 걸쳐 N이 주어짐 (N<40)

    출력:
        - 각 TC마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해 출력
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = []
    TC = int(input().strip())

    for _ in range(TC):
        N = int(input().strip())
        zero = [1, 0] + [0] * (N-1)
        one = [0, 1] + [0] * (N-1)

        for i in range(2,N+1):
            zero[i] = zero[i-1]+zero[i-2]
            one[i] = one[i-1]+one[i-2]

        answ.append((zero[N], one[N]))

    for answer in answ:
        print(*answer)