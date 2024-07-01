import numpy as np

def get_values(x, y):
  n = np.size(x)
  m_x = np.mean(x)
  m_y = np.mean(y)
  ss_xy = np.sum(y*x) - n*m_y*m_x
  ss_xx = np.sum(x*x) - n*m_x*m_x
  b_1 = ss_xy / ss_xx
  b_0 = m_y - b_1*m_x

  return (b_0, b_1)
