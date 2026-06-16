'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120893
    isupper() / islower() / upper() / lower() / swapcase(): 대 <-> 소 문자 변환
'''
def solution(my_string):
    answer = ''
    for char in my_string:
        if char.isupper():
            answer += char.lower()
        if char.islower():
            answer += char.upper()

    return answer