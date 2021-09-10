# def minus(a ,b):
#     return a-b
# a= int(input())
# b= int(input())   
# print(minus(200 ,100))

 # lambda function is
 # minus = lambda a,b : a-b 
# print(minus(9 , 4))
def  first(a):
    return a[1]
    
a = [ [102,4] , [60,2],[54,8]]
a.sort(key=first)
print(a)