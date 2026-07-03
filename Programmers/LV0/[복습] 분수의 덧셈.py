'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120808
'''


def gdc(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(numer1, denom1, numer2, denom2):
    # 분수의 덧셈
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2

    # 기약분수: 분자 분모의 최대공약수(gdc)로 나누기
    gdc_val = gdc(numer, denom)
    return [numer // gdc_val, denom // gdc_val]

'''
    # 최대 공약수 구하는 방법 [1]: 이게 더 직관적
        - 둘 중에 더 작은 것을 골라서 큰 값 -> 0으로 반복하며 둘 다 나눌 수 있는 값 찾기
    for i in range(min(denum0,num0),0,-1):
            if denum0%i == 0 and num0%i == 0:
                s = i
                break
                
    # 최대 공약수 구하는 방법 [2]
    def gcd(a,b):
        while b > 0:
            a, b = b, a%b
        return a
'''