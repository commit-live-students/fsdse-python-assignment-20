def solution(dic1):
    list1 = []
    sorted_list = []
    for key in dic1:
        tuples = key, dic1[key]
        #print tuples
        list1.append(tuples)
    #print list1
    sorted_list = sorted(list1)
    return sorted_list

dict1 = {1: 10, 2: 20, 3: 30, 4: 40}
solution(dict1)
