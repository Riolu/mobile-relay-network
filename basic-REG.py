import pickle
import random
import operator

# load pickle
f = open('userSeqs.pkl', 'rb')
user_seqs = pickle.load(f)
f.close()

# total 36 users
random.seed(0)
upload_rate = 0.5
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
    seqs_list.append([users, objects])
seqs_list.sort(key=operator.itemgetter(0))
#print (len(seqs_list))



# initialization for object weights and user bids
weight = {}
for object in range(37,55):
    weight[object] = random.randint(1,10)

bid = {}
for user in range(1,37):
    bid[user] = random.randint(1,5)



covered = [] # objects covered in F
L = 500     # total budget
B = 0       # total cost of sequences in F
F = []      # selected sequences
cnt = {}
for user in range(1,37):
    cnt[user] = 0



def max_margin():
    max_marginal = 0
    max_seq = []
    # users and objects of a certain sequence
    for seq in seqs_list:
        users = seq[0]      # string
        objects = seq[1]    # list
        #print (users, objects)

        # calculate marginal weights
        marginal_weight = 0
        for object in objects:
            if object not in covered:
                marginal_weight = marginal_weight + weight[object]

        # calculate costs needed paying
        total_bid = 0
        user_list = users.split(',')
        for user in user_list:
            total_bid = total_bid + bid[int(user)]

        #print (marginal_weight/total_bid)
        if marginal_weight/total_bid > max_marginal:
            max_marginal = marginal_weight/total_bid
            max_seq = seq

    #print (max_marginal)
    #print (max_seq)

    return max_seq, marginal_weight, total_bid

#max_margin()

while len(seqs_dict)!=0:
    max_seq, marginal_weight, total_bid = max_margin()
    if marginal_weight == 0:
        break
    if B+total_bid <= L:
        F.append(max_seq)











