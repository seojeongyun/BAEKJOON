'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120884#
'''

# 서비스 치킨의 수를 return
    # 10마리 -> 11장
    #
def solution(chicken):
    answer = 0
    coupon = 0
    remain = 0
    if chicken < 10:
        return chicken

    while chicken > 0:
        coupon = chicken
        chicken = coupon // 10
        coupon = coupon % 10 if coupon % 10 != 0 else 1
        remain += coupon
        if remain >= 10:
            chicken += remain // 10
            remain %= 10
        answer += chicken

    return answer

print(solution(1081))

'''
    def solution(chicken):
        answer = 0
        coupon = chicken
    
        while coupon >= 10:
            service = coupon // 10
            answer += service
            coupon = service + coupon % 10
    
        return answer
'''

'''
    def solution(chicken):
        output = 0
    
        while chicken >= 10:
            output += chicken // 10
            chicken = chicken // 10 + chicken % 10
    
        return output
'''