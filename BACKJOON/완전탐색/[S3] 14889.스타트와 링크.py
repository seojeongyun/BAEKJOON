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

import sys

def start_permutation(start_permutation_len, start_permutation_lst):
    if start_permutation_len == 2:
        if not start_permutation_lst[::-1] in start_permutation_answ:
            start_permutation_answ.append(start_permutation_lst)
        return

    for i in start:
        if i not in start_permutation_lst:
            if start_permutation_lst+[i] not in start_permutation_answ:
                start_permutation(start_permutation_len+1, start_permutation_lst+[i])

def link_permutation(link_permutation_len, link_permutation_lst):
    if link_permutation_len == 2:
        if not link_permutation_lst[::-1] in link_permutation_answ:
            link_permutation_answ.append(link_permutation_lst)
        return

    for i in link:
        if i not in link_permutation_lst:
            if link_permutation_lst+[i] not in link_permutation_answ:
                link_permutation(link_permutation_len+1, link_permutation_lst+[i])

def combination(combination_len, combination_lst):
    if combination_len == N//2:
        NOT_IN = False
        for answer in combination_answ:
            if sorted(combination_lst) == sorted(answer):
                NOT_IN = True
                break

        if not NOT_IN:
            combination_answ.append(combination_lst)
        return

    for i in range(1, N+1):
        if i not in combination_lst:
            combination(combination_len+1, combination_lst+[i])

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input().rstrip())
    lst = list(range(1, N + 1))
    MAP = [list(map(int, input().rstrip().split())) for _ in range(N)]

    # 변수 선언
    combination_answ = []
    #
    combination_lst = []
    link_permutation_lst = []
    start_permutation_lst = []
    #
    combination(0, combination_lst)
    print()
    ref = set(range(1, N+1))
    #
    min_val = 200
    #
    for comb in combination_answ:
        start_val = 0
        link_val = 0
        #
        start = comb
        link = list(ref - set(start))
        #
        start_permutation_answ = []
        link_permutation_answ = []
        #
        start_permutation(0, start_permutation_lst)
        link_permutation(0, link_permutation_lst)
        # print()
        #
        for i, j in start_permutation_answ:
            start_val += MAP[i-1][j-1]
            start_val += MAP[j-1][i-1]

        for i, j in link_permutation_answ:
            link_val += MAP[i-1][j-1]
            link_val += MAP[j-1][i-1]

        # print(abs(start_val-link_val))
        min_val = min(min_val, abs(start_val-link_val))

    print(min_val)

