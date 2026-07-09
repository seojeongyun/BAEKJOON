'''
    https://school.programmers.co.kr/learn/courses/30/lessons/181844
    [1] arr에서 요소 제거하기: del arr[idx], arr.remove(값)
        - arr에 [1,2,2,3]이 들어오고 delete_list에 [2] 가있으면 2가 한번만 지워져서 결과값이 [1,2,3]
        - 문제에서 제한사항으로 arr 요소 값이 모두 다르다는 전제 때문에 맞는 풀이이지만
        - 지우는 방법보단 not in으로 없는 걸 추가하는 방법이 안
'''

def solution(arr, delete_list):
    for d in delete_list:
        if d in arr:
            del arr[arr.index(d)]
    return arr


'''
    def solution(arr, delete_list):
        return [i for i in arr if i not in delete_list]
'''