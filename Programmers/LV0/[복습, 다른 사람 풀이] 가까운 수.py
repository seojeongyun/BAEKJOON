'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120890
'''

def solution(array, n):
    # 가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.
    array.append(n)
    array.sort()
    i = array.index(n)
    #
    if i == len(array)-1:
        return array[i-1]
    elif i == 0:
        return array[i+1]
    else:
        left, right = array[i-1], array[i+1]
        if array[i] - left < right - array[i]:
            return left
        elif array[i] - left > right - array[i]:
            return right
        else:
            return left

'''
    내 풀이는 너무 조건문. 더 간결하게 풀것
    def solution(array, n):
        # 가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.
        array.sort(key=lambda x: (abs(x-n), x-n)) // 여기서 x-n 안 넣어주면 가까운 수가 여러개인 경우 더 작은 수가 우선 순위로 정렬되지 않게 되어 오답이됨
        return array[0]
'''