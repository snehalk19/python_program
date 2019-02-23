'''The function should take a number n as parameter and return True if n is prime. Return False in other cases.'''

{
#Initial Template for Python 3
//Position this line where user code will be pasted.
import math ##You will need this for prime checking
    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        number=int(input())
        print(isPrime(number)) ##This isPrime is function that you need to create
        testcases-=1
        
if __name__=='__main__':
    main()
}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
##Write the function completely
def isPrime(n):
    if n == 1: 
        return False
          
    for x in range(2, (int)(math.sqrt(n))): 
        if n % x == 0: 
            return False 
    return True