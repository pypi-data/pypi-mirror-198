import numpy as np
from getAttribute import getAttribute

def parameterAnalysis(p):
    parameterAttribute, parameter = getAttribute(p)
    parameterAttribute = np.array(parameterAttribute)
    parameter = np.array(parameter)

    parameter_max = np.zeros(np.size(parameter))
    parameter_min = np.zeros(np.size(parameter))

    # Adjust small values
    for i in range(np.size(parameter)):
        if abs(parameter[i]) < 0.1:
            parameter_max[i] = 100
            parameter_min[i] = -100
        elif parameter[i] >= 0:
            parameter_max[i] = parameter[i] * 100
            parameter_min[i] = parameter[i] * -100
        else:
            parameter_min[i] = parameter[i] * 100
            parameter_max[i] = parameter[i] * -100
    bound = np.empty((np.size(parameter), 2))
    bound[:, 0] = parameter_min
    bound[:, 1] = parameter_max
    attributeList = parameterAttribute.tolist()
    
    return attributeList, parameterAttribute, parameter, bound