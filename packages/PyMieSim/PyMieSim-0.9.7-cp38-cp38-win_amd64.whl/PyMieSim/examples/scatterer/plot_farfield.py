"""
======================
Far-Fields computation
======================

"""


from PyMieSim.scatterer import Sphere
from PyMieSim.source import PlaneWave

source = PlaneWave(
    wavelength=1000e-9,
    polarization=0,
    amplitude=1
)

scatterer = Sphere(
    diameter=1500e-9,
    source=source,
    index=1.4
)

fields = scatterer.get_far_field(sampling=100)

figure = fields.plot()

figure.show()

# -
