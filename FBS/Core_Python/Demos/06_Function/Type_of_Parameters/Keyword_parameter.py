def emp(id, name, dept, sal, age, address):
    data = (f'ID: {id}\nName: {name}\nDept: {dept}\nSal: {sal}\nAge: {age}\nAddress: {address}')
    return data

print(emp(1, 'Sukdeo', dept='DA', sal=35000, age=27, address='Jalgaon'))