import numpy as np
import pandas as pd
import testing
import math
from stateBoundary import stateBoundary
from smt.sampling_methods import FullFactorial

def stateCombination(noStateCombination):
    # getting boundaries of states
    x = testing.cornering_left()
    x_bound, x_name = stateBoundary(x)

    noState = len(x_bound[:, 0])
    # sampling system states
    #<6
    if noState < 20:
        noStateVariant = math.floor(noStateCombination ** (1/noState))
        noStateCombination = noStateVariant ** noState
        sampling = FullFactorial(xlimits=x_bound)
        xMatrix = sampling(noStateCombination)
    else:
        xMatrix = np.empty((noStateCombination, noState))
        for i, _ in enumerate(xMatrix[0, :]): xMatrix[:, i] = np.random.uniform(low=x_bound[i, 0],
                                                                                high=x_bound[i, 0],
                                                                                size=(noStateCombination,))
        
    stateCombinationName = []
    for i_stateCombination, _ in enumerate(x_bound[:, 0]):
        stateCombinationName.append("stateCombination_{}".format(i_stateCombination))
    stateCombinationData = pd.DataFrame(xMatrix, columns = stateCombinationName)
    return stateCombinationData, xMatrix, x_bound

def singleStateVariation(maxStateCombination, xMatrix, x_bound, noVariation):
    noState = len(x_bound[:, 0])
    singleStateVariationList = []
    singleStateVariationData = []
    for i_state, val_state in enumerate(x_bound):
        singleStateVariationMatrix = np.empty((noVariation+1, noState))
        singleStateVariationInformation = np.empty((noVariation+1,))
        for i_variant in range(noVariation):
            row = np.zeros(noState)
            fixedState = [state for state in range(maxStateCombination.shape[0]) if state != i_state]
            row[fixedState] = xMatrix[maxStateCombination, fixedState]
            row[i_state] = val_state[0] + (i_variant/noVariation) * (val_state[1] - val_state[0])
            np.append(singleStateVariationMatrix, row, axis=None)
            np.append(singleStateVariationInformation, row[i_state])
        row[fixedState] = xMatrix[maxStateCombination, fixedState]
        row[i_state] = val_state[1]
        np.append(singleStateVariationMatrix, row, axis=None)
        np.append(singleStateVariationInformation, row[i_state])
        singleStateVariationList.append(singleStateVariationMatrix)
        singleStateVariationData.append(singleStateVariationInformation)
    return singleStateVariationList, singleStateVariationData
