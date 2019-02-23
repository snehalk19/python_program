{
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    # testcase input
    testcases = int(input())
    
    # looping through testcases
    while(testcases > 0):
        string = input()
        
        testcases -= 1
        
        gfg(string)
if __name__ == '__main__':
    main()
}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to check if string 
# starts and ends with 'gfg'
def gfg(a):
    b = a.lower()
    if(b.startswith('gfg') and b.endswith('gfg')):  # use b.startswith() and b.endswith()
        print ("Yes")
    else:
        print ("No")