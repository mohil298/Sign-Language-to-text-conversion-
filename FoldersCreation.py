# Importing the Libraries Required

import os
import string

# Creating the directory Structure

if not os.path.exists("dataSet2"):
    os.makedirs("dataSet2")

if not os.path.exists("dataSet2/trainingData"):
    os.makedirs("dataSet2/trainingData")

if not os.path.exists("dataSet2/testingData"):
    os.makedirs("dataSet2/testingData")

# Making folder  0 (i.e blank) in the training and testing data folders respectively
for i in range(0):
    if not os.path.exists("dataSet2/trainingData/" + str(i)):
        os.makedirs("dataSet2/trainingData/" + str(i))

    if not os.path.exists("dataSet2/testingData/" + str(i)):
        os.makedirs("dataSe2t/testingData/" + str(i))

# Making Folders from A to Z in the training and testing data folders respectively

for i in string.ascii_uppercase:
    if not os.path.exists("dataSet2/trainingData/" + i):
        os.makedirs("dataSet2/trainingData/" + i)
    
    if not os.path.exists("dataSet2/testingData/" + i):
        os.makedirs("dataSet2/testingData/" + i)

