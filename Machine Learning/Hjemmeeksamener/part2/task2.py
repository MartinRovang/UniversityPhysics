

# Import data
import numpy as np
import matplotlib.pyplot as plt
import machinepy as ml
import time

# Load data
test_data = np.genfromtxt('seals_test.csv')
training_data = np.genfromtxt('seals_train.csv')



#% of data set
p = 0.10
dist = int(len(training_data)*p)

# Initaite training, validation and parameter list
tr = []
val = []
de = []


# Set up training and validation
training = np.copy(training_data)[dist:,:]
validation = np.copy(training_data)[0:dist,:]
my_tree = ml.Tree()

# use timer to time the algorithm
import time
for i in range(1,9):

    e0 = time.time()
    #
    tree = my_tree.fit(training, i)
    #
    elapsed_time = time.time() - e0

    # Create tree object
    my_tree.node_stats(tree)
    # Make confusion matrix for training set
    mat = np.array([[my_tree.class0pos,my_tree.class0neg],[my_tree.class1neg,my_tree.class1pos]])
    # Find accuracy
    accuracy = sum(np.diag(np.copy(mat)))/sum(sum(np.copy(mat)))
    print(f'Accuracy training:{accuracy*100:.2f} %')
    tr.append(accuracy*100)


    #Make confusion matrix for validation set
    confusion_mat = np.zeros((2,2))
    for row in validation:
        predicted = my_tree.predict(row, tree)
        if predicted[1] == 'Class 0':
            if row[0] == 0:
                confusion_mat[0,0] += 1
            else:
                confusion_mat[0,1] += 1
        else:
            if row[0] == 1:
                confusion_mat[1,1] += 1
            else:
                confusion_mat[1,0] += 1

    # print out accuracy and confusion matrix for validation set
    print(confusion_mat)
    confusion_mat = np.array(confusion_mat)
    accuracy = sum(np.diag(np.copy(confusion_mat)))/sum(sum(np.copy(confusion_mat)))
    print(f'Accuracy testing:{accuracy*100:.2f} %')

    val.append(accuracy*100)
    de.append(int(max(my_tree.nodenumber)))

    # print out deopth of the tree
    print('Depth: ',max(my_tree.nodenumber))
    print('Tree building took: %.2f minutes'%(float(elapsed_time)/60))

# Plot
print(tr)
print(val)
plt.plot(de, tr, label = 'Training')
plt.plot(de, val, label = 'Validation')
plt.legend()
plt.ylabel('Accuracy')
plt.xlabel('Depth')
plt.show()



# Load training set
training_data = np.genfromtxt('seals_train.csv')

# avoid pointing to data set
training = np.copy(training_data)
test = np.copy(test_data)

# make tree
my_tree = ml.Tree()

# make timer
import time
e0 = time.time()
#
tree = my_tree.fit(training, 4)
#
elapsed_time = time.time() - e0

# Print node stats of tree / tree structure
my_tree.node_stats(tree)
# confusion matrix for training
mat = np.array([[my_tree.class0pos,my_tree.class0neg],[my_tree.class1neg,my_tree.class1pos]])
accuracy = sum(np.diag(np.copy(mat)))/sum(sum(np.copy(mat)))
print(f'Accuracy training:{accuracy*100:.2f} %')


# Make confusion matrix
confusion_mat = np.zeros((2,2))
# each image/row in the test data
for row in test:
    predicted = my_tree.predict(row, tree)
    if predicted[1] == 'Class 0':
        if row[0] == 0:
            confusion_mat[0,0] += 1
        else:
            confusion_mat[1,0] += 1
    else:
        if row[0] == 1:
            confusion_mat[1,1] += 1
        else:
            confusion_mat[0,1] += 1

# Print out confusion matrix
print(confusion_mat)
confusion_mat = np.array(confusion_mat)
accuracy = sum(np.diag(np.copy(confusion_mat)))/sum(sum(np.copy(confusion_mat)))
print(f'Accuracy testing:{accuracy*100:.2f} %')

# get depth and how long it took to make tree
print('Depth: ',max(my_tree.nodenumber))
print('Tree building took: %.2f minutes'%(float(elapsed_time)/60))
