
import numpy as np
import math
from scipy.spatial.transform import Rotation as R
from quaternions_py.quaternion_utils import Quaternion


def quat_mult(q1, q2):
    """
    Multiply two quaternions
    :param q1: quaternion 1, object (instance 1)
    :param q2: quaternion 2, object (instance 2)
    :return: q3: quaternion 3, np.array
    """
    q3 = np.dot(q1, q2)

    return q3

# Quaternion instances
q1 = Quaternion(np.array([0.5, 0.0, 0.0, 0.5]))
q2 = Quaternion(np.array([0.5, 0.5, 0.0, 0.0]))

# Quaternion multiplication
q3 = quat_mult(q1.q_M, q2.q)





# Quaternion to Euler using SciPy
# q4 = Quaternion(np.array([0.701, 0.701, 0.0, 0.0]))
# r = R.from_quat(q4.q)
# print(r.as_euler('zyx', degrees=False))