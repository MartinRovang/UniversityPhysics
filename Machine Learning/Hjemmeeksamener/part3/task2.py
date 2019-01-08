
import machinepy as ml
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



data = np.genfromtxt('frey-faces.csv')
#data = np.genfromtxt('flame.csv')[:,1:]

N = 10


groups, centroid_placement, labels = ml.k_means(data, N, savefigure = False, max_iters = 5000)
            
closest, furthest = ml.minmax_control(groups, centroid_placement)

bound_change_cluster, bound_change_position = ml.border_control(centroid_placement)
#bound_change_cluster1, bound_change_position1 = ml.border_control(centroid_placement, 1)




# (A) This will find all the border cases
#bound_change_cluster, bound_change_position = ml.border_control_all_boundaries(centroid_placement)

# prints out the border of which centroids border to Key is centroid which
# we iterate from, the values are the centroids we go over to, index of the
# list tells which index corresonds to what data-point in the bound_change_position
# array it is.
print(bound_change_cluster)

ml.plot_centroids(centroid_placement,'Faces from centroids', 28, 20)
ml.plot_centroids(closest,'Faces closest to centroid', 28, 20)
ml.plot_centroids(furthest,'Faces furthest away', 28, 20)
ml.plot_centroids(bound_change_position,'Faces at boundary', 28, 20)


