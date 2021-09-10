print("enter your number")
num1 =(input())
print("enter your number")
num2 =(input())
try:
    print("the sum of this two numbers is",
    int(num1)+int(num2))
except Exception as e:
    print(e)
print("this line is very important")