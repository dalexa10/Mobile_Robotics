import numpy as np


class Quaternion:
    def __init__(self, q):
        self.q = q
        self.q_M = self.skew(q)
        self.q_conj = self.conjugate()
        self.q_norm = self.norm()
        self.q_inv = self.q_conj / self.q_norm

    def conjugate(self):
        """
        Computes the complex conjugate of the quaternion
        :return: q_conj = np.array
        """
        q_conj = np.array([self.q[0], -self.q[1], -self.q[2], -self.q[3]])
        return q_conj

    def norm(self):
        """
        Computes the quaternion norm
        :return: q_norm, float
        """
        q_norm = np.sqrt(self.q[0]**2 + self.q[1]**2 + self.q[2]**2 + self.q[3]**2)
        return q_norm

    @staticmethod
    def skew(q):
        """
        Computes the skew symmetric matrix of a quaternion
        :return: q_M: np.array, skew symmetric matrix of the quaternion
        """
        q_M = np.array([[q[0], -q[1], -q[2], -q[3]],
                        [q[1], q[0], -q[3], q[2]],
                        [q[2], q[3], q[0], -q[1]],
                        [q[3], -q[2], q[1], q[0]]])
        return q_M
