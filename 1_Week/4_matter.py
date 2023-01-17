n = 12345
def solution(n):
    n = list(map(int, str(n)))
    n.reverse()
    return n

def solution2(n):
    n = list(map(int, reversed(str(n))))
    return n