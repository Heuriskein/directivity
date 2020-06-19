from numpy import arange, pi, transpose, divide, sin, log10, matrix
from scipy.special import jv as besselj
from matplotlib.pyplot import polar, show

#dia = int(input('Diameter of driver in mm : '))
dia=20;     # diameter of piston in mm
#f = int(input('Frequency of interested in Hz : '))
f=1000;      # frequency of interest in Hz
#
c = 345
rho_a = 1.2;
phi = arange(-1*pi/2, pi/2 + pi/1800,pi/1800)
phi = phi[2:1801] # Is this a bug? it's shifted to the right, past the end of the array.
#
a = dia/1000
theta = arange(pi/1800, pi, pi/1800)
k = (2 * pi * f) / c;
#
dir = divide(2 * besselj(k * a, sin(theta)), (k * a * sin(theta)))
#
p = divide(dir, max(dir))
q = 20 * log10(p)
#
#p_s=[phi' p'];
q_s = (transpose(phi), transpose(q))
#
#Dirplot(q_s(:,1)*180/pi,q_s(:,2),'r-',[0 -30 5]);
polar(q_s[0], q_s[1], 'r-')
#
#END of File

show()