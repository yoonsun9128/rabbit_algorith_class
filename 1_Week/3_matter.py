def solution (n):
    num = 0
    for i in str(n):
        num += int(i)
    return num
print(solution(123))