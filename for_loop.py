{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        numbah=int(input())
        multiplicationTable(numbah)
        print()
        testcases-=1
        
if __name__=='__main__':
    main()
}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def multiplicationTable(N):## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11,1): ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i*N, end=" ") ## Separating by spaces using end =" "
        