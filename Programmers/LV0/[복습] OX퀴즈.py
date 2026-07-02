'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120907
    [1] eval 함수의 취약점: 코드를 동적으로 처리할 수 있다는 장점이 있지만, 악의적인 코드를 실행할 가능성도 존재
    ex) 외부에서 'rm -rf *'같은 문자열이 들어온다고 할 때 이를 실행하게 될 가능성이 있음
    -> eval은 현업에서 사용하지 않는 코드
'''


def solution(quiz):
    answer = []

    for q in quiz:
        if str(eval(q.split('=')[0])) == q.split('=')[-1].strip():
            answer.append("O")
        else:
            answer.append("X")
    return answer