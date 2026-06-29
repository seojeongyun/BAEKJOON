'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120902#
    [1] eval(expression): 매개변수로 받은 expression (=식)을 문자열로 받아서, 실행하는 함수
        - eval("1+2")이면 3을 return
    [2] for문 step 적극 활용
'''


'''
[1]
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
* -를 +-로 바꾸고 +로 split 해버려서 음수 만드는거
* 5 - 8 = 5 + (-8)로 바꿔서 싹 더해버린다
'''