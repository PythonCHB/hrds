from firedrake import *
from thetis import *
from firedrake import Expression
import sys
sys.path.insert(0,"../../")
from hrds import HRDS

mesh2d = Mesh('test_mesh.msh') # mesh file

P1_2d = FunctionSpace(mesh2d, 'CG', 1)
bathymetry2d = Function(P1_2d, name="bathymetry")
bvector = bathymetry2d.dat.data
bathy = HRDS("gebco_uk.tif", 
             rasters=("emod_utm.tif", 
                      "inspire_data.tif"), 
             distances=(700, 200))
bathy.set_bands()
for i, (xy) in enumerate(mesh2d.coordinates.dat.data):
    bvector[i] = bathy.get_val(xy)
File('bathy.pvd').write(bathymetry2d)




