x = 89
def deepak1():
    global x
    x = 20
    def deepak2():
        
        y = 88
        deepak2()
    print("after calling deepak2" ,x)
deepak1()
print(x)

        
    