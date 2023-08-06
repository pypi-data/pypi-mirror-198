import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
from Simulation import Simulation
def resultPlot(clusterDatabase, centroidDatabase, variationList, variationData):


    #Getting state combination with max sensitivity

    # Plotting clustered data for each situation/state combination
    plotCluster = go.Figure()
    for C in list(clusterDatabase.Cluster.unique()):
        plt.scatter(clusterDatabase[clusterDatabase.Cluster == C]["StateCombination"] , clusterDatabase["SensitivityIndex"], label = "Cluster_{}".format(C))
    plt.legend()
    plt.show()
    
    for i_variation, val_variation in enumerate(variationList):
        plt.scatter(val_variation["StateCombination"] , val_variation["SensitivityIndex"])
        plt.show
    

    plotCluster.show()
    
    