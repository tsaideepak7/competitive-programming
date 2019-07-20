'''
Given an array of non-negative integers,
 you are initially positioned at the first index of the array.

Each element in the array represents your
 maximum jump length at that position.

Your goal is to reach the last index
 in the minimum number of jumps.
'''

l=[2,3,1,1,2,4,2,0,1,1]
jumps=0
end=0
farthest=0
jumps_chosen=[]
for i in range(len(l)-1):
    if(i+l[i]>farthest):
        jumps_chosen.append(i)
    farthest=max(farthest,i+l[i])
    
    
    if(i==end):
        #print(i,end,farthest)
        
        jumps+=1
        end=farthest
print(jumps)

print(jumps_chosen)