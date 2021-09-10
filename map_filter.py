# import file1
# print(sum(45,45))


# def squre(a):
 #    return a*a
# def cube(a):
#     return a*a*a
# 
# harry = [squre ,cube]
# for i in range(5):
#     val = list(map(lambda x :x(i), harry))
 #    print(val)

 # list_1 = [2,45,65,4,65,100,48,565,56]
 # 
 # def gr_thn_5(num):
 #     return num>5
 # 
 # grt_than_5 = list(filter(gr_thn_5,list_1))
 # print(grt_than_5)
    
    #*********************************************
    
from decorters import dec1
from functools import reduce

list1 = [4,5,54,78,2]
num = reduce(lambda x,y:x*y ,list1)
print(num)