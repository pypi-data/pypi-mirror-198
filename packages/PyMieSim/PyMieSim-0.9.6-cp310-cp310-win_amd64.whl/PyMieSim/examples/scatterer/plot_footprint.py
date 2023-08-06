"""
===================
Scatterer footprint
===================

"""

from PyMieSim.scatterer import Sphere
from PyMieSim.detector import LPmode
from PyMieSim.source import PlaneWave
from PyOptik import ExpData

detector = LPmode(
    Mode="2-1",
    NA=0.3,
    sampling=200,
    gamma_offset=0,
    phi_offset=0,
    coupling_mode='Point'
)

source = PlaneWave(
    wavelength=450e-9,
    polarization=0,
    amplitude=1
)

scatterer = Sphere(
    diameter=2000e-9,
    source=source,
    material=ExpData('BK7')
)

footprint = detector.get_footprint(scatterer)

figure = footprint.plot()

figure.show()

# -
