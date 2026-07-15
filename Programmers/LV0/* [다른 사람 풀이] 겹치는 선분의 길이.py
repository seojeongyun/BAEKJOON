'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120876#
'''


def solution(lines):
    answer = 0
    lst = []
    for line in lines:
        start, end = line
        for i in range(start, end):
            lst.append(i + 1)
    # print(lst)
    for i in set(lst):
        if lst.count(i) > 1:
            answer += 1

    return answer


'''
    def solution(lines):
        s1 = set(i for i in range(lines[0][0], lines[0][1]))
        s2 = set(i for i in range(lines[1][0], lines[1][1]))
        s3 = set(i for i in range(lines[2][0], lines[2][1]))
        return len((s1 & s2) | (s2 & s3) | (s1 & s3))
'''