import numpy as np

def lazy_matrix_mul(m_a, m_b):
    a = np.array(m_a)
    b = np.array(m_b)

    return np.matmul(a,b)
