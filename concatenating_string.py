'''
You have two strings and your task is to print the string after concatenating them.

Hint: Use "+" to concatenate strings.

Input:
Geeks
Code

Output:
Geeks Code'''

{
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Python Code to concatenate given strings
def main():
    testcases = int(input())
    
    while(testcases > 0):
        string1 = input()
        string2 = input()
        print_fun(string1, string2)
        
        testcases -= 1
if __name__ == '__main__':
    main()
    

}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to concatenate given two strings and print
def print_fun(string1, string2):
    print (string1 + string2)
