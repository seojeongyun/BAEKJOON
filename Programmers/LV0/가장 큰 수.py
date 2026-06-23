'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120899
    가장 큰 수와 그 수의 인덱스를 담은 배열을 return

    def solution(array):
        answer = [max(array), array.index(max(array))]
        return answer

    위 처럼 풀었는데, max, index 함수 안 쓰고 풀어보기
'''

def solution(array):
    max_val, index = -1, -1
    for i,num in enumerate(array):
        if max_val < num:
            max_val = num
            index = i
    return [max_val, index]