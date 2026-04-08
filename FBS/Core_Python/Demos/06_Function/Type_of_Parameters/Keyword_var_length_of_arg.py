def emp(**data):
    print(type(data))   #class is dictionary
    # for i in data:
    #     print(i)
    
    for i,j in data.items():
        #print(i)    #get information in touple format
        print(f'{i} : {j}')
        
    
print(emp(id=10, name = 'Sukdeo', sal = 35000))