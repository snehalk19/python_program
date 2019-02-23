{
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver code
def main():
    testcase = int(input())
    
    while(testcase > 0):
        input1 = input().split()
        x = int(input1[0])
        y = int(input1[1])
        do_operation(x, y)
        testcase -= 1
        
if __name__ == '__main__':
    main()
}



''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to perform increment and decrement
def do_operation(x, y):
    # Your code here
    
    print (x-1)
    print (y+1)