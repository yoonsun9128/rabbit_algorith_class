# 나머지가1이되는수찾기-월간코드챌린지시즌3

def solution (n):
    result = []
    for x in range(1,n+1):
        if int(n) % int(x) == 1 :
            result.append(x)
    return result[0]