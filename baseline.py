import os
import operator
import random
import pickle


def max_margin(S, covered, bid, weight):
    max_ratio = 0
    cur_seq = []
    cur_weightsum = 0
    cur_bidsum = 0
    # users and objects of a certain sequence
    for seq in S:
        users = seq[0]  # list
        objects = seq[1]  # list
        # print (users, objects)

        # calculate marginal weights
        marginal_weight = 0
        for object in objects:
            if object not in covered:
                marginal_weight = marginal_weight + weight[object]

        # calculate costs needed paying
        bidsum = 0
        for user in users:
            bidsum = bidsum + bid[user]

        # print (marginal_weight/total_bid)
        if marginal_weight / bidsum > max_ratio:
            max_ratio = marginal_weight / bidsum
            cur_seq = seq
            cur_weightsum = marginal_weight
            cur_bidsum = bidsum

    # print (max_ratio)
    # print (max_seq)

    return cur_seq, cur_weightsum, cur_bidsum




def baseline(L):
    # load pickle
    f = open('userSeqs.pkl', 'rb')
    user_seqs = pickle.load(f)
    f.close()

    # total 36 users
    random.seed(0)
    upload_rate = 0.7
    uploaded_users = random.sample([i for i in range(1,37)], int(upload_rate*36))
    uploaded_users.sort()
    #print (uploaded_users)

    # all the uploaded sequences are put in this dict
    seqs_dict = {}
    for user in uploaded_users:
        seqs_dict.update(user_seqs[user])
    #print (len(seqs_dict))


    # count the times a certain user appears in all sequences
    #seqs_list = []
    appear = {}
    for user in range(1,37):
        appear[user] = 0
    for users, objects in seqs_dict.items():
        users_list = [int(user) for user in users.split(',')]
        for user in users_list:
            appear[user] = appear[user] + 1
        #seqs_list.append([users_list, objects])
    #seqs_list.sort(key=operator.itemgetter(0))
    #print(seqs_list)
    #print (appear)

    #===========================================above are used to calculate the dict appear.===================================


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

    seqs_list = []
    for user in uploaded_users:
        if len(user_seqs[user])!=0:
            seqs_list.append([[user],user_seqs[user]])
    #print (seqs_list)



    # initialization for object weights and user bids
    weight = {}
    for object in range(37,55):
        #weight[object] = random.randint(1,10)
        weight[object] = random.uniform(1,5)

    bid = {}
    cnt = {}
    for user in range(1,37):
        bid[user] = random.uniform(2,8)#
        cnt[user] = 0
    bid[33]=10;
    bid[29]=10
    bid[30]=10
    bid[24]=10

    for user in range(1,37):
        bid[user] = int(bid[user]*appear[user]/1) #divide for picture 1
    covered = [] # objects covered in F
    # L = 25     # total budget
    B = 0       # total cost of sequences in F
    F = []      # selected sequences
    W = 0       # total weight selected
    S = seqs_list.copy()



    while len(S)!=0:
        cur_seq, cur_weightsum, cur_bidsum = max_margin(S,covered,bid,weight)
        if cur_weightsum == 0:
            break
        if B+cur_bidsum <= L: # accept the sequence
            F.append(cur_seq)
            B = B + cur_bidsum
            W = W + cur_weightsum
            for object in cur_seq[1]:
                if object not in covered:
                    covered.append(object)

            for user in cur_seq[0]:
                bid[user] = bid[user] + 1 # update the bids of users if they are choosen
                cnt[user] = cnt[user] + 1

        S.remove(cur_seq)

    #print (F)
    #print (W)


    max_W = 0
    max_seq = []
    for [users, objects] in seqs_list:
        B_t = 0
        for user in users:
            B_t = B_t + bid[user]
        if B_t>L:
            continue

        W_t = 0
        for object in objects:
            W_t = W_t + weight[object]

        if W_t>max_W:
            max_W = W_t
            max_seq = [users, objects]

    #print (max_seq)
    #print (max_W)

    #print("Final Result:")
    result_seqs = []
    result_W = 0
    if (W > max_W):
        result_seqs = F
        result_W = W
    else:
        result_seqs = max_seq
        result_W = max_W
    #print(result_seqs)
    #print(result_W)

    return result_W







if __name__ == "__main__":
    # L = 30
    # res = baseline(L)
    # print (res)

    for i in range(20,50):
        print (i, baseline(i))