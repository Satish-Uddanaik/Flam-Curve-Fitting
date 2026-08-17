import numpy as np
from scipy.optimize import minimize

import numpy as np
from curve import generate_curve

def loss(params, x_actual, y_actual, t):

    theta, M, X = params

    x_pred, y_pred = generate_curve(theta, M, X, t)

    l1 = np.mean(
        np.abs(x_actual - x_pred)
        +
        np.abs(y_actual - y_pred)
    )

    return l1


def optimize_parameters(x_actual, y_actual):

    t = np.linspace(6, 60, len(x_actual))

    initial_guess = [
        np.deg2rad(25),
        0.0,
        80
    ]

    bounds = [

        (np.deg2rad(0), np.deg2rad(50)),

        (-0.05, 0.05),

        (0,100)

    ]

    result = minimize(

        loss,

        initial_guess,

        args=(x_actual, y_actual, t),

        bounds=bounds,

        method="L-BFGS-B"

    )

    return result