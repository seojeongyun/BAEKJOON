'''
    https://school.programmers.co.kr/learn/courses/30/lessons/181888
    [1] 슬라이싱: lst[시작번호:끝번호:간격]
'''

def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i])
    return answer

'''
def solution(num_list, n):
    return num_list[::n]
'''