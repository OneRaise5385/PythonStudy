for i in range(1,1001):
    k=0
    for j in range(1,i-1):
        if i%j==0:
            k=k+j
    if k==i:
        print(i)