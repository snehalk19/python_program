{
#Initial Template for Python 3
//Position this line where user code will be pasted.    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        base=int(input())
        exp=int(input())
        print(power(base,exp)) ##calling the anonymous function
        testcases-=1
        
if __name__=='__main__':
    main()
}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
    
power = lambda base, exp: base**exp
