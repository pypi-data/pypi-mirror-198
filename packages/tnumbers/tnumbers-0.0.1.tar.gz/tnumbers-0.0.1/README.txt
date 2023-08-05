This module return all the even umbers between the given two numbers(Both inclusive).

How to make most use of the module?

simply run the following command "pip install tnumbers" in the command prompt

then open up your project and import tevevn package

now you are ready to use the function evens_between

-------------USAGE----------------

import tnumbers

//Prints the values between two integers a and b where a<b
a,b=2,20

evens=tnumbers.evens_between(a,b)
print(evens)//output is [2,4,6,8,10,12,14,16,18,20]

//similarly for odd and prime numbers
print(tnumbers.odds_between(a,b)) //output is [3, 5, 7, 9, 11, 13, 15, 17, 19]
print(tnumbers.primes_between(a,b)) //output is [2,3,5,7,11,13,17,19]