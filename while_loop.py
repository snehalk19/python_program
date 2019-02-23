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
        
        printInDecreasing(x);
        
        print ()
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to print x in decreasing order
def printInDecreasing(x):
    # Complete the code below
    while(x >= 0):
        
        # your statement below to print the number
        # in decreasing order
        # Note: use end=" " parameter with print to seperate numbers by space.
        ##Output for testcases will automatically separated by a new line by the print() in driver code
        
        print(x , end = " ")
        
        x -= 1