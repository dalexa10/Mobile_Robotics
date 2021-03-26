import numpy as np
import math
from .quaternion_utils import Quaternion


def euler2quat(euler_seq, deg=True):
    """
    Convert an euler sequence (Aerospace sequence), i.e, psi, theta, phi angles
    into a quaterion representation
    :param euler_seq: np.array, [psi, theta, phi]
    :param deg: boolean, indicates if angles are given in degrees (default value)
    :return: Quaternion instance, q
    """
    if deg:
        phi = math.radians(euler_seq[0])
        theta = math.radians(euler_seq[1])
        psi = math.radians(euler_seq[2])
    else:
        phi = euler_seq[0]
        theta = euler_seq[1]
        psi = euler_seq[2]

    q0 = np.cos(psi/2) * np.cos(theta/2) * np.cos(phi/2) + np.sin(psi/2) * np.sin(theta/2) * np.sin(phi/2)
    q1 = np.cos(psi/2) * np.cos(theta/2) * np.sin(phi/2) - np.sin(psi/2) * np.sin(theta/2) * np.cos(phi/2)
    q2 = np.cos(psi/2) * np.sin(theta/2) * np.cos(phi/2) + np.sin(psi/2) * np.cos(theta/2) * np.sin(phi/2)
    q3 = np.sin(psi/2) * np.cos(theta/2) * np.cos(phi/2) - np.cos(psi/2) * np.sin(theta/2) * np.sin(phi/2)

    q = Quaternion([q0, q1, q2, q3])

    return q


def quat_mult(q1, q2):
    """
    Multiply two quaternions
    :param q1: quaternion 1, object (instance 1)
    :param q2: quaternion 2, object (instance 2)
    :return: q3: quaternion 3, np.array
    """
    q3 = np.dot(q1, q2)

    return q3