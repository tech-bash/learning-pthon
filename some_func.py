

class Employee:
    raise_amt=1.04
    def __init__(self, name ,age, pay):
     self.name= name
     self.age=age 
     self.pay=pay
     self.email=name +'@gmail.com'
    def __repr__(self) :
        return "Employee {} {}".format(self.name,self.age)
    def __str__(self):
        return '{}-{}'.format(self.name,self.age)
    def __add__(self,other):
        return self.pay + other.pay
        
emp1=('airi',18,5000)
emp2=('keshav',15,6000)
print(emp1 + emp2)     