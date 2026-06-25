'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120913
'''

def solution(my_str, n):
    answer = []
    lst = list(my_str)
    i = 0
    while True:
        answer.append(''.join(lst[i*n: i*n+n]))
        if i * n + n >= len(lst):
            break
        i += 1
    return answer

'''
    TC마다 문자열 길이가 달라서 for문 구성이 어렵겠다 판단해 while문을 사용했는데 step을 n으로 주면 됐음
    def solution(my_str, n):
        return [my_str[i: i + n] for i in range(0, len(my_str), n)]
'''
