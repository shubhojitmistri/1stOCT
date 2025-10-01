import matplotlib.pyplot as plt
import numpy as np
# change the size of the graph
fig = plt.figure(figsize=(10,10))

#3d axes
ax = plt.axes(projection='3d')

#shape of the voxel grid
axes = (5,5,5)

#create voxel data(True means a cube exist there)
data = np.ones(axes, dtype= bool)

#transperency
alpha = 0.9

#create a colour array with the same shape as data + RGBA channels
colours =np.zeros(axes + (4,))

#assign colours layer by layer
colors[0,:, :] = [1, 0, 0 , alpha] # red
colors[1,:, :] = [0, 1, 0 , alpha] # green
colors[2,:, :] = [0, 0, 1 , alpha] # blue
colors[3,:, :] = [1, 1, 0 , alpha] # yellow
colors[4,:, :] = [1, 1, 1, alpha] # white

#hide axes
ax.set_axis_off()

#draw voxels
ax.voxels(data, facecolors=colors, )