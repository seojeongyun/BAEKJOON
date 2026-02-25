'''
    비밀번호 길이와 일부 숫자가 주어질 때 가능한 모든 비밀번호의 개수를 출력하시오.

    예제)
    첫 줄에 비밀번호 길이, 비밀번호에 들어가는 수의 개수
    두 번째 줄에 비밀번호에 들어가는 수가 주어짐

    [알고리즘]
    백트래킹: 재귀함수를 이용해 "가능한" 모든 경우를 확인해보는 완전탐색 알고리즘
'''

import sys

def dfs(len, lst):
    global answ

    # [1] 종료 조건
    if len == N:
        # [2] 정답 처리
        NOT_IN = False
        for num in NUM:
            if not num in lst:
                NOT_IN = True
                break
        if not NOT_IN:
            answ += 1
        return

    for i in range(10):
        dfs(len + 1, lst+[i])

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().rstrip().split())
    NUM = list(map(int, input().rstrip().split()))
    #
    answ = 0
    lst = []
    #
    dfs(0, lst)
    #
    print(answ)
