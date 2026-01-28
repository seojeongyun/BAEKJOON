'''
    2차원 평면 위에 점 N개
    우선순위: y, x로 정렬
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    #
    N = int(input().rstrip())
    lst = [list(map(int, input().rstrip().split())) for _ in range(N)]
    #
    lst.sort(key=lambda x: (x[1], x[0]))

    for answ in lst:
        print(*answ)