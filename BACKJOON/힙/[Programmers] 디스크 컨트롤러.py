'''
    https://school.programmers.co.kr/learn/courses/30/lessons/42627

    우선순위 디스크 컨트롤러
        - 작업의 번호, 요청 시각, 소요 시간을 저장해두는 대기 큐 존재
            - 큐는 처음에 비어있음
        - 하드 디스크가 작업을 하지 않고 대기 큐가 비어있지 않으면 우선순위가 높은 작업을 대기큐에서 꺼내 작업
            - 우선 순위: 소요 시간 짧고, 요청 시각 빠르고, 작업 번호가 작은 것 순
        - HDD는 한 번 작업을 시작하면 그 작업을 마칠 때 까지 그것만 함
        - 작업을 마치는 시점과 다른 작업 요청이 들어오는 시점이 겹친다면,
          작업을 마치자 마자 디스크 컨트롤러는 요청이 들어온 작업을 대기 큐에 저장한 뒤,
          우선 순위가 높은 작업을 대기 큐에서 꺼내 하드디스크에게 작업을 시킴
        - 작업 마치는 시점에 다른 게 들어오지 않더라도, 작업을 마치자마자 또 다른 작업을 시작할 수 있고 이 과정에서 걸리는 시간은 없음


    입력:
        [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 정수 배열
    출력:
        모든 요청 작업의 반환 시간의 평균
'''

import sys
from collections import deque

def solution(jobs):
    answer = 0
    answ = []
    processes = []
    for i, lst in enumerate(jobs):
        lst.append(i)
        processes.append(lst)

    # python은 stable sort라서 소요시간, 요청 시각을 기준으로 정렬하면 작업번호 빠른 순은 알아서 보장됨
    # 처음 jobs에서 작업 번호가 인덱스로 정렬되어 제공되기 때문
    processes.sort(key=lambda x: (x[1], x[2], x[0]))
    q = deque(processes)
    time = q[0][0]
    while q:
        process = q.popleft()
        if process[0] > time:
            time = process[0]
        time += process[1]
        answ.append(time-process[0])

    answer = int(sum(answ) / len(answ))
    print(answ)
    return answer

if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [3, 5]]
    print(solution(jobs))

'''
TC1
[[0, 3], [1, 9], [3, 5]]

TC2
[[2, 4], [13, 7], [5, 3], [5, 10]]

TC3
[[0, 1]]

TC4
[[1,1], [4,1],[6,1],[2,1],[70,1],[22,1],[32,1]] 

'''