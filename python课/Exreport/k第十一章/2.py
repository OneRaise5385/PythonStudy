class Undergraduate:
    def __init__(self,name,sex,date1,school1):
        self.name=name
        self.sex=sex
        self.date1=date1
        self.school1=school1
        # print(self.name,self.sex)
        # print(self.date1,self.school1)
class Master(Undergraduate):
    def __init__(self,name,sex,date1,school1,date2,school2):
        self.date2=date2
        self.school2=school2
        # print(self.date2,self.school2)
class Doctor(Master):
    def __init__(self,name,sex,date1,school1,date2,school2,date3,school3):
        self.date3=date3
        self.school3=school3
        # print(self.date3,self.school3)

# a=Undergraduate('Jack','male','20211017','zzu')
# b=Master('Jack','male','20211017','zzu','none','none')
# c=Doctor('Jack','male','20211017','zzu','none','none','none','none')