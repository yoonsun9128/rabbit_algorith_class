# 없는 숫자 더하기

def solution(numbers):
    total_list = [0,1,2,3,4,5,6,7,8,9]
    total_set = set(total_list)-set(numbers)
    answer = 0
    for a in total_set:
        answer+= a
    return answer

print(solution([1,2,3,4,6,7,8,0]))