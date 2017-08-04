#-*-coding:utf8;-*-
#qpy:3
#qpy:console

# This script finds longest common end(front and back) in a string
# "abcxyzabc" returns "abc"
def sameEnds(str):
    leng=len(str)
    if(leng==1):
        return "we need a longer input"
    
    #Finding left and right to extract string[from 0 to left] and string[from right upto end] for comparison
    half = int(leng/2)
    left=half
    right=0
    if(leng%2 == 0):
        right=half
    else:
        right=half+1
    
    try:
        while( left>0 and 
        	str[:left] != str[right:] ):
            left=left-1
            right=right+1
        
        if(left>0):#A match is found
            return 'result:{}'.format(str[:left])
        else:#No match. left will be 0
            return 'no same ends found'  
    except :
        return '\nexception'