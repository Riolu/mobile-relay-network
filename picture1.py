import matplotlib.pyplot as plt
import numpy as np
from baseline import baseline
from basic_REG import basic
from enhanced_REG import enhanced

if __name__ == "__main__":

    x = [i for i in range(25,27)]
    baseline_y = []
    basic_y = []
    enhanced_y = []
    for L in x:
        a = baseline(L)
        b = basic(L)
        c = enhanced(L)
        #print (a,b,c)
        baseline_y.append(a)
        basic_y.append(b)
        enhanced_y.append(c)

    print ("Finish computing!")

    data = np.array([baseline_y, basic_y, enhanced_y])
    np.save('data.npy', data)
    print ("Finish Save Numpy")


    plt.figure()
    plt.plot(x, baseline_y)
    plt.plot(x, basic_y)
    plt.plot(x, enhanced_y)
    plt.show()

    print ("Finish figure!")


