#완주하지 못한 선수
# 참가자에서 완주자의 면단을 우선 뺀다
# 동일 이름일 경우->첫번째는 지우나 두번째는 남겨두는 쪽으로 접근

def solution(participant, completion):
    participant_count = {}
    total = list(set(participant)-set(completion))

    for a in participant:
        try:
            participant_count[a] +=1
        except:
            participant_count[a] =1
    for k,v in participant_count.items():
        if v >= 2:
            total.append(k)
    return str(total[0])



print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))