
# coding: utf-8

# In[1]:


#Import needed modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Importing data to variables to dataframe and numpy arrays.
data = np.genfromtxt('data\chess-games.csv')
datanames = pd.read_csv('data\chess-games-names.csv', header=None)
chessname = np.copy(datanames)
chessdata = np.copy(data)


# In[2]:


#Grapping names only from original data
name_lst = []
for name in chessname:
    name_lst.append(name[1])


# In[3]:


def make_transitionmat(chessdata):
    """
    make_transitionmat function takes in the chessdata as argument the function will then
    sort the dataframe into a NxN transition matrix and return it.
    """
    
    #Initate empty 291X291 matrix (all players)
    A = np.zeros((291,291))
    #each row containing player id white, black and if win/tie/loss
    for match in chessdata:
        #If white won then black lost, holding row(black id) and column (white id)
        if match[2] == 1:
            #Typecasting to int because data is taken as string.
            row = int(match[1])
            column = int(match[0])
        #If black won then white lost, holding row(white id) and column (black id)
        elif match[2] == 0:
            row = int(match[0])
            column = int(match[1])
            
            #Filter out ties.
        if match[2] != 0.5:
            #Adding +1 on all lost matches on rows and columns.
            A[row,column] += 1
            
    #Normalizing each row.
    for i in range(291):
        A[i,:] *= 1/A[i,:].sum()

    return A
A = make_transitionmat(chessdata)


# In[4]:


def power_method(A, iterations, init_vec = None):
    """
    power_method takes the transition matrix, the amount of iterations and a initial vector as arguments,
    if there is no initial vector given the function will assignt a fair initial vector as 1/N on each row.
    The function will return the steady state vector if it converges.
    """
    
    A = A.T
    if init_vec == None:
        init_vec = np.ones_like(A[0])/len(A)
    for i in range(iterations):
        AA = np.linalg.matrix_power(A,i)
        AAA = AA@init_vec
    return AAA


#Making a new pandas dataframe with the steady state vector. Then adding chess player names in first column and the rank given from the power method in the second column
#Then sorting from highest to lowest rank.
df_new = pd.DataFrame(power_method(A, 100))
df_new[0] = name_lst
df_new['Rank'] = power_method(A, 100)
df_new.columns = ['Player','Rank']
df_new1 = np.copy(df_new)
df_new1 = pd.DataFrame(df_new1)
df_new1.columns = ['Player','Rank']
df_new1 = df_new1.sort_values(by=['Rank'],ascending=False)
#Print out top 10
print('Top ten players: ',df_new1.head(n = 10).values)


# In[5]:


def google_mat(alpha, S):
    """
    google_mat takes a tuning scalar with values from 0 to 1 and the stochastic transition matrix as arguments.
    The function will take the google algorithm and return the google transition matrix.
    """
    
    e = np.ones(len(S))
    E = 1/len(S)*np.outer(e,e)
    G = alpha*S + (1-alpha)*E
    return G


def check_stochasticity(A):
    """
    check_stochasticity checks if the matrix is stochastic by summing all rows and checks if this equals one.
    Since this is numeric i have a threshold of 0.1 because some values might be 0.99 etc, 
    but want it to fail if it is too low like 0.8 etc.
    """
    
    column = 1
    testcheck = 0
    threshold = 1e-1
    for row in A:
        threshold_test = abs(1-row.sum())
        if threshold_test > threshold:
            print('Sum of row in column %d does not equal one!'%column)
            testcheck = 1
        
    column += 1
    if testcheck == 0:
        print('Test finished: Matrix is stochastic')

#Checking if the matrix is stochastic before i use it in google alogrithm function.
check_stochasticity(A)

