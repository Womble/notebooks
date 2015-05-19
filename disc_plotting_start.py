# coding: utf-8

import pyfits as P, complete as C, disc as d
import mayavi
from mayavi import mlab
disc=P.getdata('/import/phy-pc1064_a/opt/LIME/LimePackage/disk/disk_model/disk2.fits.gz')
vel=P.getdata('/import/phy-pc1064_a/opt/LIME/LimePackage/disk/disk_model/vels2.fits.gz')
grid=mgrid[-128:128,-128:128]
X=grid[1,...]
Y=grid[0,...]
R=sqrt(X**2+Y**2)
theta=arctan2(Y,X)
theta=theta.reshape((256,256,1))
vx=vel[...,0]/100
vy=vel[...,1]/100
vz=vel[...,2]/100
vr=vx*cos(theta)+vy*sin(theta)
vq=vy*cos(theta)-vx*sin(theta)
vn=vx*0
rho=disc[1,...].T
temp=disc[0,...].T
