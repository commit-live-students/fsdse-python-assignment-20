def solution(dic1):
    key_list = dic1.keys()
    val_list = dic1.values()

    sor_list = []

    for i in range(len(key_list)):
        c = (key_list[i], val_list[i])
        sor_list.append(c)

    sorted(sor_list,key=lambda l:l[0], reverse=True)
    print sor_list
    return sor_list
