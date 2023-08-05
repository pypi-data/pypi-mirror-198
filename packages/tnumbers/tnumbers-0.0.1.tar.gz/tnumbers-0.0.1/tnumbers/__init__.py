def evens_between(start,end):
    evens=[]
    if(start<end):
        for i in range(start,end+1):
            if(i%2==0):
                evens.append(i)
    return evens


def odds_between(start,end):
    odds=[]
    if(start<end):
        for i in range(start,end+1):
            if(i%2!=0):
                odds.append(i)
    return odds

def primes_between(start,end):
    primes=[]
    if(start<end and start>0 and end>0):
        for num in range(start, end + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    primes.append(num)
    return primes                