format long e
clear all
clc
%
dia = input('Diameter of driver in mm : ');
%dia=20;     % diameter of piston in mm
f = input('Frequency of interested in Hz : ');
%f=10e3;      % frequency of interest in Hz
%
c=345;
rho_a=1.2;
phi=-1*pi/2:pi/1800:pi/2;
phi=phi(2:1801);
%
a=dia/1000;
theta=pi/1800:pi/1800:pi;
k=(2*pi*f)/c;
%
dir=2*besselj(k*a,sin(theta))./(k*a*sin(theta));
%
p=dir./max(dir);
q=20*log10(p);
%
p_s=[phi' p'];
q_s=[phi' q'];
%
Dirplot(q_s(:,1)*180/pi,q_s(:,2),'r-',[0 -30 5]);
%
%END of File

