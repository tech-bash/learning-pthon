

class Employee:
    raise_amt=1.04
    def __init__(self, name ,age, pay):
     self.name= name
     self.age=age 
     self.pay=pay
     self.email=name +'@gmail.com'
    def email_(self):
        return '{}@gmail.com'.format(self.name)
  
emp1=Employee('airi',18,5000)
emp2=Employee('keshav',15,6000)
emp2.name = 'raghav'
print(emp1.email_())     