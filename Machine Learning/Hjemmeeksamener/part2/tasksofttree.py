# Import data
import numpy as np
import matplotlib.pyplot as plt
import machinepy2 as ml
import time

# Load data
test_data = np.genfromtxt('seals_test.csv')
training_data = np.genfromtxt('seals_train.csv')



# avoid pointing to data set
training = np.copy(training_data)
test = np.copy(test_data)

# make tree
my_tree = ml.softTree()

# make timer
import time
e0 = time.time()
#
tree = my_tree.fit(training, 4)
#
elapsed_time = time.time() - e0

# Print node stats of tree / tree structure and make stats for confusion matrix
my_tree.node_stats(tree)
print('Depth: ',max(my_tree.nodenumber))
mat = np.array([[my_tree.class0pos,my_tree.class0neg],[my_tree.class1neg,my_tree.class1pos]])
accuracy = sum(np.diag(np.copy(mat)))/sum(sum(np.copy(mat)))
print(f'Accuracy training:{accuracy*100:.2f} %')

tp = []
fp = []

for i in np.linspace(0.01,0.99, 10):
    # Make confusion matrix
    confusion_mat = np.zeros((2,2))
    for row in test:
        predicted = my_tree.predict(row, tree, i)
        if predicted == 'Class 0':
            if row[0] == 0:
                confusion_mat[0,0] += 1
            else:
                confusion_mat[1,0] += 1
        else:
            if row[0] == 1:
                confusion_mat[1,1] += 1
            else:
                confusion_mat[0,1] += 1

    res = confusion_mat
    print(res)
    print(i)
    # get tp and fp rate
    y = float((res[0,0]/(res[0,0]+res[0,1])))
    x = float((res[1,0]/(res[1,0]+res[1,1])))
    plt.plot(x,y,'X', markersize = 10, label = 'Boundary: %.2f'%i)
    tp.append(y)
    fp.append(x)

# sort for doing integral
tp = sorted(tp)
fp = sorted(fp)

# Find area
print('AUC: %.2f '%(np.trapz(y = tp, x = fp)))
plt.plot(fp,tp, label = 'ROC curve')
plt.plot([0,1],[0,1],'--', label = 'Better/Worse line')
plt.title('ROC curve of decision tree', fontsize = '20')
plt.xlabel('fp-rate ', fontsize = '15')
plt.ylabel('tp-rate', fontsize = '15')
plt.legend(loc = 'best')
plt.show()
