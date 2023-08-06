# -*- coding: utf-8 -*-
import math
import numpy as np
from SALib.sample import morris as ms
from SALib.analyze import morris as ma
from smt.sampling_methods import FullFactorial

import pandas as pd


from vehiclemodels.parameters_vehicle2 import parameters_vehicle2
from vehiclemodels.init_mb import init_mb
from analysis import analysis
from stateBoundary import stateBoundary
from getAttribute import getAttribute
from resultPlot import resultPlot
from cluster import cluster
from parameterAnalysis import parameterAnalysis
from stateCombination import stateCombination
from stateCombination import singleStateVariation
import testing

"""
Created on Thu Sep 29 13:34:20 2022

@author: Youssef Ibrahim
"""

# load parameters
p = parameters_vehicle2()

delta0 = 0
vel0 = 15
Psi0 = 0
dotPsi0 = 0
beta0 = 0
sy0 = 0
initialState = [
    0,
    sy0,
    delta0,
    vel0,
    Psi0,
    dotPsi0,
    beta0,
]
## initial state for simulation
# x0_ST = init_st(initialState)  # initial state for single-track model
x0_MB = init_mb(initialState, p)  # initial state for multi-body model

# Sensitivity analysis
## SA parameters
noTrajectory = 10  # Number of trajectories to generate
noLevel = 4  # Number of levels
confidenceLevel = 0.95  # Confidence interval level

attributeList, parameterAttribute, parameter, bound = parameterAnalysis(p)

## Analysis
problem = {"num_vars": np.size(parameter), "names": attributeList, "bounds": bound}

parameterMatrix = ms.sample(problem, noTrajectory, num_levels=noLevel)

noStateCombination = 512
stateCombinationData, xMatrix, x_bound = stateCombination(noStateCombination)

# Create a matrix for the attribute assignment
attributeAssign = np.empty((len(parameterAttribute), 1))
for i_attr_assign in range(len(parameterAttribute)):
    attributeAssign[i_attr_assign] = i_attr_assign

stateDatabase, simulation = analysis(problem, x_bound, xMatrix, parameterMatrix, parameterAttribute, attributeList)

# Getting situation names for the plot
situation = []
for attr in simulation.Situation.__dict__:
    if callable(getattr(simulation.Situation, attr)):
        situation.append(attr)
print(stateDatabase)
#print(stateDatabase['StateCombination'])
clusterDatabase, centroidDatabase, maxStateCombination = cluster(stateDatabase, stateCombinationData, xMatrix)

noVariation = 3
singleStateVartiationList, variationData = singleStateVariation(maxStateCombination, xMatrix, x_bound, noVariation)
variationList = []
for val_state in singleStateVartiationList:
    variationDatabase = analysis(problem, x_bound, singleStateVartiationList[i], parameterMatrix, parameterAttribute,
                                attributeList)
    variationList.append(variationDatabase)
resultPlot(clusterDatabase, centroidDatabase, variationList, variationData)
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('C:/Users/youss/Results-20.03.2023.xlsx')
clusterDatabase.to_excel(writer, sheet_name='clusterDatabase')
stateCombinationData.to_excel(writer, sheet_name='stateCombinationData')
centroidDatabase.to_excel(writer, sheet_name='centroidDatabase')
writer.close()