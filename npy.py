import numpy as np

files = ['X_data.npy', 'y_data.npy', 'X_train.npy', 'y_train.npy', 'X_test.npy', 'y_test.npy', 'frames.npy']

for file in files:
    data = np.load(file)
    print(f"{file}: shape = {data.shape}, dtype = {data.dtype}")
