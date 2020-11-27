
import numpy as np
import matplotlib.pyplot as plt
import cmath
from data import nodes, links, location

area_min = 400
area_max = 1100
width_two = 'greenyellow'
width_four = 'red'
width_six = 'purple'
width_eight = 'b'

def nodes_link(x,y,wid):
    widcolor = 'black'
    wid = int(wid)
    if wid == 2:
        widcolor = width_two
    elif wid == 4:
        widcolor = width_four
    elif wid == 6:
        widcolor = width_six
    elif wid == 8:
        widcolor = width_eight
    plt.plot(x,y, color = widcolor)

def pltmap():
    for i in location:
        plt.scatter(i[1],i[2], s=200, color=(1,0,1-(i[3]-area_min)/(area_max - area_min)))

    plt.scatter(np.array(nodes)[:,1],np.array(nodes)[:,2], color='gray', label = 'nodes')

    for i in links:
        nodes_link([nodes[int(i[0])-1][1],nodes[int(i[1])-1][1]], \
                    [nodes[int(i[0])-1][2],nodes[int(i[1])-1][2]], i[2])

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend() 
    plt.show()


if __name__ == "__main__": 
    pltmap()
    print(np.array(nodes)[:,1])