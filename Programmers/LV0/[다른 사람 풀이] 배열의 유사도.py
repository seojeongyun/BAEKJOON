'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120903

    같은 원소의 개수를 return
'''


def solution(s1, s2):
    answer = 0

    for string in s1:
        if string in s2:
            answer += 1

    return answer


'''
    def solution(s1, s2):
        return len(set(s1)&set(s2));

    & 연산을 하면 집합으로 return 되어서 길이를 구하면 개수를 구할 수 있다.
'''
