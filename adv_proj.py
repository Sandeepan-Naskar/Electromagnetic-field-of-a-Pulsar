import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style("dark")

tau = 1
n = 3 
w0 = 200
B0 = 10**12

def w(t):
    return w0*((1+t/tau)**(-1/n-1))

def B(t):
    return B0*((1+t/tau)**((3-n)/(2*n-2)))

# Y = w(X)
# Z = B(X)

for i in range(3,7):
    n = i
    X = np.linspace(0, 4, 1000)
    plt.plot(X, w(X), label='n = %d' % n)
plt.legend()
plt.title('Angular velocity vs. time')
plt.xlabel('Time (Tau)')
plt.ylabel('Angular velocity (rad/s)')
plt.grid()
plt.savefig('adv_proj.png')
plt.close()

for i in range(3,7):
    n = i
    X = np.linspace(0, 20, 1000)
    plt.plot(X, B(X), label='n = %d' % n)
plt.legend()
plt.title('Magnetic field vs. time')
plt.xlabel('Time (Tau)')
plt.ylabel('Magnetic field (G)')
plt.grid()
plt.savefig('adv_proj1.png')
plt.close()

#################################
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d


def conv(R, THETA):
    x = R * np.cos(THETA)
    y = R  * np.sin(THETA)
    return x, y

THETA = np.linspace(0, 2 * np.pi, 1000)

R = []
for i in range(2,10):
    A = i*(np.cos(THETA))**2
    R.append(A)

for i in range(10, 20):
    A = i*(np.cos(THETA))**2
    thet = []
    r = []
    for a in range(len(A)):
        x,y = conv(A[a], THETA[a])
        if x>=9 or x<=-9.07:
            continue
        else:
            thet.append(THETA[a])
            r.append(A[a])
    R.append([r, thet])
for i in range(101):
    R.append(i/100)

L = np.linspace(-11, 11, 100)

fig = plt.figure()
ax = fig.add_subplot()

for i in range(-900,900,1):
    ax.plot([i/100]*100, L, 'g-', alpha=0.025)

for r in range(len(R)):
    if r >= 18:
        X, Y = conv(R[r], THETA)
        ax.plot(X, Y, 'b-', alpha=0.12)
        continue
    if r < 8:
        X, Y = conv(R[r], THETA)
        ax.plot(X, Y, 'r--')
        continue
    X, Y = conv(R[r][0], R[r][1])
    ax.plot(X, Y, 'k--')

ax.plot([9]*100, L, 'k-')
ax.plot([-9]*100, L, 'k-')


# for i in range(100):
#     ax.plot([8,8], [L[i], L[i+1]], 'g-')
#     ax.plot([-8,-8], [L[i], L[i+1]], 'g-')
    

ax.set_xlim(-11, 11)
ax.set_ylim(-11, 11)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylabel('Axis of rotation (z-axis)')
ax.set_xlabel('Light Cylinder')
ax.set_aspect('equal')

ax.grid(True)

plt.savefig('adv_proj2.png')
plt.close()