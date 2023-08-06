"""Test the smooth trajectory modules

Functions
---------
test_linear_polynomial()
test_cubic_polynomial()
test_quintic_polynomial()
test_time_scaling()

"""

import unittest
import numpy as np
import numpy.testing as npt
from smooth_trajectory.trajectory import linear_polynomial, cubic_polynomial, quintic_polynomial, \
    time_scaling


class TestSmoothTrajectory(unittest.TestCase):
    """Unit test class for testing the smooth trajectory generation
    
    Methods
    -------
    test_linear_polynomial()
        Test the linear smoothing polynomial
    test_cubic_polynomial
        Test the cubic smoothing polynomial
    test_quintic_polynomial
        Test the quinctic smoothing polynomial
    test_time_scaling()
        Test the time scaling function

    """

    def test_linear_polynomial(self):
        """Test the linear smoothing polynomial
        
        Fit a line between the start and finish times
        
        """

        t_0 = 0.0
        t_1 = 10.0

        npt.assert_array_almost_equal(linear_polynomial(t_0, t_1), np.array([-t_0 / (-t_0 + t_1), 1.0 / (-t_0 + t_1)]))
    
    def test_cubic_polynomial(self):
        """Test the cubic smoothing polynomial
        
        Fit a cubic polynomial between the start and finish times
        
        """

        t_0 = 0.0
        t_1 = 10.0

        npt.assert_array_almost_equal(cubic_polynomial(t_0, t_1),
                                      np.array([(t_0**3 - 3 * t_0**2 * t_1) / (t_0**3 - 3 * t_0**2 * t_1 + 3 * t_0 * t_1**2 - t_1**3),
                                                6 * t_0 * t_1 / (t_0**3 - 3 * t_0**2 * t_1 + 3 * t_0 * t_1**2 - t_1**3),
                                                (-3 * t_0 - 3 * t_1) / (t_0**3 - 3 * t_0**2 * t_1 + 3 * t_0 * t_1**2 - t_1**3),
                                                2 / (t_0**3 - 3 * t_0**2 * t_1 + 3 * t_0 * t_1**2 - t_1**3)]))
    
    def test_quintic_polynomial(self):
        """Test the quintic smoothing polynomial
        
        Fit a quintic polynomial between the start and finish times
        
        """

        t_0 = 0.0
        t_1 = 10.0

        denominator = t_0**5 - 5 * t_0**4 * t_1 + 10 * t_0**3 * t_1**2 - 10 * t_0**2 * t_1**3 + 5 * t_0 * t_1**4 - t_1**5

        npt.assert_array_almost_equal(quintic_polynomial(t_0, t_1),
                                      np.array([t_0**3 * (t_0**2 - 5 * t_0 * t_1 + 10 * t_1**2) / denominator,
                                                -30 * t_0**2 * t_1**2 / denominator,
                                                30 * t_0 * t_1 * (t_0 + t_1) / denominator,
                                                10 * (-t_0**2 - 4 * t_0 * t_1 - t_1**2) / denominator,
                                                15 * (t_0 + t_1) / denominator,
                                                -6 / denominator]))

    def test_time_scaling(self):
        """Test the time scaling function"""

        # Tolerance for testing
        tol = 1e-6

        # Start and finish time
        t_0, t_1 = 0.0, 10.0

        # Polynomial coefficients of the smooting function
        a = cubic_polynomial(t_0, t_1)

        # Time vector
        t = np.linspace(t_0, t_1, 1001)

        # Calculate the time scaling
        s = time_scaling(a, t)
        
        self.assertEqual(s[0], 0.0)
        self.assertTrue(np.abs(s[-1] - 1.0) < tol)