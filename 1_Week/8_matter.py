def solution(a,b):
    result = 0
    for i in range(a,b+1):
        print("sss", i)
        count = 0
        for x in range(1,i+1):
            if int(i) % int(x) == 0:
                count+=1
        if count % 2 == 0:
            result += i
        else:
            result -= i
    return result

print(solution(13,17))