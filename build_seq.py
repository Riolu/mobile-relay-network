import os

path = "data\\imote-traces-cambridge\\SR-10mins-Students"


contact_dic = {}
min_time = pow(10,10)

for i in range(1, 37):
    filename = str(i)+".dat"
    filename = os.path.join(path, filename)

    list = []
    file = open(filename)
    for line in file:
        data_split = line.split()
        id = int(data_split[0])
        time = int(data_split[1])
        if id<=54: # id in range [0:54] are useful
            min_time = min(time, min_time)
            list.append([id, time])

    contact_dic[i] = list

print (min_time)
print (contact_dic)


