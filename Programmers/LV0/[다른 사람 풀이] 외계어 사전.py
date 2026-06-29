'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120869
'''

import itertools
def solution(spell, dic):
    # permutation
    result = itertools.permutations(spell)
    for rst in result:
        if ''.join(rst) in dic:
            return 1
    else:
        return 2


'''
    def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2
    
    # 집합의 특성을 활용
'''