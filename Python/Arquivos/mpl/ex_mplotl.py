import matplotlib.pyplot as plt

import numpy as np

x = np.arange(0,100)
y = x*2
z = x**2

# --- 1 ---
#fig = plt.figure()
#ax = fig.add_axes([0, 0, 1, 1])

#ax.plot(x, y)
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_title('Titulo')

#plt.show()

# --- 2 ---
#fig = plt.figure()
#ax1 = fig.add_axes([0, 0, 1, 1])
#ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])

#ax1.plot(x,y)
#ax2.plot(x,y)

#plt.show()

# --- 3 ---
#fig = plt.figure()
#ax1 =fig.add_axes([0, 0, 1, 1])
#ax2 =fig.add_axes([0.2, 0.5, 0.4, 0.4])

#ax1.plot(x, z)
#ax1.set_xlabel('x')
#ax1.set_ylabel('z')

#ax2.plot(x, y)
#ax2.set_xlabel('x')
#ax2.set_ylabel('y')
#ax2.set_title('zoom')

#ax2.set_ylim(30, 50)
#ax2.set_xlim(20, 22)

#plt.show()

# --- 4 ---
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 2))

axes[0].plot(x, y, 'b--', lw = 3) # ou axes[0].plot (x, y, color='blue', ls = '--', lw=3)
axes[1].plot(x, z, 'r', lw = 3)


plt.show()


























