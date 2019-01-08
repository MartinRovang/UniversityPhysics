

# Import data
import numpy as np
import matplotlib.pyplot as plt
import machinepy as ml
import time

# Load data
test_data = np.genfromtxt('seals_test.csv')
training_data = np.genfromtxt('seals_train.csv')

# percentage of data
p = 0.1
percentage_data = int((len(training_data)*p))

#Split data into training and validation data
validation_data = np.copy(training_data)[0:percentage_data,:]
training_data = np.copy(training_data)[percentage_data:,:]


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

# Copy to avoid pointers to data set
validation = np.copy(validation_data)
validation_cl = clean_test(validation)

training = np.copy(training_data)
training_cl = clean_test(training)

# Set ones in first column
validation[:,0] = 1
training[:,0] = 1

test = np.copy(test_data)
data = clean_test(test)
# Sets object with logistic discrimination and assign training data
y = ml.predictor(training = training_data)


#Trains the model
val = []
tra = []
lrr = []
lr = 0.000001
for i in range(1,11):
    y.train(lr, it = 600)
    #Print out the predictions
    tra.append(y.conf_mat(training_cl[0],training_cl[1])[0])
    #Show confusion matrix of the test data.
    val.append(y.conf_mat(validation_cl[0],validation_cl[1])[0])


    # y.conf_mat(data[0],data[1])

    # append the current learning rate
    lrr.append(lr)
    lr += lr



# Plot data
plt.plot(lrr,val,'--', label = 'Validation')
plt.plot(lrr,tra, label = 'Training')
plt.ylabel('Accuracy %',fontsize = 15)
plt.xlabel('Learning rate',fontsize = 15)
plt.title('Accuracy of training vs validation',fontsize = 20)
plt.legend(loc = 'best')

plt.show()



test = np.copy(test_data)
data = clean_test(test)


# Sets object with logistic discrimination and assign training data
y = ml.predictor(training = training_data, decision= 0.5)


y.train(3.18e-5,it = 600)
 #Print out the predictions
print(y.conf_mat(data[0],data[1])[1])

y.plterror()
plt.show()

lst = []
for i in range(0,100):
    test = np.copy(test_data)[i,:]
    y = ml.predictor(training = training_data, decision= 0.5)
    y.train(3.18e-5,it = 600)
    classif = test[0]
    test[0] = 1
    if y.predict(test) != classif:
        lst.append(i)
print(lst)

