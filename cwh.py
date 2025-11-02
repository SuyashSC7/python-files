nums=[-1,0,1,2,-1,-4]
if nums==[]:
    print([])
finalans=[]
numsin=[]
for i in range(len(nums)-2):
    for k in range(i+1,len(nums)-1):
        comb=nums[i]+nums[k]    
        for m in range(k+1,len(nums)):
            if nums[m]==(-comb) and (nums[i] not in numsin or nums[k] not in numsin or nums[m] not in numsin):
                ans=[nums[i],nums[k],nums[m]]
                numsin.extend(ans)
                finalans.append(ans)
            else:
                continue
print(finalans)