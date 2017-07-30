import matplotlib.pyplot as plt
import numpy as np
from baseline import baseline
from basic_REG import basic
from enhanced_REG import enhanced

if __name__ == "__main__":

    x = [i for i in range(20,51)]
    baseline_y = []
    # basic_y = []
    # enhanced_y = []
    for L in x:
    #     print (L)
         a = baseline(L)
    #     b = basic(L)
    #     c = enhanced(L)
    #     #print (a,b,c)
         baseline_y.append(a)
    #     basic_y.append(b)
    #     enhanced_y.append(c)
    #
    # print ("Finish computing!")
    #
    # data = np.array([baseline_y, basic_y, enhanced_y])
    # np.save('data1.npy', data)
    # print ("Finish Save Numpy")

    data = np.load('data1.npy')
    #baseline_y = data[0]
    basic_y = data[1]
    enhanced_y = data[2]


    plt.figure()
    plt.xlabel('Budget L', fontsize=17)
    plt.ylabel('TQoI', fontsize=17)
    plt.axis([20, 40, 15, 50])

    plt.plot(x, baseline_y, color='r', marker = 's', label="MCQBC") #linewidth

    plt.plot(x, basic_y, color='g', marker='o', label="Basic-REG")

    plt.plot(x, enhanced_y, color='b', marker='D', label="Enhanced-REG")

    plt.legend(loc='upper left')

    plt.show()

    print ("Finish figure!")


