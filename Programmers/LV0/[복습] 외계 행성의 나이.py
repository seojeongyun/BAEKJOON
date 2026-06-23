'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120834
    [1] list.reverse()의 return 값은 None이고 list 자체를 뒤집는다.
    [2] reverse() 대신  [::-1] 로 슬라이싱 해도 뒤집힌다.
'''

def solution(age):
    return ''.join([chr(97 + int(num)) for num in str(age)])

