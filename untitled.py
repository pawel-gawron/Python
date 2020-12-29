import numpy as np
import matplotlib.pyplot as plt
"""
ks = np.arange(0,360,10)

k = np.linspace(0,2*np.pi,100)
y = np.sin(k)
plt.plot(k,y,'r')
y2 = np.cos(k)
plt.plot(k,y2,'g')
plt.grid()
plt.title('Sinus i cosinus')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.show()

fl = [3.123456, 1.254664, 54.2354346]

with open('tablica.txt','w') as f:
    f.write(f'test {fl[1]:0.2f}')
"""

kat = np.arange(0,360,10)
k = np.deg2rad(kat)

s = np.sin(k)
c = np.cos(k)

plt.plot(kat,s,'r')
plt.plot(kat,c,'g')
plt.show()

with open('wykres.txt','w') as f:
    for i in kat:
        f.write(f'{i:0.0f} & {np.sin(i):0.3f} & {np.cos(i):0.4f}  \\\\ \\hline \n')
