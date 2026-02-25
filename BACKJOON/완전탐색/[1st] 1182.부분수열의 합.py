'''
    https://www.acmicpc.net/problem/1182

    2 / 256

    N개의 정수로 이루어진 수열
        크기가 양수인 부분수열 중 그 수열의 원소 합이 S가 되는 경우의 수 구하기

    * 1 <= N <= 20
    * |S| <= 1,000,000
'''

import sys

# 부분 수열로 연속된 수만 고른 경우
# if __name__ == '__main__':
#     input = sys.stdin.readline
#     answ = 0
#
#     # [0] 입력
#     N, S = map(int, input().strip().split())
#     lst = list(map(int, input().strip().split()))
#
#     # [1] 완탐
#     start = 0
#     while start <= len(lst):
#         tlst = []
#         for idx in range(start, len(lst)):
#             tlst.append(lst[idx])
#             if sum(tlst) == S:
#                 answ += 1
#         start += 1
#
#     print(answ)

# def dfs(lst):
#     global answ, S
#     # 정답 처리: 길이가 1 이상인 lst의 합이 S와 같다.
#     if len(lst) > 0:
#         if sum(lst) == S:
#             print(lst)
#             answ += 1
#
#     # 종료 조건: lst의 길이가 len(seq)와 같다.
#     for num in seq:
#         if not v[num] and len(lst) > 0 and (lst[-1] < num or num == 0):
#             v[num] = 1
#             dfs(lst+[num])
#             v[num] = 0


# if __name__ == '__main__':
#     input = sys.stdin.readline
#     answ = []
#
#     # [0] 입력
#     N, S = map(int, input().strip().split())
#     seq = list(map(int, input().strip().split()))
#
#     # [1] 백트래킹
#     v = [0] * 100001
#     dfs([])
#
#     # [2] 출력
#     print(len(answ))
#     print(answ)

def combination(lst, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(lst)):
        elem = lst[i]
        rest_lst = lst[i + 1:]
        for C in combination(rest_lst, n - 1):
            result.append([elem] + C)

    return result

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0

    # [0] 입력
    N, S = map(int, input().strip().split())
    seq = list(map(int, input().strip().split()))

    # a = combination(seq, 2)
    # print(a)
    for i in range(len(seq)+1):
        candidate = combination(seq, i)
        for cand in candidate:
            if sum(cand) == S and len(cand) > 0:
                answ+=1
                # print(cand)

    print(answ)
'''
    TC1
    1 1
    1
    
    TC2
    5 -2
    -2 -2 -2 -2 -2
    
    TC3
    5 -2
    5 -7 5 2 -4
    
    TC4
    10 1000000
    100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
    
    TC5
    15 499999
    100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 499999 0 2919 2910 4 18
    
    TC6
    15 499999
    100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000 100000
    
    TC7
    2 9
    1 1
    
    TC8
    
'''