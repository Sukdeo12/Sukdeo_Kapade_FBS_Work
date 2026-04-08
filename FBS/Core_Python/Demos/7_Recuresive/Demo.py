def series(n):
    if(n>=1):
        print('Number = ', n)
        series(n-1)
    
    print('Funtion end ', n)
    return    
n=5
series(n)