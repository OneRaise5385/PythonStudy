def sf(m):
    if m==0:
        return 1
    else:
        return m*sf(m-1)
result=sf(1)+sf(2)+sf(3)+sf(4)+sf(5)
print(result)