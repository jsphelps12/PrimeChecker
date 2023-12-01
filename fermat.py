import random as rnd
def prime_test(N, k):
    # This is the main function connected to the Test button. You don't need to touch it.
    return run_fermat(N,k), run_miller_rabin(N,k)


def mod_exp(x, y, N):
    # You will need to implement this function and change the return value.
    if y == 0:
        return 1
    #will call itself n times if y is n bits long
    z = mod_exp(x,(y//2),N)
    if y %2 == 0:
        #multiplication is O(n^2)
        return (z**2) % N
    else:
        #this is also still multiplication of O(n^2)
        return (x*(z**2)) % N
    

def fprobability(k):
    # You will need to implement this function and change the return value.   
    return 1-(1/(2**k))


def mprobability(k):
    # You will need to implement this function and change the return value.   
    return 1-((1/4)**k)


def run_fermat(N,k):
    #these values are unique and small enough where we don't need to run the test
    if(N == 2 or N == 3):
        return 'prime'
    #do the test a chosen amount of times
    for i in range(k):
        #pick a random a
        a = (rnd.randint(2,N-1))
        #run mod_exp check to see if it is equal to 1
        if mod_exp(a,N-1, N) != 1:
            return 'composite'
    return 'prime'


def run_miller_rabin(N,k):
    #run check
    if(N == 2):
        return 'prime'
    #auto return composite if it is even
    if N % 2 == 0 and N > 2:
        return 'composite'
    #run test a chosen amount of times
    for i in range(k):
        #generate number for the test
        a = (rnd.randint(1,N-1))
        #find what the exponent will start as
        n = N-1
        #run initial test
        if mod_exp(a,n,N) != 1:
            return 'composite'
        #half the exponent
        n = n / 2
        #while the exponent is even we continue the loop
        while n % 2 == 0:
            #continue if mod_exp returns 1
            if mod_exp(a,n,N) == 1:
                n = n/2
            #if it returns -1 after only 1's then we are prime
            elif mod_exp(a,n,N) == (N-1):
                break;
            #if we get here before it's been -1 then we are composite for sure
            else:
                return 'composite'
    return 'prime'


#print(mod_exp(3,24,97))
print(run_miller_rabin(101,10))
