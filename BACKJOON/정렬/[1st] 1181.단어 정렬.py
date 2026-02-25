'''
    2초/256

    N개의 단어
        각 단어는 알파벳 소문자로 구성

    정렬
        1. 길이가 짧은 것
        2. 길이 같으면 사전 순

    중복된 단어는 하나만 남기고 제거
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N = int(input().strip())
    lst = []

    for i in range(N):
        lst.append(input().strip())

    answ = list(set(lst))
    answ.sort(key=lambda x: (len(x), x))

    for word in answ:
        print(word)

'''
    시간 복잡도:
        lst 생성 O(N)
        정렬 O(NlogN * L): 정렬 * 문자열 길이
'''