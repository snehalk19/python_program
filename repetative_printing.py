'''There may be times when you need to print the same string multiple times.
Input Format:
1
Geeks
5

Output Format:
Geeks Geeks Geeks Geeks Geeks'''

{
#Initial Template for Python 3
# Python Code to print given string
# multiple times
//Position this line where user code will be pasted.
# Driver Code
def main():
    testcases = int(input())
    
    # Loop for testcases
    while(testcases > 0):
        string = input()
        x = int(input())
        print_fun(string, x)
        testcases -= 1
if __name__ == '__main__':
    main()
    
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to print given string 'x' times
def print_fun(string, x):
    # Your code here
    print(string*x ," ")