'''You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n. If positive, print numbers from n-1 to 0 by subtracting 1 from n.'''

{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        numbah=int(input())
        if(numbah>0):
            pos(numbah)
        elif(numbah<0):
            neg(numbah)
        else:
            print("already Zero",end="")
        print()
        testcases-=1
        
if __name__=='__main__':
    main()
}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def pos(n):
    while(n>0):
        n=n-1
        print(n,end=" ")

def neg(n): 
    while(n<=0):
        print(n,end=" ") ##Write the code
        n=n+1