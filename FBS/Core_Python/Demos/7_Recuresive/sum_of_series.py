#Sum of first number

def sum_of_series(n):
    res = n
    if(n==1):   #Base condition --- stoping conditiom
        return 1
    else:
        print(n)
        return (n + sum_of_series(n-1))
    print(n)

n=5
print(sum_of_series(n))
    