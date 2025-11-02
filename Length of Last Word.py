# def lenghtoflastword(s):
#     x=s.split()
#     lastword=len(x[-1])
#     return lastword


# def plusone(digits:list[int]):
#     numbers_as_strings = int(''.join(str(num) for num in digits))
#     numbers_as_strings+=1    
#     digits_list_comprehension = [int(digit) for digit in str(numbers_as_strings)]
#     print(digits_list_comprehension)

# def addbinary(a:str,b:str):
    
#     x=int(str(a),2)+int(str(b),2)
#     y=bin(x)[2:]
#     print(y)
# addbinary(11,1)

# def getsneakynumbs(nums:list[int]):
#     nums.sort()
#     ans=[]
#     for x in range(len(nums)-1):
#         if nums[x]==nums[x+1]:
#             ans.append(nums[x])
#         else:
#             continue
#     return ans
# print(getsneakynumbs([0,1,1,0]))

def removeZeros(n: int) -> int:
    x=str(n)

    digit_list = list(map(int, x))

    y=[]
    for i in digit_list:
        if i!=0:
            y.append(int(i))
        else:
            pass
    return y.join('')
print(removeZeros(102030))