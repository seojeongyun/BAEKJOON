'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120851
    isdigit(): 주어진 문자가 숫자인지 판별하는 함수
'''

def solution(my_string):
    answer = 0
    for char in my_string:
        if char.isdigit():
            answer += int(char)
    return answer