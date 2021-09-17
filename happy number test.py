#isHappyNumber() will determine whether a number is happy or not    
def isHappyNumber(num):    
    rem = sum = 0;    
        
    #Calculates the sum of squares of digits    
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem*rem);    
        num = num//10;    
    return sum;    
  
#two_digits = [ i for i in range(10,100)]    
  
counterUnhappy = 0
counterHappy = 0
for i in range(10,100):
    result = i
    while(result != 1 and result != 4):    
        result = isHappyNumber(result);    
         
    #Happy number always ends with 1    
    if(result == 1):    
        print(str(i) + " is a happy number");
        counterHappy +=1
    #Unhappy number ends in a cycle of repeating numbers which contain 4    
    elif(result == 4):    
        print(str(i) + " is not a happy number");
        counterUnhappy +=1

print(counterUnhappy)
print(counterHappy)