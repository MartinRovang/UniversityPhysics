import numpy as np
import random
import matplotlib.pyplot as plt
import shutil
import os
import pandas as pd

# Hold global variables for error function
reset = 0
error_func_holder = []
error_index = []
def error_func(error):
    """
    Sums up alle the distances for each centroids and stores it in global variable to plot
    at the end of algorithm.
    """
    global error_func_holder
    summed = 0
    for key in error:
        summed += np.sum(error[key])
    error_func_holder.append(summed)







def get_distance(data, centroids, N):
    """
    Find distance between the datapoints to the centroids.
    """

    # find shape
    rows_data, cols_data = data.shape
    temp = np.zeros((rows_data,N))
    # fill temporary matrix with the distances in the N dimensional space of the dataset
    for length, row in enumerate(data):
        for cent, row_cent in enumerate(centroids):
            # [centroid1, centroid2]
            #[length    , length]
            temp[length, cent] = np.linalg.norm(row-row_cent)

    return temp



def get_cents(data, temp, label = [None]):
    """
    Assigns the datapoints which are nearest a centroid and put them in a dictionary
    which belongs a the centroid.
    """
    groups = {}
    error_dist = {}
    label_dic = {}
    for i, row in enumerate(temp):
        #assign centroid to datapoints with lowest distance to a dictionary
        # argmin will give index of the lowest value (index = centroid)
        centroid_index = np.argmin(row)


        #if not exist in centroid dictionary assign new list
        if centroid_index not in groups:
            groups[centroid_index] = []

        if centroid_index not in error_dist:
            error_dist[centroid_index] = []

        #fills up the centroid with the datapoints
        groups[centroid_index].append(data[i,:])

        # If enabled (label != None) then add all the labels to the centroids aswell.
        if label[0] != None:
            if centroid_index not in label_dic:
                label_dic[centroid_index] = []
            label_dic[centroid_index].append(label[i])


        #fills up the error dictionary for the cost function
        error_dist[centroid_index].append(row[centroid_index])

    for key in groups:
        #Make them numpy arrays to be able to use numpy on the datapoints
        groups[key] = np.array(groups[key])
    error_func(error_dist)

    return groups, label_dic



def get_means(data, groups):
    """
    Get the mean of the clusters and assign the centroids this new coordinate in a
    dictionary.
    """
    features = len(data[0])
    groups_mean = {}
    for i in groups:
        for n in range(features):
            if i not in groups_mean:
                groups_mean[i] = []
            groups_mean[i].append(np.mean(groups[i][:,n]))

    return groups_mean


def initate_cents(data, N):
    """
    Make random centroids in the vectorspace of the datapoints
    """
    global reset
    features = len(data[0])
    # map the min and max value of the dataset to contain the centoid spawn into
    centroids = np.zeros((N,features))

    # place centroids in N dimensional space
    for j in range(N):
        for i in range(features):
            # make random coordinate
            rand = np.random.choice(data[random.randint(0,len(data)-1)], replace=False)
            centroids[j,i] = rand
    reset = 0
    return centroids


def remake_cents(data, groups_mean, N):
    """
    Since the distance function uses matrix, we need to fill up a new
    matrix with the new mean coordinates.
    """

    global error_func_holder
    global error_index
    features = len(data[0])
    centroids = np.zeros((N,features))

    try:
        # assign centroids to new matrix for finding distance if not all centroids (N) have atleast one
        # data point assigned to it, this test will fail and go to except to make new random centroids.
        for j in range(N):
            centroids[j,:] = groups_mean[j]

    # If some centroids fails tp find a cluster we make new random centroids
    # this could happen there is one centroid which didnt have a closest datapoint
    except:
        if not os.path.exists('plots'):
            os.makedirs('plots')
        # remove plots added to folder
        shutil.rmtree('plots')
        if not os.path.exists('plots'):
            os.makedirs('plots')

        error_index.append(len(error_func_holder)-1)
        # initiate new random centroids
        return initate_cents(data, N)

    return centroids



