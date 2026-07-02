'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120880#
'''

def solution(numlist, n):
    numlist.sort(key=lambda x: (abs(x-n), -x))
    return numlist

'''
    def solution(numlist, n):
        numlist.sort(key=lambda x: -(abs(x-n)))
        return numlist[::-1]
        
    초기엔 위의 코드로 풀이했고, 히든TC 2번 빼고 다 맞았어서
    '동일 거리에 대해서는 큰 수를 우선으로 정렬'이라는 기준에 부합한 코드인 줄 알았음.
    알고보니 파이썬 sort 함수의 stable sort 특성에 의해 우연히 맞은 거였음.
'''