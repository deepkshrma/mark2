# Function to get sum of digits
 #  def getSum(n):
 #  	
 #  	sum = 0
 #  	for digit in str(n):
 #  	     sum += int(digit)	
 #  	return sum
 #  	
 #  n = int(input("enter your number:"))
 #  print(getSum(n))



def getsum(t):
    sum = 0
    for digit in str(t):
        sum += int(digit)
    return sum



t = int(input())
print(getsum(t))