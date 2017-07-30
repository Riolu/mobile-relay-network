import matplotlib.pyplot as plt
import numpy as np
from enhanced_REG_compare3 import enhanced_compare
from PA_REG import penalty_adaptive

if __name__ == "__main__":

    x = [i for i in range(20,51)]
    # enhanced_weight = []
    # enhanced_penalty = []
    # penalty_apt_weight = []
    # penalty_apt_penalty = []
    #
    # for L in x:
    #     print (L)
    #     a_w, a_p = enhanced_compare(L)
    #     b_w, b_p = penalty_adaptive(L)
    #     print (a_w, a_p, b_w, b_p)
    #
    #     enhanced_weight.append(a_w)
    #     enhanced_penalty.append(a_p)
    #     penalty_apt_weight.append(b_w)
    #     penalty_apt_penalty.append(b_p)
    #
    # print ("Finish computing!")
    #
    # data = np.array([enhanced_weight, enhanced_penalty, penalty_apt_weight, penalty_apt_penalty])
    # np.save('data2.npy', data)
    # print ("Finish Save Numpy")

    data = np.load('data2.npy')
    enhanced_weight = data[0]
    enhanced_penalty = data[1]
    penalty_apt_weight = data[2]
    penalty_apt_penalty = data[3]

    for i in range(len(enhanced_weight)):
        if i==0:
            continue
        if enhanced_weight[i]<enhanced_weight[i-1]:
            enhanced_weight[i] = enhanced_weight[i-1]
            enhanced_penalty[i] = enhanced_penalty[i-1]

    #print (enhanced_penalty)
    #print (penalty_apt_penalty)




    plt.figure(1)
    plt.xlabel('Budget L', fontsize=17)
    plt.ylabel('TQoI', fontsize=17)
    plt.axis([20, 40, 10, 50])
    plt.plot(x, enhanced_weight, color='b', marker = 's', label="Enhanced-REG") #linewidth blue
    plt.plot(x, penalty_apt_weight, color='c', marker='o', label="Penalty-adaptive")
    plt.legend(loc='upper left')

    plt.figure(2)
    plt.xlabel('Budget L', fontsize=17)
    plt.ylabel('Penalty', fontsize=17)
    plt.axis([20, 40, 1, 8])
    plt.plot(x, enhanced_penalty, color='b', marker='s', label="Enhanced-REG")  # linewidth
    plt.plot(x, penalty_apt_penalty, color='c', marker='o', label="Penalty-adaptive")
    plt.legend(loc='upper left')

    plt.show()

    print ("Finish figure!")


