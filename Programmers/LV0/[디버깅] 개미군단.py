def solution(hp):
    ants = 0
    for i in [5,3,1]:
        ants += hp // i
        hp -= ants*i
    return ants

print(solution(23))