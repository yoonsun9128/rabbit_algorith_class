def solution(n, lost, reserve):
    answer = 0
    for i in range(1,n+1):
        for a in reserve:
            if int(a)-1 <= int(i) <= int(a)+1 :
                answer +=1
        for b in lost:
            if b == i:
                answer -=1

    return answer

print(solution(5,[2, 4]	,[1, 3, 5]))
print(solution(5,[2, 4],[3]))
print(solution(3,[3],[1]))
