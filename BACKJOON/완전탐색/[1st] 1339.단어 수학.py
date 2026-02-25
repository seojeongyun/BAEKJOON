'''
    * 그리디 서치

    https://www.acmicpc.net/problem/1339

    2 / 256

    단어 수학 문제
        -N개의 단어로 구성
            - 알파벳 대문자

        - 각 대문자를 0~9 사이의 숫자중 하나로 바꿔서 N개의 수 합하기

    입력
        단어의 개수 N(1 ≤ N ≤ 10), 대문자로만 구성, 수의 길이는 최대 8
        N개의 줄에 단어가 한 줄에 하나

    출력
        단어의 최댓값
'''

import sys

def find_weight(lst):
    for i, alpha in enumerate(lst):
        weight_dict[alpha] += 10**(len(lst)-(i)-1)

if __name__ == '__main__':
    input = sys.stdin.readline
    weight_dict = {}
    answ = 0

    # [0] 입력
    N = int(input().strip())
    input_lst = []
    for _ in range(N):
        str_ = input().strip()
        for alpha in str_:
            weight_dict.setdefault(alpha, 0)
        input_lst.append(str_)

    # [1] 문자 별 가중치 구하기
    for lst in input_lst:
        find_weight(lst)

    weight_dict=dict(sorted(weight_dict.items(), key=lambda x: -1*x[1]))

    # [2] 가중치 별로 숫자 대입
    for i, v in enumerate(weight_dict.values()):
        answ += v * (9-i)

    print(answ)
'''
    TC 1
    GCF + ACDEB
    A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7라고 하면
    두 수의 합은 99437(784 + 98654)으로 최대
'''