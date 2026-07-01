'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120878#
    * 정수도 유한소수임을 간과
'''


# 기약분수: 더 이상 약분할 수 없는 분수
# a, b의 최대공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(a, b):
    gcd_val = gcd(a, b)
    A, B = a // gcd_val, b // gcd_val

    # 정수도 유한소수이므로 정수인 경우에도 1을 return
    if A%B == 0:
        return 1

    # B의 소인수가 2와 5만 존재하는지 판단
    i = 2
    while True:
        if i == B:
            break

        if B % i != 0:
            i += 1
        else:
            if i != 2 and i != 5:
                return 2
            B //= i
    if i == 2 or i == 5:
        return 1
    else:
        return 2

solution(7,20)