def threesumclosest(nums:list[int], target:int):
    from itertools import combinations
    closest=target-nums[0]
    comb=list(combinations(nums,3))
    for c in comb:
        s=sum(c)
        
        if abs(s-target)<closest:
            closest=s
            print(s)
        else:
            continue

    print(c)
    return closest





nuns= [-1,2,1,-4]
targe=1
print(threesumclosest(nuns,targe))