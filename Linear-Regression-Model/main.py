import sys
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')

sys.path.append("..")
# from src.preprocessing.constants import BASE_PATH

# read data
data = pd.read_csv("D:/programming/Python/LA_Final_Project/data.csv", header=None)

# shuffle data
data.sample(1)

# split to train and test set
training_size = int(0.95 * len(data))
training_data = data.iloc[:training_size, :]
test_data = data.iloc[training_size:, :]

# converting 1d array to 2d array
x = np.vstack([training_data[0], np.ones(len(training_data[0]))]).T

# Linear Regression
m, c = np.linalg.lstsq(x, training_data[1])[0]

for r in test_data.iterrows():
    print("Read Value: {}\nEstimated value: {}\nError: {}\n"
          .format(r[1][1], m * r[1][0] + c, r[1][1] - (m * r[1][0] + c)))
# plot train data, test data and fitted line
_ = plt.plot(training_data[0], training_data[1], 'o', label='Original training_data', markersize=10)
_ = plt.plot(test_data[0], test_data[1], 'o', label='Original test_data', markersize=10)
_ = plt.plot(training_data[0], m * training_data[0] + c, 'r', label='Fitted line')
_ = plt.legend()
plt.show()
