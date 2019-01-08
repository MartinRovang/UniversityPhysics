

# Import data
import numpy as np
import matplotlib.pyplot as plt
import machinepy as ml
import time

test_data = np.genfromtxt('seals_test.csv')
training_data = np.genfromtxt('seals_train.csv')

def clean_test(x):
    """Order the data into classes for the confusion matrix"""
    class1 = []
    class2 = []


    for row in x:
        if row[0] == 0:
            class1.append(row)
        else:
            class2.append(row)


    class1 = np.array(class1)
    class2 = np.array(class2)

    class1[:,0] = 1
    class2[:,0] = 1

    return class1, class2



test = np.copy(test_data)
data = clean_test(test)

tp = []
fp = []

lr = 3.18e-5
for i in np.linspace(0.01,0.99, 10):
    y = ml.predictor(training = training_data, decision = i)
    y.train(lr, it = 20)
    res = y.conf_mat(data[0],data[1])[1]
    y = (res[0,0]/(res[0,0]+res[0,1]))
    x = (res[1,0]/(res[1,0]+res[1,1]))

    plt.plot(x,y,'X', markersize = 10, label = 'Boundary: %.1f'%i)
    #print(res[0,0]+res[1,0])
    tp.append(y)
    fp.append(x)

tp = sorted(tp)
fp = sorted(fp)
# Find area under curve with trapezoid rule
print('AUC: %.2f '%(np.trapz(y = tp, x = fp)))
plt.plot(fp,tp, label = 'ROC curve')
plt.plot([0,1],[0,1],'--', label = 'Better/Worse line')
plt.title('ROC curve of logistic discrimination', fontsize = '20')
plt.xlabel('fp-rate ', fontsize = '15')
plt.ylabel('tp-rate', fontsize = '15')
plt.legend(loc = 'best')
plt.show()
