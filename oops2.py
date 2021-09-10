class Employee:
    pass
    
    def printdetails(self):
        return f"name is {self.name} ,salary is {self.salary} , role is {self.role}"
        


deepu = Employee()
radhey = Employee()

deepu.name = "deepak"
deepu.salary = 120
deepu.role = "programmer"
radhey.name= "radheyshyam sharma"
radhey.salary = 120000
radhey.role = "deepu's father"

print(radhey.printdetails())