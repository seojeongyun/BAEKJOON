'''
    https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=python3

    공백으로 구분된 숫자가 있는 문자열 s에서 최소값 최대값을 찾으시오
'''

def solution(s):
    lst = s.split()
    answ = [int(num) for num in lst]
    max_val, min_val = max(answ), min(answ)
    answer = '{} {}'.format(min_val, max_val)
    return answer

if __name__ == '__main__':
    s = "1 2 3 4"
    print(solution(s))


# 다른 풀이
'''
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
'''