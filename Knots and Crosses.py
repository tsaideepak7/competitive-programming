'''
Knots and Crosses
Given a matrix, m rows, n columns and an integer k, filled with x and o, find the count of streaks of x and o. A streak is a group of adjacent k characters where adjacency is horizontal, vertical and diagonal.

Input Format
The first line contains and integer t denoting the number of test cases. The second line consists of three space separated integers m, n and k. The next m rows each contain n space separated characters.

Output Format
For each test case print the count of streaks of x and o space separated.

Sample Input
7
3 3 3
x x x
x o x
x x x
1 1 2
o
2 2 2
x o
o x
4 3 3
x x o
o x o
x o x
o x x
1 5 2
x x x x x
4 4 3
x x x x
x x o o
x x o o
x o o o
4 4 2
x o o x
o x x o
o x x o
x o o x


Sample Output
4 0
0 0
1 1
1 1
4 0
6 4
10 8


Constraints
1 <= t <= 1000 
1 <= m,n <= 100 
2 <= k <= 10

'''




def ccc(i,j,c):
    global x,o
    nh=nv=nc=nco=k
    if(c=='x'):
        for z in range(k):
            if( i+z<m and l[i+z][j]=='x'  ):
                nv-=1
            else:
                break
            if(nv==0):
                                
                x+=1
        for z in range(k):
            if(j+z<n and l[i][j+z]=='x'):
                nh-=1
            else:
                break
            if(nh==0):
                
                
                x+=1
        for z in range(k):
            if( j+z<n and i+z<m and l[i+z][j+z]=='x'):
                nc-=1
            else:
                break
            if(nc==0):
                
                x+=1
        for z in range(k):
            
            if( j+z<n and i-z>=0 and l[i-z][j+z]=='x' ):
                nco-=1
            else:
                break
            if(nco==0):
                
                x+=1
    if(c=='o'):
        for z in range(k):
            if( i+z<m and l[i+z][j]=='o'  ):
                nv-=1
            else:
                break
            if(nv==0):
                               
                o+=1
        for z in range(k):
            if(j+z<n and l[i][j+z]=='o'):
                nh-=1
            else:
                break
            if(nh==0):
                
                o+=1
        for z in range(k):
            if( j+z<n and i+z<m and l[i+z][j+z]=='o'):
                nc-=1
            else:
                break
            if(nc==0):
                
                o+=1
        for z in range(k):
            
            if( j+z<n and i-z>=0 and l[i-z][j+z]=='o' ):
                nco-=1
            else:
                break
            if(nco==0):
                
                o+=1
    


t=int(input())
while(t):
    x=0
    o=0
    t-=1
    m,n,k=map(int,input().split())
    l=[]
    
    for i in range(m):
        p=list(input().split())
        l.append(p)
    
    
    for i in range(m):
        for j in range(n):
            ccc(i,j,l[i][j])
    print(x,o)
    
            
    
