'''
find the largest square sub array having all ones

input:
4,5
0, 1, 1, 0, 1
1, 1, 1, 0, 0
1, 1, 1, 1, 0
1, 1, 1, 0, 1

output:
0, 1, 1, 0, 1
1, 1, 2, 0, 0
1, 2, 2, 1, 0
1, 2, 3, 0, 1

3
(left bottom has a 3x3 matrix with all ones)


'''



n=int(input()) #rows
m=int(input()) #columns
matrix=[]

for i in range(n):
    
    l=list(map(int,input().split()))
    matrix.append(l)


print(matrix)    

result=[[0 for i in range(m)] for j in range(n)]

maximum=0
for i in range(n):
    result[i][0]=matrix[i][0]
    if(result[i][0]==1):
        maximum=1

result[0]=matrix[0]
if(1 in result[0]):
    maximum=1

#print(result)

for i in range(1,n):
    for j in range(1,m):
        
        if(matrix[i][j]==0):
            #result[i][j]=max(result[i][j-1],result[i-1][j-1],result[i-1][j])
            continue
        t=min(result[i][j-1],result[i-1][j-1],result[i-1][j])
        result[i][j]=t+1
        if(result[i][j]>maximum):
            maximum=result[i][j]


print(result)
print(maximum)


