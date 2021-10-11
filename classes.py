class Emloyee():
    # its the basic code for storing 
  def __init__(self,name,age,pay):
    #define each of the following and then add info.
     self.name = name 
     self.age=age
     self.pay=pay
     self.email=name + '@gmail.com'
     # the the info. u need
emp1=Emloyee('airi',19,500000)
emp2=Emloyee('yash',20,70000)
 # this format tag is to be learned evertime u need to print {} and this {}
print ("This is the name {} {}".format(emp1.name ,emp2.age))
