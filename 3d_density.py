# coding: utf-8
rho2=rho.copy()
rho2[rho2<10**10]=9e9
mask=zeros(rho2.shape)*1e-15
mask[:,rho2.shape[1]/2:,:]=1
cpy=rho2.copy()
cpy[mask==1]=rho2.min()
Rscalar=mlab.pipeline.scalar_field(log10(cpy/1e6))
Rscalar2=mlab.pipeline.scalar_field(log10(rho2/1e6))
mlab.pipeline.volume(Rscalar)
mlab.pipeline.scalar_cut_plane(Rscalar2, plane_orientation='z_axes')
mlab.axes(Rscalar,ranges=(-64,64, -64,64, -16,16), nb_labels=3, color=(0,0,0))
extents=[(0,128, 0,128, 0,64),(0,128, 128,256, 0,64),(128,256, 0,128, 0,64),(128,256, 128,256, 0,64),(0,256, 0,256, 0,32)]
for e in extents:
    mlab.pipeline.outline(Rscalar, extent=e, color=(0,0,0))    
mlab.view(azimuth=45, elevation=60)
