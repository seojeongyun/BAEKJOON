'''
    N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하시오.
    = N명 줄 세우기

    [출력]
        - list에 순열 담아두었다가 출력
'''


import sys
import itertools

def dfs(len, lst):
    if len == N:
        answ.append(lst)
        return

    for i in range(1, N+1):
        if i not in lst:
            dfs(len + 1, lst + [i])

if __name__ == '__main__':
    # [0] 입력
    input = sys.stdin.readline
    N = int(input())

    # [1] 변수 선언
    answ = []
    lst = []

    # [2-1] 재귀
    # dfs(0, lst)

    # [2-2] itertools
    lst = list(range(1, N + 1))

    answ = itertools.permutations(lst, N)

    # [3] 출력
    for answer in answ:
        print(*answer)

