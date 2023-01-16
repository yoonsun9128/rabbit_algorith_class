def solution(a):
    a = int(a)
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(solution(3))