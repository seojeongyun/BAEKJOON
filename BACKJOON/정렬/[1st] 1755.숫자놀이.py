'''
    https://www.acmicpc.net/problem/1755

    2 / 128

    79 -> seven nine
    80 -> eight zero
    위와 같은 방식으로 숫자를 영어로 읽게 되면 80이 79보다 사전순으로 먼저 나옴

    M 이상 N 이하의 정수를 조건에 맞게 정렬해 한 줄에 10개 씩 출력

    * 1 <= M <= N <= 99
    * 1 <= L <= 5

    one two three four five six seven eight nine
'''

import sys

def int_2_eng(num):
    if num > 9:
        ten_num = num // 10
        one_num = num % 10
        return int_2_eng_dict[ten_num]+int_2_eng_dict[one_num]

    else:
        one_num = num
        return int_2_eng_dict[one_num]

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    M, N = map(int, input().strip().split())
    lst = []

    # [1] 범위 내 숫자 생성: O(N)
    for val in range(M, N+1):
        lst.append(val)

    # [2] 숫자 -> 영어
    int_2_eng_dict = {
        0:'zero',
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine'
    }

    # [3] 정렬: K는 숫자의 개수
    # key 생성 비용 O(1 * K) = 각 요소에 대해 key 함수 생성되기 때문
    # 정렬 비용 O(KlogK)
    # O(1)은 dict 접근과 두 자릿수 분해 -> 문자열 덧셈
    lst.sort(key=lambda x: int_2_eng(x))


    for i in range(len(lst) // 10 + 1):
        print(*lst[i*10:i*10+10])

