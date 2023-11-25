import random
num_list=[]
for i in range(1000):
	n=random.randint(20,100)
	num_list.append(n)
print(num_list)
num_set=set(num_list)
print(num_set)
for j in num_set:
	k=num_list.count(j)
	print(j,"出现了",k,"次")
