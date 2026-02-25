'''
    N: 짝수
    - N/2로 스타트팀과 링크팀 나눔
        - 각 팀 별로 능력치 부여됨
            - 예를 들어 1,2번 팀이 스타트 팀 / 3,4번이 링크 팀일 경우
                - S12 + S21이 스타트 팀의 능력치
                - S34 + S43이 링크 팀의 능력치
    - 두 팀의 능력치 차이가 최솟값을 구하시오.

    [고려할 점]
    - 팀원 수가 2를 초과하는 경우
        - 예를 들어, 1,2,3이 스타트팀인 경우 -> S12, S13, S23, S21, S31, S32를 더해야 함
        - 3개 중 2개 뽑아 줄 세우기 = (N/2 Comb 2)!

    [접근법]
    - itertools
    - 백트래킹
'''

def calc(alst, blst):
    a_val = b_val = 0

    # for i in alst:
    #     for j in alst:
    #         a_val += MAP[i][j]
    #
    # for i in blst:
    #     for j in blst:
    #         b_val += MAP[i][j]

    for i in range(N//2):
        for j in range(N//2):
            a_val += MAP[alst[i]][alst[j]]
            b_val += MAP[blst[i]][blst[j]]

    return abs(a_val - b_val)

def dfs(n, alst, blst):
    global answ
    # [1] 종료 조건 및 정답 처리
    if n == N:
        if len(alst) == len(blst):
            answ = min(answ, calc(alst, blst))
        return

    # [2-1] A팀인 경우
    dfs(n+1, alst+[n], blst)

    # [2-2] B팀인 경우
    dfs(n+1, alst, blst+[n])

import sys
# sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input().rstrip())
    MAP = [list(map(int, input().rstrip().split())) for _ in range(N)]

    # 변수 선언
    answ = 10000

    # 백트래킹 함수 호출
    dfs(0, [], [])

    print(answ)