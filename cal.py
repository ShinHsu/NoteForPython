def finx_max(lst):
    max = 0
    pos = 0
    for i in range(len(lst) + 1):
        print(i)
        if lst[i] > max:
            max = lst[i]
            pos = i
            
    return i

lst = [17, 92, 18, 33, 58, 7, 33, 42]
find_max(lst)