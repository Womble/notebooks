# coding: utf-8
vz[vz<-10000]=-10000
vz[vz>10000]=10000
#src = mlab.pipeline.vector_field((-vr*cos(theta))[:,120:136,:], (vq*sin(theta))[:,120:136,:], vz[:,120:136,:], scalars=vy[:,120:136,:])
#mlab.pipeline.vector_cut_plane(src, mask_points=20, scale_factor=30., plane_orientation='y_axes')
#mlab.axes(src, ranges=(-64,64, -64,64, -16,16), nb_labels=3, line_width=3.0)
#mlab.view(azimuth=-90, elevation=90)

src = mlab.pipeline.vector_field(vx,vy,vz)
mlab.pipeline.vector_cut_plane(src, mask_points=20, scale_factor=30., plane_orientation='y_axes')
mlab.axes(src, ranges=(-64,64, -64,64, -16,16), nb_labels=3, line_width=3.0)
mlab.view(azimuth=-90, elevation=90)
