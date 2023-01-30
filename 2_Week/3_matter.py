def solution(n):
    n= list(str(n))
    n.sort(reverse=True)
    answer = "".join(n)
    return answer

print(solution(118372))


def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))
print(solution(118372))
