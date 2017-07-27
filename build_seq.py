import os
import operator
import random

path = "data\\imote-traces-cambridge\\SR-10mins-Students"

contact_list = [] # the contents are in the form [meet_time, user1, user2], where user1 meets user2.
u_meet_u = [] # user meets another user
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
        if id<=36:
            u_meet_u.append([time, i, id])
        if id>36 and id<=54:
            u_meet_o.append([time, i, id])

        # if id<=54: # id in range [0:54] are useful
        #     contact_list.append([time, i, id])


random.seed(0)
contact_list = random.sample(u_meet_u, int(len(u_meet_u)/20)) # random sample one-tenth of the data
contact_list.extend(u_meet_o)
contact_list.sort(key=operator.itemgetter(0)) # sort by the meet time
print (len(contact_list))

min_time = contact_list[0][0]
max_time = contact_list[-1][0]
#print (min_time)
#print (max_time)

# # This part is for display the meeting time
# time_dict = {}
# meet_place_dict = {}
# gap = (max_time-min_time)/10
# for meet in contact_list:
#     tmp = int((meet[0]-min_time)/gap)
#     if tmp not in time_dict:
#         time_dict[tmp] = 1
#     else:
#         time_dict[tmp] = time_dict[tmp] + 1
#
#     user2 = meet[2]
#     if user2 > 36 and user2 <= 54:
#         if tmp not in meet_place_dict:
#             meet_place_dict[tmp] = 1
#         else:
#             meet_place_dict[tmp] = meet_place_dict[tmp] + 1
#
#
# for i in range(0,10):
#     print (time_dict[i], meet_place_dict[i])





# max_user_num = 5
user_seqs = {}
for user in range(1,37):
    user_seqs[user] = {} # seqs for a certain users are stored in dictionary


run_time = len(contact_list)
count = 0
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

            previous = users.split(',')
            # if len(previous)==max_user_num: # if the users number exceeds, continue
            #     continue
            if str(user1) in previous: # user1 appears in one suquence of user2 = =
                continue

            new_users = str(users)+','+str(user1)
            user_seqs[user1][new_users] = objects

    count = count+1
    if (count%int(run_time/100)==0):
        print (count/int(run_time/100))
    if count==run_time:
        break
print ("Finish Generate Sequences.")

seqs_count = 0
for i in user_seqs:
    seqs_count = seqs_count + len(user_seqs[i])
print (seqs_count)



