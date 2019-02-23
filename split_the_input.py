'''In this question, you will take input a single line string comprised of string, int, and float. You'll split the string and assign string to s, int to i, and float to f. Print a final string comprised of s and (i+f)'''

{

def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        inPutS() #the function that gets things done
        testcases-=1
        
if __name__=='__main__':
    main()
}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def inPutS():
    a=input() ## input in a single line()
    s,i,f = a.split() 
    print(s+" "+str(int(i)+float(f))) ##type cast i to int, f to float. Add i with f. Typecast the result to string