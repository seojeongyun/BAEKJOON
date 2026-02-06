'''
    https://www.acmicpc.net/problem/1431

    2 / 128

    시리얼 번호
        - 알파벳 대문자 (A-Z)
        - 숫자 (0-9)

    정렬 기준
        - 길이가 짧은 것
        - 길이가 같다면, 자리수의 합이 작은 것이 우선
        - 사전순, 숫자가 알파벳보다 사전순으로 작다.

    출력: 정렬된 시리얼 번호
'''

import sys

def summation(lst):
    rslt = 0
    for char in lst:
        if char.isdigit():
            rslt += int(char)

    return rslt

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N = int(input().rstrip())
    lst = [input().rstrip() for _ in range(N)]

    # [1] 정렬: O(Nlog N * L) -> 여기서 L이 summation(x)에서의 O(L)
    lst.sort(key=lambda x: (len(x), summation(x), x))

    for answ in lst:
        print(answ)


'''
    시간 복잡도: O(N * NlogN * L)
'''