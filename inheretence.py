from classes import Emloyee


class Employee:
    raise_amt=1.04
    def __init__(self, name ,age, pay):
     self.name= name
     self.age=age 
     self.pay=pay
     self.email=name +'@gmail.com'
    def name(self):
        return '{}'.format(self.name)

    def apply_raise(self):
       self.pay=int(self.pay * self.raise_amt)

class developer(Employee):

    def __init__(self , name ,age, pay,lang):
       super().__init__(name,age,pay)
       self.lang=lang
class manager(Employee):
    def __init__(self,name,age,pay,employees=None):
        super().__init__(name,age ,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees= employees
    def append_emp(self,emp):
        if emp not in  self.employees:
            self.employees.append(emp)
            #for removing the items
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # for printing the items
    def print_item(self):
        for emp in self.employees:
            print('>>-',emp.name)
 



#writing the name of the developers
dev1=developer('airi',18,5000,'python')
dev2=developer('jhatu',48,70000,'cpp')
mang1=manager('bhavy',18,6000,[dev1])
print(mang1.email)
mang1.remove_emp(dev2)
mang1.print_item()
     
print(isinstance(mang1,Employee))
print(issubclass(Employee,developer))