def make_plots(savefi, groups, groups_mean, N, savefigure = False):
    """
    If savefigure = True then plot the dataset and centroids with their respective color
    and save the figures.
    """
    plt.figure(figsize = (15,10))
    colors = ['red','blue','green','orange','pink','purple','yellow','black','brown','lightgreen','k', 'w','c','lightblue']
    for i in groups:
        plt.plot(groups[i][:,0],groups[i][:,1], 'o', color = colors[i], markeredgecolor= 'black')


    for i in groups_mean:
        plt.plot(groups_mean[i][0],groups_mean[i][1],'^', color = colors[i], markersize = 20, markeredgecolor= 'black')

    #make new folder if it does not exist (for plots)
    if not os.path.exists('plots'):
        os.makedirs('plots')
    # # Save plots
    # make_plots(savefi, groups, groups_mean, N)
    plt.title('K-means plot', fontsize = 20)
    if savefigure == True:
        plt.savefig('plots/k-means_%d_cents%d'%(savefi,N))
    plt.close()



def k_means(data, N, label = [None], savefigure = False, max_iters = 150):
    """
    This is the main k-means algo, this is the function to run,
    this function "initate_cents", "get_distance", "get_cents", "remake_cents" functions.
    
    returns grousp dictionary, centroid placement dictionary, and labels (labels are empty dictionary if 
    labels are not given)
    """

    #make new folder if it does not exist (for plots)
    if not os.path.exists('plots'):
        os.makedirs('plots')


    # make a loader for to see that the program is working
    loader = ['|','/','-','|','/','-']

    # copy to avoid pointer
    data = np.copy(data)

    rows_data, cols_data = data.shape

    # Make random placed centroids
    centroids = initate_cents(data, N)

    #some variables to change in the whole loop to keep track of loader etc.
    change = 0
    savefi = 0
    load = 0
    global reset

    # Begin iteration
    while True:

        # Find distance from all points
        temp = get_distance(data, centroids, N)

        # Group the data to the centroids
        groups, label_dic = get_cents(data, temp, label)

        if reset >= 2:
            make_plots(savefi, groups, groups_mean, N, savefigure)

        # Get mean coordinates for the centroids
        groups_mean = get_means(data, groups)

        # make matrix with coordinates for distance measure
        centroids = remake_cents(data, groups_mean, N)



        # if converged or reached max iterations return the groups of clusters
        if change == np.sum(temp) or savefi == max_iters:
            global error_index
            global error_func_holder
            # get the values from error function where new centroids where generated
            error_values = [error_func_holder[x] for x in error_index]

            #Plots the error function and the generated centroids
            plt.plot(error_func_holder,'--', label = 'Cost function')
            #plt.plot(error_index, error_values,'*', label = 'Generated new centroids', color = 'red', markersize = 13)
            plt.title('Cost function of k-means', fontsize = 20)
            plt.ylabel('Error', fontsize = 15)
            plt.xlabel('Iteration', fontsize = 15)
            plt.legend(loc = 'best')
            # save errorfunction plot
            plt.savefig('plots/errorfunction.png')
            plt.close()
            # return the centroids with their given dataset and the placement of the centroids
            return groups, groups_mean, label_dic


        # To change name of savefig file
        savefi += 1
        reset += 1
        change = np.sum(temp)

        # The loader
        load += 1
        try:
            print('{0} {0} {0} Generating k-means {0} {0} {0}'.format(loader[load]), end = '\r')
        except:
            load = 0
            print('{0} {0} {0} Generating k-means {0} {0} {0}'.format(loader[load]), end = '\r')






def plot_centroids(groups, title , v, h):
    """
    Plots the images given.
    """
    for i in sorted(groups):

        plt.subplot(5,2,i+1)
        number = groups[i]
        number = np.reshape(number,(v,h))
        plt.imshow(number, cmap = 'Greys_r')
        plt.suptitle(title, fontsize = 20)
    plt.savefig('plots/%s.png'%title)
    plt.close()





def feature_reduction(X):
    """
    Reduced the features of data to two dimensions
    """
    # Get eigenvalues and eigenvector
    val, E = np.linalg.eig(X)
    # Sorting highest to lowest eigenvalues
    idx = val.argsort()[::-1]
    val = val[idx]
    # Taking square root of the diagonal eigenvalue matrix
    Dsqr = np.sqrt(np.diag(val))
    print(Dsqr)
    # Taking the inner product to form data-set Z
    Z = np.dot(E, Dsqr)
    # Return two features
    return Z[:,:2]





