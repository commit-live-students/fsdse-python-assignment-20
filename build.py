
def solution(dic1):
    list1=[]
    for (k,v) in dic1.items():
        list1.append((k,v))
    return list1
print solution({1: 10, 2: 20, 3: 30})
