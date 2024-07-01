import numpy as np

def estimate_simple_linear_reg_coef(x: list[float], y: list[float]) -> tuple[float, float]:
  """
  Estimates the coefficients using a simple linear
  regression model (y ~ b_0 + b_1 * x).

  Borrowed from https://www.geeksforgeeks.org/linear-regression-python-implementation/

  Parameters
  ----------
  x : list[float]
    A list of observations for a given feature or condition.
  y : list[float]
    A list of observations for the outcome.
  
  Returns
  -------
  tuple[float, float]
    The coefficients of the intercept and the feature.
  """

  # Number of observations/points
  n = np.size(x)

  # Mean of x and y vector
  m_x = np.mean(x)
  m_y = np.mean(y)

  # Cross-deviation and deviation about x
  ss_xy = np.sum(y*x) - n*m_y*m_x
  ss_xx = np.sum(x*x) - n*m_x*m_x

  # Regression coefficients
  b_1 = ss_xy / ss_xx
  b_0 = m_y - b_1*m_x

  return (b_0, b_1)
