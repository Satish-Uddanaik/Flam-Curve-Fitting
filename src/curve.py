import numpy as np

import numpy as np

def generate_curve(theta, M, X, t):
    """
    Generate x and y coordinates from the parametric equation.

    Parameters
    ----------
    theta : float
        Angle in radians.
    M : float
        Exponential parameter.
    X : float
        Horizontal shift.
    t : numpy array
        Parameter values.

    Returns
    -------
    x, y : numpy arrays
    """

    x = (
        t * np.cos(theta)
        - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta)
        + X
    )

    y = (
        42
        + t * np.sin(theta)
        + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    )

    return x, y