# coding: utf-8
temp2=temp.copy()
temp2[temp2<40]=39
temp3=temp2.copy()
temp3[:,temp2.shape[1]/2:,:]=40
Rscalar=mlab.pipeline.scalar_field(temp3[:,:,:])
mlab.pipeline.volume(Rscalar)
mlab.axes(Rscalar,ranges=(-64,64, -64,64, -16,16), nb_labels=3, line_width=3.0)
extents=[(0,128, 0,128, 0,64),(0,128, 128,256, 0,64),(128,256, 0,128, 0,64),(128,256, 128,256, 0,64),(0,256, 0,256, 0,32)]
for e in extents:
    mlab.pipeline.outline(Rscalar, extent=e, line_width=0.5)
Rscalar2=mlab.pipeline.scalar_field(temp2[:,:,:])
mlab.pipeline.scalar_cut_plane(Rscalar2, plane_orientation='z_axes')
mlab.view(azimuth=300, elevation=60)
