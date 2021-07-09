'''@author: Lamgaraj mohamed
   @MAster :  wisd
   @module: visual analytics  '''
from scipy import misc
import cv2
import numpy as np
import matplotlib.pyplot as plt

M = cv2.imread('E:\\rapports\\lena.png')

salt_value = 30

noise = np.random.randint(salt_value+1, size=(512, 512))

#---------- Pepper ----------#

indexe = np.where(noise == 0)

A = indexe[0]
B = indexe[1]

M[A,B,:] = 0

#---------- Salt ----------#

indexe = np.where(noise == salt_value)

A = indexe[0]
B = indexe[1]

M[A,B,:] = 255

#---------- Plot & Save ----------#

print(M.shape)

my_dpi=100

fig = plt.figure(figsize=(800/my_dpi, 800/my_dpi), dpi=my_dpi)

ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)

plt.imshow(M)
plt.savefig("lena_saltpepper.png", dpi=my_dpi)
plt.show()
