{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        c=int(input())
        bitwise(a,b,c)
        testcases-=1
        
if __name__=='__main__':
    main()
}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def bitwise(a,b, c):
    d=  a ^ a
    print(d)
    e = c ^ b
    print(e)
    f = a & b
    print(f)
    g = c | (a ^ a)
    print(g)
    e = ~e
    print(e)