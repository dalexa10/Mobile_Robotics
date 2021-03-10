
import numpy as np
from quaternions_pkg.quaternion_utils import Quaternion

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
q1 = Quaternion(np.array([1, 2, 3, 4]))
q2 = Quaternion(np.array([2, 3, 2, 4]))

# Quaternion multiplication
q3 = quat_mult(q1.q_M, q2.q)