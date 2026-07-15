'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120815
    두 수의 곱을 최대공약수(GCD)로 나누면 최소공배수(LCM) 가 됩니다.
'''

# 6과 n의 최소 공배수 구하기
def solution(n):
    for i in range(1, n*100):
        if i % n == 0 and i % 6 == 0:
            return i // 6

'''
    # math 라이브러리 없이 lcm 구하는 best 방법
    
    def solution(n):
        def gcd(a, b):
            while b > 0:
                a, b = b, a%b
            return a
    
        return n // gcd(n, 6)
        
        
    a=10, b=6

    a,b = 6, 10%6
         = 6,4    
    a,b = 4, 6%4
         = 4,2
    a,b = 2, 4%2
         = 2,0  
'''