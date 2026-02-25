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

    # jobs = [[요청 시간, 소요 시간, 작업 번호]]
    for i in range(len(jobs)):
        jobs[i].append(i)
    jobs.sort(key = lambda x : x[0])
    #
    process = deque()
    q = []
    time = 0

    while True:
        # 대기 큐에 들어갈 job 번호 저장
        job_num = []
        # 반복문 종료 조건
        if not len(jobs) and not len(q) and not len(process):
            break

        # 요청 시간이 되면 대기큐에 추가
        # 요청 시간이 같은 job이 여러개인 경우를 처리하기 위해 for문으로 순회
        for i, job in enumerate(jobs):
            if len(job) > 0 and job[0] == time:
                job_num.append(i)

        # 대기큐에 삽입할 job이 있는 경우, q에 넣고 정렬
        if len(job_num):
            for i in range(len(job_num)):
                q.append(jobs.pop(0))
            # 대기큐 정렬
            # jobs = [[요청 시간, 소요 시간, 작업 번호]]
            q.sort(key=lambda x: (x[1], x[0], x[2]))

        # 프로세스 종료
        if len(process) > 0 and time == process[0][-1] + process[0][0][1]:
            answ.append(time - process[0][0][0])
            process.pop()

        # 프로세스 추가
        if len(q) > 0 and not len(process):
            process.append([q.pop(0), time])

        time += 1

    answer = int(sum(answ) / len(answ))
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