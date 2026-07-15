'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120835
'''

def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)
    for v in emergency:
        answer.append(sorted_emergency.index(v)+1)
    return answer

'''
    # 위 코드는 O(N^2)이라서 딕셔너리 쓰는 게 좋다
    def solution(emergency):
        answer = []
        sorted_emergency = sorted(emergency, reverse=True)
        dict_ = {k:v+1 for v, k in enumerate(sorted_emergency)}
        for v in emergency:
            answer.append(dict_[v])
        return answer
'''
