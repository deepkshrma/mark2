class Employee:
    def __init__(self, aname,asalary,arole):
        self.name =aname
        self.salary=asalary
        self.role=arole
        self.__doc__=self
        
        
        
        



deepu = Employee("deepak" , 120 , "programmer")
# radhey = Employee()

# vdeepu.name = "deepak"
# vdeepu.salary = 120
# vdeepu.role = "programmer"
# vradhey.name= "radheyshyam sharma"
# vradhey.salary = 120000
# vradhey.role = "deepu's father"
print(deepu.salary)