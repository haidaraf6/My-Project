import numpy as np
import matplotlib.pyplot as plt

rs=np.linspace(-1,4,1000)
N=500
r=0.5
x=.5+np.zeros(N)
endcap=np.arange(round(N*.9),N)
for ri in range(len(rs)):
    for n in range(N-1):
        x[n+1]=rs[ri]*np.sin(np.pi*x[n])
    u=np.unique(x[endcap])
    r=rs[ri]*np.ones(len(u))
    plt.plot(r,u,'k.',markersize=1)
plt.show()







