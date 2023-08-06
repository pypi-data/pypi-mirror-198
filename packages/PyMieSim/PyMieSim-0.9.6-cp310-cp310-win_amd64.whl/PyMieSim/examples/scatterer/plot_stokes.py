"""
=============================
Stokes parameters computation
=============================

"""

from PyMieSim.scatterer import Sphere
from PyMieSim.source import PlaneWave

source = PlaneWave(
    wavelength=450e-9,
    polarization=0,
    amplitude=1
)

scatterer = Sphere(
    diameter=300e-9,
    source=source,
    index=1.4
)

stokes = scatterer.get_stokes(sampling=100)

figure = stokes.plot()

figure.show()

# -
