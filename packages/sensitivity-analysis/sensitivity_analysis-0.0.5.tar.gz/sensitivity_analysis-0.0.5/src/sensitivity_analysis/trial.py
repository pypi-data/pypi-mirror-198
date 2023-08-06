import numpy as np
import matplotlib.pyplot as plt

from smt.sampling_methods import FullFactorial

xlimits = np.array([[0.0, 4.0], [0.0, 3.0]])
sampling = FullFactorial(xlimits=xlimits)

num = 9
x = sampling(num)

print(x)