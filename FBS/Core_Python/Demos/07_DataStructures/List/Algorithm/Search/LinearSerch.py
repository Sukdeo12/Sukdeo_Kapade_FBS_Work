def linearSearch(li, el):
    for i in range(0, len(li)):
        if el == li[i]:
            return i
    else:
        return None

li = [10,20,33,7,29,3]
el = int(input('Enter the search number - '))
result = linearSearch(li, el)
if result:
    print(f'the search element {el} is found in index is : {result} and list no : is {li[result]} ')
else:
    print(f'Serch Element {el} not found in list') 