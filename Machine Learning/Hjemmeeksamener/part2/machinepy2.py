


import numpy as np
import matplotlib.pyplot as plt
####################################################################
#
#
# SOFT decision tree
#
#
####################################################################


def entropy(data):

    """Finds the entropy from the data by using equation 9.4 in the book,
     Introduction to machine learning, Alpaydin, Ethem"""

    A, B  = 0, 0
    # Check if data is either class 0 or class 1
    for i in data:
        if i[0] == 1:
            A += 1
        else:
            B += 1

    length = A+B
    tot = A
    # Avoid division by zero
    try:
        p =  tot/length
    except:
        p = 0
    # Finds the impurity of the data (how much the data is mixed with different classes.)
    # if 0log0 then 0
    if p == 0:
        entropy = 0
    else:
        entropy = -p*np.log2(p + 1e-20) - (1 - p)*np.log2(1 - p + 1e-20)
    return entropy




def count_classes(data):
    """Find the amount of each class and return a dictionary with the labels and amount"""
    amount = {0:0,1:0}
    for row in data:
        label = int(row[0])
        amount[label] += 1

    return amount



def inf_gain(left,right, parent_entropy):
    # https://en.wikipedia.org/wiki/Decision_tree_learning

    # Get the weight if the child nodes
    p = float(len(left)) / (len(left) + len(right))

    # Return the information gained by this split.
    return parent_entropy - p*entropy(left) - (1 - p) *entropy(right)




class threshold:
    """Makes a threshold object to hold the features and the threshold in the nodes"""
    def __init__(self, feature, thresh):
        # holds features and threshold before seperating into branches
        self.feature = feature
        self.thresh = thresh

    def check(self, data):
        # gets value of feature
        value = data[self.feature]

        # Returns the boolean logic True/False if threshold is met or not
        return value >= self.thresh



    # Return a string representation of the threshold
    def __repr__(self):
        return str(self.thresh)






class leaf:
    """Leaf node, this is where a node becomes classified with the majority class."""
    def __init__(self,data):
        self.amount = count_classes(data)
        # probability classes
        self.pc0 = self.amount[0]/(self.amount[1] + self.amount[0])
        self.pc1 = self.amount[1]/(self.amount[1] + self.amount[0])

        if self.amount[0] >= self.amount[1]:
            self.classified = 'Class 0'
        else:
            self.classified = 'Class 1'




class node:
    """A node in the tree"""
    def __init__(self, thresh, index, left, right):
        self.thresh = thresh
        self.left = left
        self.right = right
        self.index = index






def split(dataset, threshold):
    """ Splits the data """
    left, right = [], []
    for row in dataset:
        # Uses the threshold.check method to test if feature meets the threshold condition
        if threshold.check(row):
            left.append(row)
        else:
            right.append(row)

    # Return left and right branch data
    return left, right




def find_best_split(data):
    """
    Finds the best split given that the split yields the best information about the data
    """
    best_ent, bestf, ind, current_entropy = 0, 0, 1, entropy(data)
    for index in range(1, len(data[0])):
        for row in data:
            condition = row[index]
            thresh = threshold(index, condition)

            # Splitting dataset
            left, right = split(data, thresh)

            # Find the information gain
            e = inf_gain(left, right, current_entropy)


            # If maximum gain choose bestfeature,(index) and update bestentropy to the best information gain
            if e > best_ent:
                best_ent, bestf, ind = e, thresh, index

    # Return the information gain, the bestfeature threshold and the feature index
    return best_ent , bestf, ind



class softTree:
    """
    The decision tree, the tree includes the methods build_tree for building the tree with the training data,
    and a node_stats method to get the whole tree structure, and a prediction method which uses the tree built with
    the training data to find the classes from the data.
    The tree object
    """
    def __init__(self):
        self.class0pos = 0
        self.class0neg = 0
        self.class1pos = 0
        self.class1neg = 0
        self.leafnumber = 0
        self.nodenumber = [1]


    def fit(self, data, N, depth = 0):

        """
        Building the tree, here we have a depth variable that chooses how deep our tree will go,
        We are here building the tree using recursion (we call the build function within the function).
        """


        # Max depth of the tree
        if depth == N+1:
            # If we have reached our max depth we stop building and we make leaf
            # No matter what the information gain is
            L = leaf(data)
            # set the number of leafes
            self.leafnumber += 1
            return L


        # Loading tree print, a way to visualize that the process is ongoing
        print('Building Tree: {:.0f}% '.format((max(self.nodenumber)/N)*100))

        # Get the best information gain, threshold of the node and the feature index
        inf_gain, thresh, index = find_best_split(data)

        # If we have less then 0.05 information gain, we make it a leaf
        if inf_gain <= 0.12:
            # Get the number of leaves
            self.leafnumber += 1
            # Make leaf object
            L = leaf(data)
            return L


        # Split the data set into two branches
        left, right = split(data, thresh)

        # Recoursion, here we the branches left will keep building until all we have all the leaves,
        # then it goes up to last node and builds the right branch, then it build all the left until leaves,
        # and so on.
        left = self.fit(left, N,depth + 1)
        right = self.fit(right, N, depth + 1)
        # Add depth, where max value of array will yield depth
        self.nodenumber.append(depth)

        # Returns the node at each threshold point in the tree
        N = node(thresh, index, left, right)
        return N


    def node_stats(self, node):

        """
        Print out the whole tree structure
        """

        # If node object is leaf, then write the dictionary of the data inside leaf and the classification
        if isinstance(node, leaf):
            print('Leaf: {}'.format(node.amount))
            print('{}'.format(node.classified))
            # {0:2,1:3}
            # Create stats for confusion matrix
            for label in node.amount:
                if label == 0:
                    if node.classified == 'Class 0':
                        self.class0pos += node.amount[label]
                    else:
                        self.class1neg += node.amount[label]
                else:
                    if node.classified == 'Class 1':
                        self.class1pos += node.amount[label]
                    else:
                        self.class0neg += node.amount[label]
            return


        # Print the feature and its threshold for the node
        print('X{} <= {}'.format(node.index, node.thresh))

        # Print if left branch
        print('--------------')
        print('Left branch')
        self.node_stats(node.left)
        print('--------------')


        # Print if right branch
        print('--------------')
        print('Right branch')
        self.node_stats(node.right)
        print('--------------')


    def predict(self, row, tree, threshold_value):
        """
        This function predicts using the pre-made tree, sends each row from the dataset into the tree and find
        which leaf it falls into and classify the the data with the class assignet to the leaf by the training data.
        """

        # If we have a leaf print return the leaf data from the training and the classification
        if isinstance(tree, leaf):
            ss0 = tree.pc0
            if ss0 >= threshold_value:
                return 'Class 0'
            else:
                return 'Class 1'

        # Here we use the threshold found for the nodes in the training and use this on the row data
        # coming into the prediction function.
        if tree.thresh.check(row):
            return self.predict(row, tree.left, threshold_value)
        # if the row data do not meet the threshold we send it to the right branch to test it in a new node
        # with a new threshold
        else:
            return self.predict(row, tree.right, threshold_value)
