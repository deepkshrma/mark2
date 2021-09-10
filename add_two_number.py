from typing import List


n = int(input("enter your test_case"))
i=0
while(i < n ):
    

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    
    List = [a , b , c , d , e]
    List.sort()
    print(List[2])

    
    i+=1
