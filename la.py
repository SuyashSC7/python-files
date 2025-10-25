def matrix(rowechelon):
    for i in range(len(a)):
        for k in range(0,len(a)):
            if a[i][k]==0:
                for j in range(0,len(a[0])):
                    a[i], a[-1] = a[-1], a[i]




    for k in range(1,len(a)):
        for i in range(k,len(a)):
            if a[i][k-1]!=0:
                multiple=a[i][k-1]/a[k-1][k-1]
                for j in range(0,len(a[0])):
                    a[i][j]=a[i][j]-multiple*a[k-1][j]

    for i in range(len(a[0])-1):
            if a[i][i]!=1:
                div=a[i][i]
                for j in range(0,len(a[0])):
                    a[i][j]=a[i][j]/div
    for i in range(len(a)-1,-1,-1):
        for k in range(i-1,-1,-1):
            multiple=a[k][i]/a[i][i]
            for j in range(0,len(a[0])):
                a[k][j]=a[k][j]-multiple*a[i][j]
    return a
#i wanna make the entries below pivot elements zero how to do that?????

a=[
    [10,4,-2,0,14],
    [-15,0,2,-3,0],
    [1,1,0,1,6],
    [-5, -5, -10, 8, 26]
]
x = matrix(a)

for row in x:
    print([round(y, 2) for y in row])
print()
for i in range(len(a)):
    print(f'x{i} : ',round(a[i][-1],2))
num = 12345
digits = [int(d) for d in str(num)]
print(digits)