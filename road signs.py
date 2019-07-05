'''
On her way to ChefLand, Marichka noticed 10K road signs (numbered 0 through 10K−1). For each valid i, the sign with number i had the integer i written on one side and 10K−i−1 written on the other side.

Now, Marichka is wondering — how many road signs have exactly two distinct decimal digits written on them (on both sides in total)? Since this number may be large, compute it modulo 109+7.

For example, if K=3, the two integers written on the road sign 363 are 363 and 636, and they contain two distinct digits 3 and 6, but on the road sign 362, there are integers 362 and 637, which contain four distinct digits — 2, 3, 6 and 7. On the road sign 11, there are integers 11 and 988, which contain three distinct digits — 1, 9 and 8.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains a single integer K.
Output
For each test case, print a single line containing one integer — the number of road signs with exactly two digits, modulo 109+7.

Constraints
1≤T≤105
1≤K≤109
Subtasks
Subtask #1 (20 points): 1≤T,K≤5
Subtask #2 (80 points): original constraints

Example Input
1
1
Example Output
10
'''
try:
    import time
    def fast_power(base, power):
        result = 1
        while power > 0:
            # If power is odd
            if power % 2 == 1:
                result = (result * base)%1000000007 

            # Divide the power by 2
            power = power // 2
            # Multiply base to itself
            base = (base * base) % 1000000007

        return result
    
    
    
    
    
    t=int(input())
    while(t):
        
        t=t-1
        k=int(input())
        s=time.time()
        print((10*(fast_power(2,k-1))%(10**9+7)))
        e=time.time()
        #print(e-s)
except:
    pass
