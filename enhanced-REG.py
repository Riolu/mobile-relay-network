import pickle
import random
import operator
import itertools

# load pickle
f = open('userSeqs.pkl', 'rb')
user_seqs = pickle.load(f)
f.close()

# total 36 users
random.seed(0)
upload_rate = 0.1
uploaded_users = random.sample([i for i in range(1,37)], int(upload_rate*36))
uploaded_users.sort()
#print (uploaded_users)

# all the uploaded sequences are put in this dict
seqs_dict = {}
for user in uploaded_users:
    seqs_dict.update(user_seqs[user])
#print (len(seqs_dict))

# the reason transfer seqs_dict to seqs_list is the order is fixed in list
seqs_list = []
for users, objects in seqs_dict.items():
    users_list = [int(user) for user in users.split(',')]
    seqs_list.append([users_list, objects])
seqs_list.sort(key=operator.itemgetter(0))
print ("sequence num:", len(seqs_list))



# initialization for object weights
weight = {}
for object in range(37,55):
    #weight[object] = random.randint(1,10)
    weight[object] = random.gauss(5,1)

bid = {}
cnt = {}
for user in range(1,37):
    bid[user] = random.randint(1,5)
    cnt[user] = 0

L = 500     # total budget


def max_margin(covered,S,bid):
    max_ratio = 0
    cur_seq = []
    cur_weightsum = 0
    cur_bidsum = 0
    # users and objects of a certain sequence
    for seq in S:
        users = seq[0]      # list
        objects = seq[1]    # list
        #print (users, objects)

        # calculate marginal weights
        marginal_weight = 0
        for object in objects:
            if object not in covered:
                marginal_weight = marginal_weight + weight[object]

        # calculate costs needed paying
        bidsum = 0
        for user in users:
            bidsum = bidsum + bid[user]

        #print (marginal_weight/total_bid)
        if marginal_weight/bidsum > max_ratio:
            max_ratio = marginal_weight/bidsum
            cur_seq = seq
            cur_weightsum = marginal_weight
            cur_bidsum = bidsum

    #print (max_ratio)
    #print (max_seq)

    return cur_seq, cur_weightsum, cur_bidsum

# max_margin()


k = 3
H2 = []
W_H2 = 0
permuate = list( itertools.permutations(seqs_list,k) )
for tuples in permuate:
    F = []  # selected sequences
    B = 0  # total cost of sequences in F
    W = 0  # total weight selected
    covered = []  # objects covered in F
    S = seqs_list.copy()
    cur_bid = bid.copy()
    cur_cnt = cnt.copy()

    #print (tuples)
    for [users, objects] in tuples:
        F.append([users, objects])
        for user in users:
            B = B + cur_bid[user]
        for object in objects:
            if object not in covered:
                W = W + weight[object]
                covered.append(object)
        S.remove([users, objects])
        for user in users:
            cur_bid[user] = cur_bid[user] + 1
            cur_cnt[user] = cur_bid[user] + 1

    if B>L:
        continue

    while len(S)!=0:
        cur_seq, cur_weightsum, cur_bidsum = max_margin(covered,S,cur_bid)
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
                cur_bid[user] = cur_bid[user] + 1 # update the bids of users if they are choosen
                cur_cnt[user] = cur_cnt[user] + 1

        S.remove(cur_seq)

    if W>W_H2:
        H2 = F
        W_H2 = W

print (H2)
print (W_H2)




W_H1 = 0
H1 = []
permuate_num = k-1
while permuate_num>=1:
    permuate_2 = list( itertools.permutations(seqs_list,k-1) )
    for tuples in permuate_2:
        total_cost = 0
        total_weight = 0
        cur_bid = bid.copy()
        tmp_list = []
        covered = []

        for [users, objects] in tuples:
            tmp_list.append([users, objects])
            for user in users:
                total_cost = total_cost + cur_bid[user]
                cur_bid[user] = cur_bid[user] + 1
            for object in objects:
                if object not in covered:
                    total_weight = total_weight + weight[object]
                    covered.append(object)

        if total_cost > L:
            continue

        if total_weight > W_H1:
            W_H1 = total_weight
            H1 = tmp_list

    permuate_num = permuate_num-1


print (H1)
print (W_H1)



# result_seqs = []
# result_W = 0
# if (W_H1>W_H2):
#     result_seqs = H1
#     result_W = W_H1
# else:
#     result_seqs = H2
#     result_W = W_H2
#
#
# print (result_seqs)
# print (result_W)







