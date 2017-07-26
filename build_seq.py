import os
import operator

path = "data\\imote-traces-cambridge\\SR-10mins-Students"

contact_list = [] # the contents are in the form [meet_time, user1, user2], where user1 meets user2.

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
        if id<=54: # id in range [0:54] are useful
            contact_list.append([time, i, id])

# sort by the meet time
contact_list.sort(key=operator.itemgetter(0))


min_time = contact_list[0][0]
max_time = contact_list[-1][0]
#print (min_time)
#print (max_time)

print (len(contact_list))


user_seqs = {}
for user in range(1,37):
    user_seqs[user] = {} # seqs for a certain users are stored in dictionary


count = 500
for meet in contact_list:
    user1 = meet[1]
    user2 = meet[2]

    # user2 is a location
    if user2>36 and user2<=54:
        seqs_dict = user_seqs[user1]
        if str(user1) not in seqs_dict:
            seqs_dict[str(user1)] = []
        seqs_list = seqs_dict[str(user1)]
        if user2 not in seqs_list:
            seqs_list.append(user2)


    else:
    # here user1 detects user2, then the sequences of users2 are copied and add to user1
        seqs_dict = user_seqs[user2]
        for users in seqs_dict:
            # variable users is string while objects is list
            objects = seqs_dict[users]

            if users == (str(user1)+','+str(user2)): #?
                continue

            new_users = str(users)+','+str(user1)
            user_seqs[user1][new_users] = objects

    count = count-1
    if count==0:
        break


print (user_seqs)



