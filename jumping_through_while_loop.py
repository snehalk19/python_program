'''Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).'''

{
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        x = int(input())
        
        printIncreasingPower(x);
        print ()
        
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to print x in increasing order
def printIncreasingPower(x):
    ##Your code here
    i = 1
    # Loop to jump in powers of 2
    while(pow(i,2)<=x):
        
        
        print (pow(i,2), end = " ")
        i = i+1
    