def minmax_control(groups, centroid_placement):
    """
    Finds the datapoints closest to the centroids and the ones on the border
    returns two dictionaries, first is datapoint closest to centroids and second dictionary
    is the ones on the border. The plots are saved to folder /plots
    """

    colors = ['red','blue','green','orange','pink','purple','yellow','black','brown','lightgreen','k', 'w','c','lightblue']
    
    distances_to_centroids = {}
    for i in groups:
        for datapoint in groups[i]:
            if i not in distances_to_centroids:
                distances_to_centroids[i] = []
            distances_to_centroids[i].append(np.linalg.norm(datapoint - centroid_placement[i]))

    borders = {}
    closest = {}
    for i in distances_to_centroids:
        if i not in borders:
            borders[i] = []
        max_index = np.argmax(distances_to_centroids[i])
        borders[i].append(groups[i][max_index])

        if i not in closest:
            closest[i] = []
        min_index = np.argmin(distances_to_centroids[i])
        closest[i].append(groups[i][min_index])
                

    
    for i in distances_to_centroids:
        plt.plot(distances_to_centroids[i], '*', markeredgecolor= 'black', markersize = 10 , color = colors[i], label = 'Centroid %d'%i)
    plt.xlabel('Index of datapoint')
    plt.ylabel('Distance from their respective centroid')
    plt.legend(loc = 'best')
    plt.savefig('plots/Distance_Plot')
    plt.close()

    return closest, borders




def border_control(centroid_placement):

    """
    Finds the border cases from each centroid
    """

    # finds all the unit vectors 
    borders = {}
    for i in centroid_placement:
        if i not in borders:
            borders[i] = []
            for l in centroid_placement:
                if i == l:
                    continue
                else:
                    borders[i].append((np.array(centroid_placement[l]) - np.array(centroid_placement[i]))\
                    /(np.linalg.norm(np.array(centroid_placement[l]) - np.array(centroid_placement[i]))))
    # dictionary for which cluster it has the boundary to
    bound_change_cluster = {}
    # dictionary for the position for which the boundary is
    bound_change_position = {}
    for indec in sorted(centroid_placement):
        # lock to start with cluster when we have found the boundary
        lock = 0
        while True:
            if lock != 1:
                # Find the current position on the vector
                try:
                    current_position = centroid_placement[indec] + i*np.array(borders[indec][indec])
                except:
                    current_position = centroid_placement[indec] + i*np.array(borders[indec][0])
                # list to append all the distances to each centroid from the point on the vector
                lst = []
                for j in sorted(centroid_placement):
                    lst.append(np.linalg.norm(current_position - centroid_placement[j]))
                # find which centroid the point belongs too by finding the minimum distance
                # and chech which index(cluster) it belongs to
                index_min = np.argmin(lst)
                i += 0.1
                if indec != index_min:
                    if indec not in bound_change_position:
                        bound_change_position[indec] = []
                        bound_change_cluster[indec] = []
                    bound_change_cluster[indec].append(index_min)
                    bound_change_position[indec].append(current_position)
                    lock = 1
            else:
                break
    
    return bound_change_cluster, bound_change_position



def border_control_all_boundaries(centroid_placement):

    """
    Finds the border cases from each centroid
    """

    # finds all the unit vectors 
    borders = {}
    for i in sorted(centroid_placement):
        if i not in borders:
            borders[i] = []
            for l in sorted(centroid_placement):
                if i == l:
                    continue
                else:
                    borders[i].append((np.array(centroid_placement[l]) - np.array(centroid_placement[i]))\
                    /(np.linalg.norm(np.array(centroid_placement[l]) - np.array(centroid_placement[i]))))
    # dictionary for which cluster it has the boundary to
    bound_change_cluster = {}
    # dictionary for the position for which the boundary is
    bound_change_position = {}
    for indec in sorted(centroid_placement):
        for border_values in borders[indec]:
            # lock to start with cluster when we have found the boundary
            lock = 0
            while True:
                if lock != 1:
                    # Find the current position on the vector
                    current_position = np.array(centroid_placement[indec]) + i*np.array(border_values)
                    # list to append all the distances to each centroid from the point on the vector
                    lst = []
                    for j in sorted(centroid_placement):
                        lst.append(np.linalg.norm(current_position - centroid_placement[j]))
                    # find which centroid the point belongs too by finding the minimum distance
                    # and chech which index(cluster) it belongs to
                    index_min = np.argmin(lst)
                    i += 0.1
                    if indec != index_min:
                        if indec not in bound_change_position:
                            bound_change_position[indec] = []
                            bound_change_cluster[indec] = []
                        # cluster represents which the centroid borders to
                        bound_change_cluster[indec].append(index_min)
                        # position is the border positions
                        bound_change_position[indec].append(current_position)
                        lock = 1
                else:
                    break
    
    return bound_change_cluster, bound_change_position
