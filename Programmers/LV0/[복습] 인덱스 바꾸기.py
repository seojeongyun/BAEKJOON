'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120895
'''

def solution(my_string, num1, num2):
    lst = list(my_string)
    tmp = lst[num1]
    lst[num1] = lst[num2]
    lst[num2] = tmp
    answer = ''.join(lst)
    return answer

'''
    * 파이썬에서 swap은 a,b = b,a 로 가능
    def solution(my_string, num1, num2):
        s = list(my_string)
        s[num1],s[num2] = s[num2],s[num1]
        return ''.join(s)
'''