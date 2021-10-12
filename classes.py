class Emloyee():
  count=0
  # this is defining the class variable 
  #raise_amount=int(input('enter the amount :'))
    # its the basic code for storing 
  def __init__(self,name,age,pay):
    #define each of the following and then add info.
     self.name = name 
     self.age=age
     self.pay=pay
     self.email=name + '@gmail.com'
     
     Emloyee.count+=1
  def apply_raise(self):
       self.pay=int(self.pay * Emloyee.raise_amount)  
     # creating an alternative consturctor
  @classmethod
  def set_raise_amount(cls,amount):
    cls.raise_amount=amount
  @classmethod
  def from_string(cls,emp_str):
    name,age,pay=emp_str.split('-')
    return cls(name,age,pay)
  @staticmethod
  def workday(day):
    if day.weekday()==5 or day.weekday == 6 :
      return True
    else :
      return False
         
import datetime
my_date = datetime.date(2016, 7 , 16)

#emp1='airi-18-5000'
#emp2='keshav-14-8000'
#emp1.set_raise_amount(5)
#print(emp2.raise_amount)
     # here u can call hte class method 
#new_emp=Emloyee.from_string(emp1)
#print(new_emp.pay)
 # this format tag is to be learned evertime u need to print {} and this {}
# print ("The amount to {} is  ${}".format(emp1.name ,emp1.pay))
#print(emp1.raise_amount)
#print(new_emp.__dict__)
print(Emloyee.workday(my_date))
