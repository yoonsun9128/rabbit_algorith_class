
def solution(a):
    number_dict = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    for i in number_dict:
        a = a.replace(i,number_dict[i])
    return int(a)

print(solution("123"))

print(type(123))
print(type("123"))