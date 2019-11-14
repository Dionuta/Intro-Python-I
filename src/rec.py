def re(n):
    if n < 2:
       return 1
    return n * re(n -1) 

print(re(3))
