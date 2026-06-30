'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120882#
    [1] index 함수는 가장 먼저 마주한 값의 index를 return해주기 때문에 동석차 계산에 유리하다.
'''


def solution(score):
    answer = []
    tmp = []
    copied_score = sorted(score, key=lambda x: (x[0] + x[1]), reverse=True)

    for i, score_lst in enumerate(copied_score):
        if sum(copied_score[i]) == sum(copied_score[i - 1]) and i != 0:
            tmp.append([tmp[i - 1][0], copied_score[i]])
        else:
            tmp.append([i + 1, copied_score[i]])

    for score_lst1 in score:
        for order, score_lst2 in tmp:
            if score_lst1 == score_lst2:
                answer.append(order)

    print(answer)
    # for i, v in tmp:
    #     print(i, v)
    return answer

'''
    def solution(score):
        a = sorted([sum(i) for i in score], reverse = True)
        return [a.index(sum(i))+1 for i in score]
'''

'''
    def solution(score):
        rank = sorted([sum(s) / 2 for s in score], reverse=True)
        rankDict = {}
        for i, r in enumerate(rank):
            if r not in rankDict.keys():
                rankDict[r] = i + 1
        return [rankDict[sum(s) / 2] for s in score]
'''