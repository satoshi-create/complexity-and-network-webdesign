import numpy as np
import pyvista as pv
import streamlit as st
import stpyvista

## Initialize a plotter object
plotter = pv.Plotter(pv.Plotter(window_size=[400,400]))

rng = np.random.default_rng(seed=0)
point_cloud = rng.random((100, 3))
pdata = pv.PolyData(point_cloud)
pdata['orig_sphere'] = np.arange(100)

# create many spheres from the point cloud
sphere = pv.Sphere(radius=0.02, phi_resolution=10, theta_resolution=10)
pc = pdata.glyph(scale=False, geom=sphere, orient=False)
#pc.plot(cmap='Reds')

plotter.view_isometric()
plotter.set_background="white"

plotter.add_mesh(sphere)
plotter.add_mesh(pc, cmap="Reds")

# doesn't integrate with streamlit so no point in drawing
#st.draw(pc)

## Send to streamlit
stpyvista.stpyvista(plotter)
