import re
import numpy as np
import matplotlib.pyplot as plt


bait = {}
nonbait = {}


def structure(x):
    delimiters = " "
    global bait
    global nonbait
    cla = x[1]
    sentence = x[0].upper()
    reg = '|'.join(map(re.escape, delimiters))
    sentence = re.split(reg, sentence)
    
    for word in sentence:
        if cla == 0:
            if word in nonbait:
                nonbait[word] += 1
            else:
                nonbait[word] = 1
        elif cla == 1:
            if word in bait:
                bait[word] += 1
            else:
                bait[word] = 1
        else:
            print('error in class number')


#Fetching trainingdata and trainging
import csv

with open('training_clickbait.txt','r') as csvfile:
    data = csv.reader(csvfile,delimiter = '\n')
    for clickbait in data:
        clickbait.append(1)
        structure(clickbait)
        
with open('trainingnonclick.txt','r') as csvfile:
    data = csv.reader(csvfile,delimiter = '\n')
    for clickbait in data:
        clickbait.append(0)
        structure(clickbait)
        

#restructure to probabilities
for word in bait:
    if word in nonbait:
        summed = bait[word] + nonbait[word]
        bait[word] = bait[word]/summed
        nonbait[word] = nonbait[word]/summed
    else:
        summed = bait[word]
        bait[word] = bait[word]/summed


def classify(filename):
    classified_notclick_lst = []
    classified_click_lst = []
    titlelst = []
    titlelstclick = []
    with open(filename,'r') as csvfile:
        data = csv.reader(csvfile,delimiter = '\n')
        for title in data:
            global bait
            global nonbait
            delimiters = " "
            init_spam = 0
            init_not_spam = 0
            x_dic = {}
            sentence = title[0].upper()
            reg = '|'.join(map(re.escape, delimiters))
            sentence = re.split(reg, sentence)
            
            
            for word in sentence:
                if word in x_dic:
                    x_dic[word] += 1
                else:
                    x_dic[word] = 1
                    
            
            for word in x_dic:
                if word in bait:
                    init_spam += np.log(bait[word] + 1e-20)**x_dic[word] + (1 - x_dic[word])*np.log(1 - bait[word]+1e-20)
                else:
                    bait[word] = 0
                    init_spam += np.log(bait[word] + 1e-20)**x_dic[word] + (1 - x_dic[word])*np.log(1 - bait[word]+1e-20)
                    
            for word in x_dic:
                if word in nonbait:
                    init_not_spam += np.log(nonbait[word] + 1e-20)**x_dic[word] + (1 - x_dic[word])*np.log(1 - nonbait[word]+1e-20)
                else:
                    nonbait[word] = 0
                    init_not_spam += np.log(nonbait[word] + 1e-20)**x_dic[word] + (1 - x_dic[word])*np.log(1 - nonbait[word]+1e-20)
                    
        #     if (init_spam + np.log(prob_spam)) > (init_not_spam + np.log(prob_not_spam)):
            if (init_spam) > (init_not_spam):
                classified_click_lst.append(abs(init_spam))
                titlelstclick.append(title)
                
            else:
                classified_notclick_lst.append(abs(init_not_spam))
                titlelst.append(title)
    return classified_click_lst, classified_notclick_lst,titlelstclick, titlelst

        
        
class_values = classify('buzzfeed.txt')



plt.plot(class_values[1], 'o', label = 'Not clickbait')
plt.plot(class_values[0], 'o', label = 'Clickbait')
plt.title('Classification of clickbait titles')
plt.legend(loc = 'best')
plt.show()

print(class_values[2])