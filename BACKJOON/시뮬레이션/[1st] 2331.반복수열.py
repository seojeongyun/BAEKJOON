'''
    D[1] = A
    D[n] = D[n-1]의 각 자리의 숫자를 P번 곱한 수들의 합

    EX) A = 57, P = 2
        수열 D는 [57, 74(5^P(==2) + 7^P(==2) = 25 + 49), 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37, 58, .. ]
                                                                |---------------------------|   |-------..
                                                                            반복
    출력: 반복되는 부분을 제외했을 때 수열에 남게되는 수의 개수
'''


import sys

def decomp(num):
    lst = []

    while num >= 10:
        lst.append(num % 10)
        num //= 10

    lst.append(num)
    return lst

if __name__ == '__main__':
    ANSW = []
    input = sys.stdin.readline

    # [0] 입력
    A, P = map(int, input().rstrip().split())
    ANSW.append(A)

    while True:
        result = 0 # 다음 수를 담는 변수
        lst = decomp(A) # 한 자리씩 분해
        for num in lst:
            result += num ** P  # 다음 수 구하기

        if result not in ANSW:  # 처음 등장하는 수면 ANSW에 추가
            ANSW.append(result)
            A = result
        else:                   # 중복 등장하면 브레이크
            break

    for idx, num in enumerate(ANSW):        # 중복 숫자 위치 찾기
        if num == result:
            print(len(ANSW[:idx]))
            break


