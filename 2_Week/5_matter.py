# 예산 - Summer/Winter Coding(~2018)
import random

def solution (d, budget):
    d.sort()
    result = 0
    if sum(d) == int(budget):
        result = len(d)
    else:
        for i in range(1,len(d)):
            if sum(random.sample(d,i)) > int(budget):
                result = int(i)
    return result


print(solution([2,2,3,3],10))
print(solution([1,3,2,5,4],9))

d = [1,2,3,4,5]
print(sum(random.choices(d,k = 2)))

def solution2(d, budget):
    answer = 0

    d = sorted(d)

    for i in range(len(d)) :
        if budget >= d[i] :
            budget -= d[i]
            answer += 1

    return answer