import numpy as np
import math


class Quaternion:
    def __init__(self, q):
        self.q = q
        self.q_M = self.skew(q)
        self.q_conj = self.conjugate()
        self.q_norm = self.norm()
        self.q_inv = self.q_conj / self.q_norm
        self.q_Euler = self.q2Euler()

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

    def q2Euler(self, deg=True):
        """
        Method that converts the quaternion into an Euler (Aerospace sequence)
        :param deg: boolean, if True, the Euler sequence is in degrees (by default)
        :return: np.array: [phi, theta, psi]
        """

        m11 = 2 * self.q[0]**2 + 2 * self.q[1]**2 - 1
        m12 = 2 * self.q[1] * self.q[2] + 2 * self.q[0] * self.q[3]
        m13 = 2 * self.q[1] * self.q[3] - 2 * self.q[0] * self.q[2]
        m23 = 2 * self.q[2] * self.q[3] + 2 * self.q[0] * self.q[1]
        m33 = 2 * self.q[0]**2 + 2 * self.q[3]**2 - 1

        psi = math.atan2(m12, m11)
        theta = math.asin(-m13)
        phi = math.atan2(m23, m33)

        q_Euler = np.array([phi, theta, psi])

        if deg:
            q_Euler = np.array([math.degrees(q_e) for q_e in q_Euler])

        return q_Euler


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
