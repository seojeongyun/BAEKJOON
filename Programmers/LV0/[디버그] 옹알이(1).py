'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120956
'''


def solution(babbling):
    answer = 0
    lst = ["aya", "ye", "woo", "ma"]

    for saying in babbling:
        while len(saying) > 0:
            if saying[:len(lst[0])] == lst[0]:
                saying = saying[len(lst[0]):]
            elif saying[:len(lst[1])] == lst[1]:
                saying = saying[len(lst[1])]
            elif saying[:len(lst[2])] == lst[2]:
                saying = saying[len(lst[2])]
            elif saying[:len(lst[3])] == lst[3]:
                saying = saying[len(lst[3])]
            else:
                break
        else:
            answer += 1

    return answer


solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])