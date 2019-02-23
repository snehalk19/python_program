{
#Initial Template for Python 3
import re
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        mystr=input()
        print(validate(mystr))
        testcases-=1
        
if __name__=='__main__':
    main()
}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def validate(str):
    pat= r"[a-z]+[!@#$% ]+[0-9]"
    match=re.search(pat,str)
    if(match):
        return True
    else:
        return False
