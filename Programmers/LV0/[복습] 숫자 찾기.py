'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120904
    [1] list.index(): 매개변수로 숫자 or str 가능
    [2] str.index() : 매개변수로 str만 가능
'''

def solution(num, k):
    if str(k) in str(num):
        # num의 자리수
        return str(num).index(str(k))+1
    else:
        return -1

'''
    내 풀이
    
'''