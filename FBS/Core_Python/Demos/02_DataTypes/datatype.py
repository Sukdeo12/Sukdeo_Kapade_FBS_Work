# ###Numerical
 
# # #1.Int
# # x = 0.1
# # print(type(x), " : Data : ", x)
 
# # #2.int
# # y = 3.14
# # print(type(y), " : Data : " , y)
 
# # #3.string
# # z = 'sukdeo'
# # print(type(z), " : Data : ", z)
 
# z_1 = "sukdeo 1's"              #apenstop s mostly we are used
# print(type(z_1), " : Data : ", z_1)
 
# # #multilne store
# z_2 = '''This is my 1st line
# This is my 2st line
# This is my 3st line'''
 
# z_2 = """This is my 1st line
# This is my 2st line's
# This is my 3st line's"""
 
# print(type(z_2), " : Data : ", z_2)
 
# #4. complex
# a = 0.1 + 5j         #Real + imaginary
# print(type(a), " : Data : ", a)
 
# #Sequntials datatype:
# #1-List
# l = [1, 2, "abc", 3.14]
# print(type(l), " : Data : ", l)
 
# #2-Tuple
# t = (1, 2, "abc", 3.14)
# print(type(t), " : Data : ", t)
 
# # #3-range
# r = range(1, 11)
# print(type(r), " : Data : ", r)
 
# #4-Set type
# s = {1, 2, 'abc', 3.14}
# #s = frozenset({1, 2, "abc", 3.14})
# print(s)
# print(type(s), " : Data : ",s)
 
# ###Mapping
 
# #1-Dictionaries -> dict
# d = {'Name':'Sukdeo Kapade', 'dept':'KPIT'}
# print(type(d), " : Data : ",d)
 
# #Boolean
# #1-True
# b = True
# print(type(b), " : Data : ",b)
 
# ###Nonetype
# n = None
# print(type(n), " : Data : ", n)
 
#Binary datatype
b = b'Sukdeo'
 
print(type(b), " : Data : ", b)#, "In Bin--->", b[1:4])
 
mv = memoryview(b)
print(type(mv), " : Data : ", mv)
 
# # Print the number of bytes in the memory view
# print(mv.nbytes)  # Output: 5
 
# # Print the format of the data in the memory view
# print(mv.format)  # Output: 'B'
 
# # Print the data in the memory view as a list
# print(list(mv))  # Output: [72, 101, 108, 108, 111]
 
# # Convert the memory view to a bytes object
# bytes_obj2 = mv.tobytes()
 
# # Print the bytes object
# print(bytes_obj2)  # Output: b'Hello'
 
##The memoryview object has several attributes and methods that allow you to access and manipulate the underlying data:
# obj: The object that the memory view is referencing.
# nbytes: The number of bytes in the memory view.
# readonly: A boolean indicating whether the memory view is read-only.
# format: A string indicating the format of the data in the memory view.
# itemsize: The size of each item in the memory view.
# shape: A tuple indicating the shape of the data in the memory view.
# strides: A tuple indicating the strides of the data in the memory view.
# suboffsets: A tuple indicating the suboffsets of the data in the memory view.
# tobytes(): Returns a bytes object containing the data in the memory view.
# tolist(): Returns a list containing the data in the memory view.
# release(): Releases the memory view, allowing the underlying object to be garbage
print(mv.suboffsets)