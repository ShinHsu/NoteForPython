def slsl(lst6):
    for i in range(len(lst6)):
        if lst6[i] > min(lst6[i+1:]): 
            lst6[lst6.index(min(lst6[i+1:]))], lst6[i] = lst6[i], lst6.index(min(lst6[i+1:]))
    return lst6

d = [2,4,5,1,2]
slsl(d)