#두 정수 사이의 합
def solution(a,b):
    answer = 0
    for i in range(a, b+1):
        answer +=i
        # sum(range(a,b+1))
    return answer
print(solution(3,5))