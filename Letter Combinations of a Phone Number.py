def lettercombinations(digits:str):
    from itertools import product
    dit={
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }
    ansset=[]
    digits=str(digits)
    ans=[]
    n=len(digits)
    for i in digits:
        templis=[]
        for j in dit[i]:
            templis.append(j)
        ans.append(templis)
    print(ans)
    maximumlen=0
    for x in ans:
        maximumlen=max(maximumlen,len(x))
    
    for i in range(maximumlen):
        pass
    while i>=0:
        
    # wannans1=[]
    # for i in ans:
    #     wannans=[]
    #     for k in i:
    #         wannans.append([k])
    #     wannans1.append(wannans)

    # for i in
    # print(wannans1)





lettercombinations(237)