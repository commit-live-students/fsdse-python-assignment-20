def solution(dic1):
    list1 = []
    for key in dic1:

        list1.append((key , dic1[key]))

    return list1

print solution({1: 10, 2: 20, 3: 30, 4: 40})
