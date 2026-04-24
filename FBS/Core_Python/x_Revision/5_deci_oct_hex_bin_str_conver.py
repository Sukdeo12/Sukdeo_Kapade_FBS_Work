str = '100'
dec = int(str) #Convert string to int
# print(str,dec)
# print(type(str), type(dec))

# bins = bin(dec) #Convert int to bin
# print(bins,dec) #0b1010 10
# print('Bin - ',type(bins), type(dec)) #Bin -  <class 'str'> <class 'int'>

# octs = oct(dec)
# print(octs, dec)    #0o144 100
# print(type(octs), type(dec))    #<class 'str'> <class 'int'>

# h = format(dec, 'x')  # 'x' => hex conv, 
# print(h, dec)
# print(type(h), type(dec))
# h = int(h)
# d = format(h, 'd')
# print(d, h)
# print(type(d), type(h))


num = 255
print(type(num))
print("Decimal :", type(format(num, 'd')), type(int(num)))
print("Hex     :", format(num, 'x'), hex(num))
print("Octal   :", format(num, 'o'), oct(num))
print("Binary  :", format(num, 'b'), bin(num))

'''
Decimal → Hexformat(n, 'x')
Decimal → Octformat(n, 'o')
Decimal → Binformat(n, 'b')
Hex → Decimalint(hex_str, 16)
Oct → Decimalint(oct_str, 8)
Bin → Decimalint(bin_str, 2)
String → Hexs.encode().hex()
String → Bytess.encode()
'''