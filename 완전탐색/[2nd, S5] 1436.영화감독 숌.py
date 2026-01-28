'''
    종말의 수: 6이 3개 이상 연속으로 들어가는 수

    N번째 영화의 제목은 N번째로 작은 종말의 수

    출력: 숌이 만든 N번째 영화의 제목에 들어간 수
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    num = 0
    answ = 0

    # [0] 입력
    N = int(input().rstrip())

    # [1] 완전탐색
    while True:
        num += 1

        if '666' in str(num):
            answ += 1

        if answ == N:
            break

    print(num)