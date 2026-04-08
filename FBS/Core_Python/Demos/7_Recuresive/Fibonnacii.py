def fibb(n,a,b):
    # if n>0:
    #     c = a + b
    #     print(c)        
    #     fibb(n-1, b, c)
    a,b = 0,1
    while a <= n:
        print (a)        
        a,b = b,a+b 
              
n = 15
fibb(n, -1, 1)        