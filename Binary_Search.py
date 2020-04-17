def binary_search(list, l, h, x):
    if h>=l:
        mid = l + (h-l) // 2
        if list[mid] == x:
            return mid
        elif list[mid] > x:
            return binary_search(list, l, mid-1, x)
        else:
            return binary_search(list, mid + 1, h, x)
    else:
        return -1


run = True
while run:
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = int(input("What number are you looking for in the list: "))
    result = binary_search(list, 0, len(list)-1, x)
    if result != -1:
        print("X is at index: " + str(result))
    else:
        print("X is not in range")
