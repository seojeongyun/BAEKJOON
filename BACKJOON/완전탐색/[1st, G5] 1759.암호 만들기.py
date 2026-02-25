'''
    https://www.acmicpc.net/problem/1759

    2 / 128

    암호
        - 서로 다른 L개의 알파벳 소문자로 구성
        - 최소 한 개의 모음(a, e, i , o , u)
        - 최소 두 개의 자음으로 구성
        - 알파벳이 증가하는 순서로 배열 (abc는 가능, bac는 아님)

    암호로 사용했을 법한 문자의 종류 C가지

    C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호를 모두 구하시오

    입력:
        - 첫째 줄에 두 정수 L, C (3 <= L <= C <= 15)
        - 다음 줄에는 C개의 문자들이 공백으로 주어짐

    출력:
        각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력
'''

import sys

def dfs(lst):
    # 종료 조건 및 정답 처리
    if len(lst) == L:
        password = ''.join(lst)
        v.setdefault(password, 0)
        if not v[password]:
            v[password] = 1
            answ.append(password)
        return

    # 하부 함수 호출
    for char in data:
        if not v[char]:
            if len(lst) == 0:
                v[char] = 1
                dfs(lst+[char])
                v[char] = 0

            else:
                if lst[-1] < char:
                    v[char] = 1
                    dfs(lst + [char])
                    v[char] = 0

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = []
    aeiou = ('a','e','i','o','u')

    # [0] 입력
    L, C = map(int, input().strip().split())
    data = list(map(str, input().strip().split()))

    # [1] 백트래킹
    v = {}
    for char in data:
        v[char] = 0
    dfs([])

    # [2] 정답 처리
    answ.sort()
    for password in answ:
        condition1 = False
        condition2 = 0
        for char in password:
            if char in aeiou:
                condition1 = True
                condition2 += 1

        if condition1 and len(password) - condition2 > 1:
            print(password)



# 두 개의 자음
'''
TC1
4 6
a t c i s w

3 3
e c t

3 6
c t w a g e
'''
