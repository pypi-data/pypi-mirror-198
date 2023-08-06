"""
===============
SPF computation
===============

"""

from PyMieSim.scatterer import Sphere
from PyMieSim.source import PlaneWave

source = PlaneWave(
    wavelength=500e-9,
    polarization=0,
    amplitude=1
)

scatterer = Sphere(
    diameter=1200e-9,
    source=source,
    index=1.4,
    n_medium=1.0
)

spf = scatterer.get_spf(sampling=300)

figure = spf.plot()

figure.show()

# -
