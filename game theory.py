'''2 players are playing a game,
given number of piles of stones, each player has to pick either [1,2,3] stones
from a pile alternatively.
A player looses if he cannot make his move.
Both the players play optimally
'''



def calculate_mex(Set): 
	mex = 0
	
	while mex in Set: 
		mex += 1

	return mex 



def calculate_grundy(n):
    if 0 <= n <= 3:    #end conditions depends on the question
        return n
    
    Set=set()

    for i in taken_allowed:
        #print(n-i)
	if(n-i)<=0:
		Set.add(calculate_grundy(n-i))   #recursion depends on the question
    #print(Set)
        
    return(calculate_mex(Set))
    

                

      


given_stone_piles=[10,64]
taken_allowed=[1,2,3]

t=[]

for i in given_stone_piles:
    t.append(calculate_grundy(i))
xor=0
for i in t:
    xor=xor^i    #simple nim game

if(xor==0):
    print('player 2 wins')
else:
    print('player 1 wins') 
                    

