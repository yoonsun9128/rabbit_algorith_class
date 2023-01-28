b = format(9, "b").zfill(5)
c = format(30, "b")
print(b)
# print(bin(9)) #0b1001
# print(bin(9)[2:].zfill(5)) #1001
# print(b) #1001
# print(c) #11110

# n	5
# arr1	[9, 20, 28, 18, 11]
# arr2	[30, 1, 21, 17, 28]

def solution(n, arr1, arr2):
    for a,b in arr1,arr2:
        print(bin(a)[2:].zfill(n))
        print(bin(b)[2:].zfill(n))
    # return answer
    #ValueError: too many values to unpack (expected 2)

def solution2(n, arr1, arr2):
    result = [''] * n #변의 길이
    for i in range(len(arr1)):
        bin1 = bin(arr1[i])[2:].zfill(n)
        bin2 = bin(arr2[i])[2:].zfill(n)
        print(bin1)
        print(bin2)
        for a in range(n):
            print("ddd",bin1[a])
            print("ccc",bin2[a])
            if bin1[a] == '0' and bin2[a] =='0':
                result[i] += ' '
            else:
                result[i] += '#'
    return result

# print(solution2(5,[9, 20, 28, 18, 11] , [30, 1, 21, 17, 28]))
print(solution2(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]  ))

['###  #', '######', '## ###', '#  ## ', '# ####', '### # ']
['######', '###  #', '##  ##', ' #### ', ' #####', '### # ']