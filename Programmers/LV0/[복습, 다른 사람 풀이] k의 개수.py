'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120887
    [1] str1.count(str2): str1에 들어있는 str2의 개수 return
'''

def solution(i, j, k):
    # i부터 j까지 k가 몇 번 등장하는지
    answer = 0
    for val in range(i, j+1):
        answer += str(val).count(str(k))
    return answer

'''
    def solution(i, j, k):
        answer = 0
        for n in range(i, j + 1):
            answer += str(n).count(str(k))
        return answer
'''