class A:
    def __init__(self,s1,n1):
        self.s1=s1
        self.n1=n1
    def disp(self):  # 定义基类方法
        print(self.s1,self.n1)
a=A('张','义举')
a.disp()
class B(A):
    def __init__(self,s1,n1,s2,n2):
        self.s2=s2
        self.n2=n2
    def disp(self):
        print(self.s2,self.n2)
b=B('张','义举','张','三')
b.disp()