'''
    자연수 N과 M
        - 1부터 N까지 자연수 중에 중복 없이 M개 고른 수열을 모두 구하시오

    출력: 공백으로 구분, 사전순으로 증가하는 순서
'''

import sys

def dfs(n, lst):
    # [1] 종료 조건 및 정답 처리
    if n == M:
        ANSW.append(lst)
        return ANSW

    # [2] 하부 함수 호출
    for i in range(1, N+1):
        # not in은 시간 복잡도 O(N)
        # visited 배열 활용
        # if i not in lst:
        if V[i] == 0:
            V[i] = 1 # 방문
            dfs(n+1, lst+[i]) # 사용 후
            V[i] = 0 # 클리어

if __name__ == '__main__':
    input = sys.stdin.readline
    ANSW = []

    # [0] 입력
    N, M = map(int, input().rstrip().split())

    # [1] 백트래킹
    lst = []
    V = [0] * (N+1)
    dfs(0, lst)

    for answ in ANSW:
        print(*answ)

