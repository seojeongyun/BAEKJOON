'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120898
'''

def solution(message):
    return len(message) * 2

'''
    def solution(message):
    return len(message) << 1
'''

'''
    2² → 2³
    2¹ → 2²
    2⁰ → 2¹
    왼쪽으로 한 칸 옮기면 모든 자리수가 2배
'''