#Make new variable with the google transition matrix with tuning 0.85 and 100 iteration. Then assign new pandas dataframe,
#with the steady state google vector. The dataframe is then given the column names "Players" and rank. The dataframe is then sorted from highest to lowest rank.
df_make_google_matrix = google_mat(0.85, A)
df_new_google = pd.DataFrame(power_method(df_make_google_matrix, 100))
df_new_google[0] = name_lst
df_new_google['Rank'] = power_method(df_make_google_matrix, 100)
df_new_google.columns = ['Player','Rank']
#Changing name of dataframe to avoid using the ordered dataframe in regression model.
df_new_google1 = np.copy(df_new_google)
df_new_google1 = pd.DataFrame(df_new_google1)
df_new_google1.columns = ['Player','Rank']
df_new_google1 = df_new_google1.sort_values(by=['Rank'],ascending=False)
#Print out top 10
print('Top ten players with google matrix: ',df_new_google1.head(n = 10).values)


# In[6]:


#Importing matplotlib module for plotting
import matplotlib.pyplot as plt

#Importing the chess elo data assigning the chess data to a pandas dataframe and renaming columns to Players and Elo rank.
chess_elo = pd.read_csv('data\chess-games-elo.csv', header = None)
df_chess_elo = pd.DataFrame(chess_elo)
df_chess_elo.columns = ['Player', 'Elo']
# Performing np.copy is to avoid changing the original data.
X = np.copy(df_chess_elo)

#Taking logarithm of the data and multiplying with 
Rank_temp = np.log(np.copy(df_new_google['Rank'])*10**4)

def linearfit_estimate(X):
    """
    linearfit_estimate takes the matrix with players and elo as argument, the function then sorts the matrix for
    vectorized regression model, it will then return the whole regression model y as a array.
    Here we assume gaussian distributed error so that we can minimize the error and use the following multiplications."""
    
    player_temp = np.copy(df_chess_elo['Player'])
    #Assigning the r vector with the steady vector of the google transition matrix and the regular one.
    r = np.copy(df_chess_elo['Elo'])
    ones = np.ones_like(r)
    #Rearranging the matrix to have ones in first column and elo ranks i second (using the logarithm of the data in the regression line).
    A = np.array((ones,Rank_temp)).T
    
    w = (np.linalg.inv(A.T@A))@A.T@r
#     Returning the linear regression model
    
    return w



# Performing the linear regression on the chess elo data.
# The regression model is plotted with the logarithmic paramater, then the google steady state values are plotted with the regression model on a logarithmic y-scale.
reg_coeffs = linearfit_estimate(X)
regline_goog = reg_coeffs[1]*Rank_temp + reg_coeffs[0]
plt.figure(figsize = (15,5))
plt.plot(Rank_temp,regline_goog, label = r'$\hat{y}_{i} = \hat{\beta}_{1}\lnx^{t} + \hat{\beta}_{0} $', color = 'red')
plt.plot(Rank_temp,df_chess_elo['Elo'],'^', label = 'ln(Pagerank),Elo', color = 'blue')
plt.legend(loc = 'best', prop={'size': 20})
# plt.xscale('log')
plt.title('Rank/Elo Plot',fontsize=18)
plt.ylabel('Elo',fontsize=18)
plt.xlabel('Ranking',fontsize=18)
# axes = plt.gca()
# axes.set_ylim([0.0003,1])
plt.show()


# In[7]:


def residual(regline):
    """
    residual function takes in the steady state vector and the regression model as arguments
    the function then finds the residual by find the difference between the model and the data.
    Then it find the residual sum of squares and the total sum of squares and then finding the R^2.
    
    #https://en.wikipedia.org/wiki/Residual_sum_of_squares
    #https://en.wikipedia.org/wiki/Coefficient_of_determination
    """
    
    r = np.copy(df_chess_elo['Elo'])
    resid = []
    for i,j in zip(r,regline):
        resid.append(j-i)
    resid = np.array(resid)
    SSres = sum(resid**2)
    SStot = sum((r - np.mean(r))**2)
    #Relative square error used to find the R^2
    E_RSE = SSres/SStot
    R_Sqr = 1 - E_RSE
    
    return R_Sqr


#print out the coefficient of determination R^2 and the estimators of the regression model for the google vector
print('R^2 Google',residual(regline_goog))
print('Beta_0_hat = ',reg_coeffs[0])
print('Beta_1_hat = ',reg_coeffs[1])

