'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120816
    피자 조각 수와 사람 수가 주어질 때 인당 한 조각 이상 먹기 위한 피자의 최소 개수
'''

def solution(slice, n):
    answer = int(n//slice)+1 if int(n%slice)!=0 else int(n/slice)
    return answer

for slice, n in ((7,10), (4,12)):
    print(solution(slice,n))