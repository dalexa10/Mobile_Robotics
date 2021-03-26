import numpy as np
import math
from scipy.spatial.transform import Rotation as R
from quaternions_py.quaternions_py.quaternion_utils import Quaternion
from quaternions_py.quaternions_py.quaternion_functions import *


# Quaternion instances
q1 = Quaternion(np.array([0.5, 0.0, 0.0, 0.5]))
q2 = Quaternion(np.array([0.5, 0.5, 0.0, 0.0]))

# Quaternion multiplication
q3 = quat_mult(q1.q_M, q2.q)

# Transformation from Euler angles to quaternions
Euler_database = [[0, 0, 0],
                  [30, 0, 0],
                  [-30, 0, 0],
                  [0, 60, 0],
                  [0, -60, 0],
                  [0, 0, 80],
                  [0, 0, -80],
                  [30, 20, -54]]  # List of Euler angles [phi, theta, psi] to be converted

Q_databse = [euler2quat(Euler_i, deg=True).q for Euler_i in Euler_database]  # Quaternions list

r_test = R.from_euler('zyx', [30, 20, -54])
print(r_test.as_quat())

# Transformation from quaternions to Euler angles
Q_databse2 = [[1, 0, 0, 0],
              [0.9659, 0, 0, 0.2588],
              [0.9659, 0, 0, -0.2588],
              [0.8660, 0, 0.5, 0],
              [0.8660, 0, -0.5, 0],
              [0.7660, 0.6428, 0, 0],
              [0.7660, -0.6428, 0, 0],
              [0.8272, -0.4713, 0.0337, 0.3033]]  # List of quaternions to be converted


Euler_database2 = [Quaternion(q_i).q_Euler for q_i in Q_databse]  # Euler angles list [phi, theta, psi]


# Quaternion to Euler using SciPy
# q4 = Quaternion(np.array([0.701, 0.701, 0.0, 0.0]))
# r = R.from_quat(q4.q)
# print(r.as_euler('zyx', degrees=False))

