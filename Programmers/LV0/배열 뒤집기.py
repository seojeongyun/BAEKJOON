'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120821

    배열 뒤집기
'''

def solution(num_list):
    answer = []
    for i in range(len(num_list)-1, -1, -1):
        answer.append(num_list[i])
    return answer