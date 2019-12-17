def comp(arr1, arr2):
    if arr1 > arr2 : return arr1
    else : return arr2 
    
def find_max(lst, index):
    if index == 1: return comp(lst[index], lst[index-1])
    return comp(lst[index], find_max(lst, index-1))

lst = [17, 60, 18, 33, 90, 7, 33, 42]
print(find_max(lst, len(lst) - 1))