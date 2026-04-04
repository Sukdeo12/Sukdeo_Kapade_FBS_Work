#List defines in [] braket
li1 = [1,2,3,4]
li2 = [1, 0.33, 'abc', '&&']
# print(li1)
# print(type(li1))
# print(li2)
# print(type(li2))
print(id(li1))
print(li1[0])
print(type(li1[0]))
print(id(li1[0]))
li1[0] = 10
print(li1[0])
print(type(li1[0]))
print(id(li1[0]))
li1[0] = 5.56778
print(li1[0])
print(type(li1[0]))
print(id(li1[0]))
li1[0] = 'a'
print(li1[0])
print(type(li1[0]))
print(id(li1[0]))
print(id(li1))