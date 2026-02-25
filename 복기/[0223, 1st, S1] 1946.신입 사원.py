'''
    https://www.acmicpc.net/problem/1946

    2 / 256

    다른 모든 지원자와 비교했을 때 서류 심사 성적과 면접 시험 성적 중
    적어도하나가 다른 지원자보다 떨어지지 않는 자만 선발

    채용 가능한 인원 수

    입력:
        - 첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)
        - 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)
        - 둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다.
        - 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정

    출력:
        - 채용 가능한 신입사원 최대 인원 수
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = []

    # [0] TC 입력
    TC = int(input().strip())

    for _ in range(TC):
        # [1] DATA 입력
        N = int(input().strip())
        score = [list(map(int, input().strip().split())) for _ in range(N)]

        # [2] 정렬
        # i번째 사람을 기준으로, i번째 사람은 이후에 올 사람들보다 서류 점수가 높다.
        # 반면 이전에 오는 사람들에게는 서류 점수가 지니까, 면접 점수를 이겨야한다.
        #
        score.sort()

        # [2] 비교
        top_interview_score = score[0][1]
        tc_answ = 1

        for _, interview_score in score:
            if top_interview_score > interview_score:
                top_interview_score = interview_score
                tc_answ += 1

        answ.append(tc_answ)

    for cnt in answ:
        print(cnt)