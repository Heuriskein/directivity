from numpy import arange, pi, transpose, divide, sin, log10
from scipy.special import jv as besselj
import matplotlib.pyplot as plt
import sys

if '--test' in sys.argv:
    dia=33.0	     # diameter of piston in mm
    f=5000.0      # frequency of interest in Hz
else:
    dia = float(input('Diameter of driver in mm : '))
    f = float(input('Frequency of interested in Hz : '))
#
c = 345.0
rho_a = 1.2;
phi = arange(-1*pi/2.0, pi/2.0 + pi/1800.0, pi/1800.0)
phi = phi[1:1800] # Is this a bug? it's shifted to the right, past the end of the array.
#
a = dia/1000.0
theta = arange(pi/1800.0, pi, pi/1800.0)	
k = (2 * pi * f) / c;
#
dir = 2 * divide(besselj(k * a, sin(theta)), (k * a * sin(theta)))
#
p = divide(dir, max(dir))
q = 20.0 * log10(p)
#
#p_s=[phi' p'];
q_s = (transpose(phi), transpose(q))
#
#Dirplot(q_s(:,1)*180/pi,q_s(:,2),'r-',[0 -30 5]);
ax = plt.subplot('111', projection='polar')
ax.plot(q_s[0], q_s[1], 'r-')
ax.set_rticks(range(-30, 1, 6))
ax.set_theta_offset(pi/2.0)
ax.set_thetalim(thetamin=90, thetamax=-90)
ax.set_theta_direction(-1)
ax.set_thetagrids(range(-90, 90, 10),
	labels=["-90", "", "", "-60", "", "", -30, "", "", 0, "", "", 30, "", "", 60, "", "", 90])
ax.set_rmax(0)
ax.set_rmin(-30)
ax.grid(True)
#
#END of File

plt.show()