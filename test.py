import numpy as np
import matplotlib.pyplot as plt
from data import nodes, links, location

def nodes_link(x,y,wid):
    plt.plot(x,y,color = 'olive')

if __name__ == "__main__":
    nodes_link([111.634267, 111.649789],[40.779697, 40.830156],1)
    plt.show()