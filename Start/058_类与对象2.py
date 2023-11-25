class R:
    name='Jack'
    x=1
    y=2
    def Disp(self):
        print(self.name)
d=R()
# print(d.name)
d.Disp()

print('------------------------')
class Stu:
    name='张'
    mark=99
s=Stu()
print(s.name)
print(s.mark)

print('-------------------------------')
class Student:
    def __init__(self,s):
        self.name=s
    def F1(self):
        self.h=20
d=Student('z义举')
d.F1()
print(d.name,d.h)