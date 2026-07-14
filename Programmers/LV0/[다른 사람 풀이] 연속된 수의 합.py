'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120923
'''


# 투포인터
def solution(num, total):
    answer = []
    lst = []
    for i in range(-100, 1000):
        lst.append(i)

    start = 0
    end = num
    while sum(lst[start:end]) != total:
        if sum(lst[start:end]) != total:
            start += 1
            end += 1

    answer = lst[start:end]
    return answer

'''
    # 다른 풀이를 참고한 나의 풀이
    # 핵심은 기본 수열에 offset을 얼마나 더해줄 거냐
    # offset을 구하는 방식: 예시 total = 15, n = 3
    # 15에서 sum(1~3)를 빼면 9가 남는데, 이 9는 3개의 원소(1,2,3)에 각각 3씩 더해주면 만들어지는 차이이므로,
    # offset은 (total - sum(1~n)) // n 이 된다.
    
    def solution(num, total):
        answer = []
        
        # 기본 수열
        lst = []
        for i in range(1, num+1):
            lst.append(i)
            
        # offset 계산
        summation = sum(lst)
        diff = total - summation
        offset = diff // num
        
        for i in lst:
            answer.append(i+offset)
        return answer
'''