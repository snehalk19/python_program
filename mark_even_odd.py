'''Given a positive integer x. The task is to check if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number)'''

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
        
        if(checkOddEven(x)):
            print ("Even")
        else:
            print ("Odd")
        
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def checkOddEven(x):
    if(x % 2 is 0):
      # Complete the statement below
      return True
    else:
        # Complete the statement below
        return False