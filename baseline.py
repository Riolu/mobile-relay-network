import os
import operator
import random
import pickle

path = "data\\imote-traces-cambridge\\SR-10mins-Students"

contact_list = [] # the contents are in the form [meet_time, user1, user2], where user1 meets user2.
u_meet_o = [] # user meets an object

# ID [1:36] are users; [37:54] are locations
for i in range(1, 37):
    filename = str(i)+".dat"
    filename = os.path.join(path, filename)

    list = []
    file = open(filename)
    for line in file:
        data_split = line.split()
        id = int(data_split[0])
        time = int(data_split[1])
        if id>36 and id<=54:
            u_meet_o.append([time, i, id])



contact_list.extend(u_meet_o)
contact_list.sort(key=operator.itemgetter(0)) # sort by the meet time
#print (contact_list)



user_seqs = {}
for user in range(1,37):
    user_seqs[user] = [] # record objects this user visited

for [time, user, object] in contact_list:
    if object not in user_seqs[user]:
        user_seqs[user].append(object)

# for user in user_seqs:
#     print (user_seqs[user])
# print ("===========================")



# total 36 users
random.seed(0)
upload_rate = 0.7
uploaded_users = random.sample([i for i in range(1,37)], int(upload_rate*36))
uploaded_users.sort()
#print (uploaded_users)


seqs_list = []
for user in uploaded_users:
    seqs_list.append([[user],user_seqs[user]])
#print (seqs_list)


# specific method





