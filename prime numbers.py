#sieve of erathosthenes , prime numbers

def generateprime(n):
    global prime
    prime=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if prime[p]==True:
            for j in range(p*2,n+1,p):
                print(j)
                prime[j]=False
        p+=1
    primelist=[]
    for i in range(2,n):
        if prime[i]:
            primelist.append(i)
        
    return(primelist)
        
            

k=generateprime(121)


