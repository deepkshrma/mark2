'''n = 3
for i in range(3):
   # print("*" * (i+1))
   # print(" " * (n-i-1), end="")
    #print("*" * (2*i+1))
    print(" " * (n-i-1))
'''
num = int(input())
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
print(f"The factorial of {num} is {factorial}")

     
    