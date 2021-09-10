n = 9
t= 0
while t<n:
    num = int(input("enter your number:"))
    if num < 18:
        print("incress your number\n")
    elif num>18:
        print("decress your number\n")
    elif num == 18:
        print("you win!")
        print("round  for win:" ,t+1)
        break
    t += 1