def countValidSelections(nums: list[int]):
    wherezerois=[]
    count=0
    if len(nums)==1:
        return 0
    else:
        for currs in range(len(nums)):
            if nums[currs]==0:
                wherezerois.append(currs)
            else:
                continue
        for i in wherezerois:
            
            lhs_sum=sum(nums[:i])
            rhs_sum=sum(nums[i+1:])
            if lhs_sum==rhs_sum:
                count+=2
            elif abs(lhs_sum-rhs_sum)==1:
                count+=1
            else:
                continue
        return count

nums = [16,13,10,0,0,0,10,6,7,8,7]
print(countValidSelections(nums))

