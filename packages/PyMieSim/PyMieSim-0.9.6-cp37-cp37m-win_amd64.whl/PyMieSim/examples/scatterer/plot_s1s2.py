"""
==========================
S1 S2 function computation
==========================

"""


from PyMieSim.scatterer import Sphere
from PyMieSim.source import PlaneWave

source = PlaneWave(
    wavelength=450e-9,
    polarization=0,
    amplitude=1
)

scatterer = Sphere(
    diameter=600e-9,
    source=source,
    index=1.4
)

S1S2 = scatterer.get_s1s2(sampling=200)

figure = S1S2.plot()

figure.show()

# -
