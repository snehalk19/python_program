'''You are given a string str, you need to print True if cat and hat appear same number of times in str, otherwise print False.'''

{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=input()
        print(cat_hat(mystr))
        testcases-=1
        
if __name__=='__main__':
    main()
}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def cat_hat(str):
  ##your code here##
  ##You need to write complete code this time 
  hat = str.count("hat")
  cat = str.count("cat")
  if hat==cat:
      return True
  else:
      return False
