def BinarySearch(li, searchEle):
    beg = 0
    end = len(li)-1
    while(beg <= end ):
        mid = (beg + end)//2
        if searchEle == li[mid]:
            return mid
        elif (searchEle > li[mid]):
            beg = mid + 1
        elif (searchEle < li[mid]):
            end = mid -1
    else:
        return None
    
li = [10, 20, 30, 40, 50, 60,70]
el = int(input('Enter the element to search : '))
res = BinarySearch(li, el)

if res != None:
    print(f'{el} is present in list in give index {res}')
else:
    print(f'{el} not present in list')