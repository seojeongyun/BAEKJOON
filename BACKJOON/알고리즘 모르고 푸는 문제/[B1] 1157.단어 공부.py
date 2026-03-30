'''
    https://www.acmicpc.net/problem/1157

    2 / 128

    알파벳 대소문자로 된 단어가 주어지면,
    이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내시오

    대소문자 구분 X, 여러개일 경우 ? 출력
'''

import sys
from collections import defaultdict

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    string = input().strip()
    cnter = defaultdict(int)

    for alphabet in string:
        alpha = alphabet.lower()
        cnter[alpha] += 1

    max_val, max_k = -1, -1
    for k, v in cnter.items():
        if max_val < v:
            max_val = v
            max_k = k

    for k in cnter.keys():
        if k != max_k and max_val == cnter[k]:
            print('?')
            break
    else:
        print(max_k.upper())

'''
TC1
ab
'''