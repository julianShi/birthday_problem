# This solves the average number of birthdays in a group
# Julian Shi, 2020-02-11

def binomial(n,k,cache):
    # Calculate the binomial coefficient
    if(k<0 or k>n):
        return 0
    if(k==0 or n==k):
        return 1
    if(k==1 or n==k+1):
        return n
    if(cache[n][k]!=None):
        return cache[n][k]
    cache[n][k]= binomial(n-1,k,cache)+binomial(n-1,k-1,cache)
    return cache[n][k]

def divide(numerator,denominator):
    # Return approximate solution
    lenN=len(str(numerator))
    lenD=len(str(denominator))
    proximateN=numerator/(10**(lenN-10))
    proximateD=denominator/(10**(lenD-10))
    return float(proximateN)/float(proximateD)*(10**(lenN-lenD))

def average_birthdays(DAYS,PEOPLE):
    # DAYS denotes the number of days in a year
    # PEOPLE denotes the number of members in the group
    cache = [ [ None for _ in range(DAYS+1)] for _ in range(DAYS+1)] 
    permutations = [ [ 0 for _ in range(DAYS+1)] for _ in range(DAYS+1)] 
    # permutations[n][k] denotes the permutation when there are exactly k days in n days that are birthdays

    permutations[1][1]=1
    for n in range(1,DAYS+1):
        permutations[n][n]=n**PEOPLE
        for k in range(1,n):
            permutations[n][k]=permutations[k][k]*binomial(n,k,cache)
            permutations[n][n]-=permutations[n][k]

    denominator=DAYS**PEOPLE
    probabilities = [ divide(perm,denominator) for perm in permutations[DAYS]]
    # Calculate the average days by weight
    average_days=0
    for k in range(1,DAYS+1):
        average_days+=k*probabilities[k]
    return average_days

PEOPLE=365 
DAYS=365 
print(average_birthdays(DAYS,PEOPLE))
