#!/usr/bin/python3
"""
Defines a function that multiply a matrix using NumPy.
"""


import numpy as np

def matrix_multiplication(m_a, m_b):
    """
    Return the product of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
        
    Returns:
        numpy.ndarray: The resulting matrix.
    """
    
    return np.matmul(m_a, m_b)
