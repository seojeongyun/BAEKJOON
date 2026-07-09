'''
    https://school.programmers.co.kr/learn/courses/30/lessons/181910
    [1] 리스트 슬라이싱에서 lst[-n:] = lst[len(lst)-n:]과 같다
'''

def solution(my_string, n):
    answer = ''.join(list(my_string)[len(my_string)-n:])
    return answer