'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120924#
'''

# 수열 내에 0이 있는 경우를 고려해서 아래와 같이 풀이

def solution(common):
    # 등차면
    if common[2] - common[1] == common[1] - common[0]:
        return common[-1] + common[-1] - common[-2]
    # 문제에서 공비는 0이 아닌 정수라고 했으므로 등비 수열 파트는 아래 주석처럼 풀이 가능
    # elif common[2] / common[1] == common[1] / common[0]:
    #     return common[-1] * common[2] / common[1]

    # 등비면
    else:
        lst = []
        i = 0
        while len(lst) < 2:
            if common[i] != 0:
                lst.append(common[i])
            else:
                lst = []
            i += 1
        r = common[-1] // common[-2]
        return common[-1] * r
