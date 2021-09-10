def dec1(func1):
    def now_exec():
        print("execute starting")
        func1()
        print("executed")
    return now_exec()

@dec1
def who_is_me():
    print("deepu is a good boy")
    
        