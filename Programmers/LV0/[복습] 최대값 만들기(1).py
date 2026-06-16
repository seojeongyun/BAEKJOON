'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120847

    리스트에서 두 개 뽑기
'''
def solution(numbers):
    max_val = -1
    # Combination
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            max_val = max(max_val, numbers[i]*numbers[j])
    answer = max_val
    return answer