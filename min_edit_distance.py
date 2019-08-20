''' The edit distance is the number of operations (insertions, deletions or substitutions) needed to transform one string in another. 

find the edit distance to convert s1 to s1 '''

s1 = 'azced'
s2 = 'abcdef'

n = len(s1)
m = len(s2)

dp=[[0 for j in range(n+1)] for i in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if(i == 0):
            dp[i][j]=j
        elif(j == 0):
            dp[i][j]=i
        else:
            try:
                if(s1[i-1] == s2[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] , dp[i-1][j-1] , dp[i][j-1]) + 1

            except:
                dp[i][j] = min(dp[i-1][j] , dp[i-1][j-1] , dp[i][j-1]) + 1
for row in dp:
    print(row)

print(dp[-1][-1])
