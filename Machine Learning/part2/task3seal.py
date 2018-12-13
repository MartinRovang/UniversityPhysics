import numpy as np
import machinepy as ml

# Set up classifier
y = ml.predictor(training = training_data, decision= 0.5)
# Train with given learning rate and 600 iterations
y.train(3.18e-5,it = 600)
# Initialize array
lst = []
# How many picture to look at
N = 100
# Iterate through a given amount of picture
for i in range(0,N+1):
    test = np.copy(test_data)[i,:]
    # Hold which class it actually is
    classif = test[0]
    # Set it ready to be classified
    test[0] = 1
    # Append array with index of wrongly classified image
    if y.predict(test) != classif:
        lst.append(i)
print(lst)



images = np.genfromtxt("seals_images_test.csv")
# Get images of seals
for i in [22,29,31,35,50,53,65,74,88,93]:
    print(i)
    ml.get_seal_img(images,i)


ml.get_seal_img(images,6)
