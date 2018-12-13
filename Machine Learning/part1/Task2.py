
# # Task 2

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

#Import data
data = np.genfromtxt('data\optdigits-1d-train.csv')
alpha = 9

#putting each class in its own list for finding priors and for training
C0 = []
C1 = []
#sorting classes
for i in data:
    if i[0] == 0:
        C0.append(i[1])
        
    elif i[0] == 1:
        C1.append(i[1])
        
C0 = np.array(C0)
C1 = np.array(C1)
#Priors for each class
C0_prior = len(C0)/(len(C0)+len(C1))
C1_prior = len(C1)/(len(C0)+len(C1))

#The estimated parameters for gamma distribution and normal distribution
beta = (1/(len(C0)*alpha))*sum(C0)
mu = (1/len(C1))*sum(C1)
variance = (1/len(C1))*sum((C1-mu)**2)    


def gammadistr(x,alpha,beta):
    """
    The gammadistr function takes in the datapoint or an numpy array, alpha parameter and the beta parameter as arguments
    the result of the gamma distribution is then returned.
    """
    #as long as alpha is bigger then 0 and integer
    Tau_alpha = math.factorial(alpha - 1)
    result = (1/(beta**alpha*Tau_alpha))*x**(alpha-1)*np.exp(-x/beta)
    return result



def normaldistr(x,mu,variance):
    """
    The normaldistr function takes in the data point or an numpy array, mu and variance parameters
    the function the returns the values of the normal distribution.
    """
    result = (1/(np.sqrt(2*np.pi*variance)))*np.exp(-((x - mu)**2)/(2*variance))
    return result


#values to plot the 'continues' distributions
x1 = np.linspace(0.5,1.2,100)
x = np.linspace(0,0.4,100)


#values to plot the 'continues' distributions
P_C0 = gammadistr(x,alpha,beta)
P_C1 = normaldistr(x1,mu,variance)


#Plotting the histogram and distributions together in one plot
plt.figure(figsize = (20,10))
plt.hist(C0, bins = 50, label = 'Class 0',density = True)
plt.plot(x,P_C0, label = 'Class 0 distribution')
plt.hist(C1,bins = 50, label = 'Class 1',density = True)
plt.plot(x1,P_C1, label = 'Class 2 distribution')
plt.legend(loc = 'best', prop={'size': 20})
plt.ylabel('Datapoints',fontsize = 20)
plt.xlabel('Linear projection',fontsize = 20)
plt.show()



# In[9]:


#Import seaborn to make nice confusion matrix
import seaborn as sns

#Importing training data
data = np.genfromtxt('data\optdigits-1d-train.csv')


def bayes_class(data,alpha,beta,mu,variance,C0_prior,C1_prior):
    """
    The bayes_class function takes in the data, alpha and beta parameters for the gamma distribution
    and the mu and variance of the normal distribution, and the prior probability for class 0 and for class1.
    The data is then classified using the bayes theorem without the equal terms.
    Here the results is added into a result list where the output is zero for class 0 and one for class 1.
    """
    
    result = []
    for x in data:
        P_C0 = gammadistr(x,alpha,beta)
        P_C1 = normaldistr(x,mu,variance)

        if C0_prior*P_C0 > C1_prior*P_C1:
            result.append(0)
        else:
            result.append(1)
            
        
    return result

#Adding training data to the classifier
C0_bayes = bayes_class(C0,alpha,beta,mu,variance,C0_prior,C1_prior)
C1_bayes = bayes_class(C1,alpha,beta,mu,variance,C0_prior,C1_prior)


def confusion_matrix(data0_train,data1_train):
    """
    The confustion_matrix function takes in the training data for class 0 and training data for class 1
    then the data is training with the classifier and the results are sorted in a 2x2 matrix with the True positives and True negatives
    are given on the diagonal axis.
    """
    data0_train = bayes_class(data0_train,alpha,beta,mu,variance,C0_prior,C1_prior)
    data1_train = bayes_class(data1_train,alpha,beta,mu,variance,C0_prior,C1_prior)
    
    confusion_mat = np.zeros((2,2))
    class0_0 = 0
    class0_1 = 0
    class1_1 = 0
    class1_0 = 0
    #Sorting the results
    for i in data0_train:
        if i == 0:
            confusion_mat[0,0] += 1
        else:
            confusion_mat[0,1] += 1
    for i in data1_train:
        if i == 1:
            confusion_mat[1,1] += 1
        else:
            confusion_mat[1,0] += 1
    
    return confusion_mat

    
    
#Setting up the confusion matrix
df_cm = pd.DataFrame(confusion_matrix(C0,C1), index = [i for i in ["Prediction class 0","Prediction class 1"]],
                  columns = [i for i in ["Class 0","Class 1"]])

#plotting the confustion matrix with seaborn heatmap
plt.figure(figsize = (10,5))
sns.heatmap(df_cm, linewidths=1 , cmap="YlGnBu",cbar=False, annot=True,fmt='g', annot_kws={"size": 10})
plt.title('Confusion Matrix',fontsize = 20)
plt.show()


#Finding the accuracy of the prediction
#https://en.wikipedia.org/wiki/Confusion_matrix
#Taking the sum of the true positives and negatives divided by the total population
Population = sum(sum(confusion_matrix(C0,C1)))
Accuracy = sum(np.diag(confusion_matrix(C0,C1)))/Population

print('Accuracy of the prediction: ',Accuracy)


# In[10]:


#Importing the utility python module.
from he1_util import get_msg_for_labels

#Importing the test data
data_test = np.genfromtxt('data\optdigits-1d-test.csv')

#Printing out the secret message
print('The secret message is,',get_msg_for_labels(bayes_class(data_test,alpha,beta,mu,variance,C0_prior,C1_prior)))



