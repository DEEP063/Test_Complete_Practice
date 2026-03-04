import numpy as np

def test_numpy_matrix():
    matrix = np.array([[1, 2], [3, 4]])

    Log.Message("Matrix:")
    Log.Message(str(matrix))

    Log.Message("Matrix Sum: " + str(np.sum(matrix)))
    Log.Message("Matrix Transpose:")
    Log.Message(str(matrix.T))