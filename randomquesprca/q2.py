keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]


def listtodict(l1,l2):
    d = {}
    for i,j in zip(l1,l2):
        d[i] = j
    return d
        
        

print(listtodict(keys,values))