'''
    N개의 수로 이루어진 수열
    N-1개의 연산자
        - 덧셈, 뺄셈, 곱셈, 나눗셈

    주어진 수의 순서를 바꾸지 않고 수 사이에 연산자를 넣을 수 있다.

    예) 수열: 1, 2, 3, 4, 5, 6
      연산자: + + - x /
      -> 5개 줄 세우기 & 더하기 연산자는 순서가 없으니 2로 나눔
      -> 5! / 2 = 5 4 3 2 / 2 = 5 4 3  = 60

    연산자 우선 순위를 무시하고 앞에서부터 연산 진행
    나눗셈은 몫만 취함
    음수를 양수로 나눌 땐 양수로 바꾼뒤 몫을 취하고 몫을 음수로 취함

    N개의 수와 N-1개의 연산자가 주어졌을 때 만들 수 있는 식의 결과가
    최소인 것과 최대인 것을 구하시오.
'''

import sys
from collections import deque

def dfs(n, lst):
    global min_answ, max_answ

    # [0] 종료 조건 및 정답 처리
    if n == N-1:
        # 수식 검증
        tlst = []
        for i, v in enumerate(SEQ):
            tlst.append(v)
            if i < len(SEQ)-1:
                tlst.append(lst[i])

        DQ = deque(tlst)
        result = []

        while DQ:
            num = DQ.popleft()
            result.append(num)
            if len(result) == 3:
                if result[1] == 101:
                    result = [result[0] + result[2]]
                elif result[1] == 102:
                    result = [result[0] - result[2]]
                elif result[1] == 103:
                    result = [result[0] * result[2]]
                elif result[1] == 104:
                    result = [int(result[0] / result[2])]

        min_answ = min(min_answ, result[0])
        max_answ = max(max_answ, result[0])
        return

    for i in range(len(PATTERN_LIST)):
        if visited[i] == 0:
            visited[i] = 1
            lst.append(PATTERN_LIST[i])
            dfs(n+1, lst)
            lst.pop()
            visited[i] = 0



if __name__ == '__main__':
    # [0] 입력
    input = sys.stdin.readline
    N = int(input().rstrip())   # 수열 길이
    SEQ = list(map(int, input().rstrip().split()))
    PATTERN = list(map(int, input().rstrip().split()))

    # [1] PATTERN 전처리
    PATTERN_LIST = []
    for i, v in enumerate(PATTERN):
        for j in range(v):
            PATTERN_LIST.append(101+i)

    # [2] 변수 선언
    min_answ = 10 ** 9
    max_answ = -1 * 10 ** 9
    cnt = 0
    visited = [0] * len(PATTERN_LIST)
    #
    dfs(0, [])
    #
    print(max_answ)
    print(min_answ)


