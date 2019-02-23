'''Given two strings a and b. The task is to make a new string where the string with longer length should be in between and the one with shorter length should be outside on front and end. New string should be like shorter+longer+shorter.'''

{
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    # 
    testcases = int(input())
    
    while(testcases > 0):
        string = input().split()
        string1 = string[0]
        string2 = string[1]
        
        testcases -= 1
        
        print (combo_string(string1, string2))
if __name__ == '__main__':
    main()
}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
# Function to join given strings
def combo_string(a, b):
  
  # your code here
  if len(a)<len(b):
      short = a
      longer = b
  else:
      short = b
      longer = a
  
  return short+longer+short