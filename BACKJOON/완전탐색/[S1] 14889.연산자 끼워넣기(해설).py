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

def dfs(n, val, add, sub, mul, div):
    global mn, mx
    # [1] 종료 조건 및 정답 처리
    if n == N:
        mn = min(mn, val)
        mx = max(mx, val)
        return

    if add > 0:
        dfs(n+1, val+SEQ[n], add - 1, sub, mul, div)

    if sub > 0:
        dfs(n+1, val-SEQ[n], add, sub-1, mul, div)

    if mul > 0:
        dfs(n+1, val * SEQ[n], add, sub, mul-1, div)

    if div > 0:
        dfs(n+1, int(val/SEQ[n]), add, sub, mul, div-1)



if __name__ == '__main__':
    # [0] 입력
    input = sys.stdin.readline
    N = int(input().rstrip())   # 수열 길이
    SEQ = list(map(int, input().rstrip().split()))
    add, sub, mul, div = map(int, input().rstrip().split())

    mn, mx = int(1e9), int(-1e9)

    dfs(1, SEQ[0], add, sub, mul, div)

    print(mx)
    print(mn)

