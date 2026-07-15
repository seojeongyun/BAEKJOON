'''
    https://school.programmers.co.kr/learn/courses/30/lessons/181864
    [1] 두 문자를 swap하는 경우 tmp를 활용한 value swap처럼 다른 문자를 거치면 됨.
    [2] ~면 1을 아니면 0을 return하는 문제에서 int() 활용 가능
'''


def solution(myString, pat):
    mystring = ''
    for char in myString:
        if char == 'A':
            mystring += 'B'
        else:
            mystring += 'A'

    if mystring.find(pat) != -1:
        return 1
    else:
        return 0


'''
def solution(myString, pat):
    return int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))
'''


'''
def solution(myString, pat):
    return int(''.join(['A' if i == 'B' else 'B' for i in pat]) in myString)
'''