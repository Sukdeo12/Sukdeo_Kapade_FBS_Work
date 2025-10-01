while(1):
    num =int(input("ENter the number:"))

    if num >= 0:
        if num > 50:
            if num > 100:
                if num > 500:
                    if num > 5000:
                        print(f'{num} is more than 5000')
                    else:
                        print(f'{num} is between 501 - 5000')
                else:
                    print(f'{num} is between 101-500')
            else:
                print(f'{num} is between 51-100')
        else:
            print(f'{num} is between 0-50')
    else:
        print(f'{num} is Negative')
