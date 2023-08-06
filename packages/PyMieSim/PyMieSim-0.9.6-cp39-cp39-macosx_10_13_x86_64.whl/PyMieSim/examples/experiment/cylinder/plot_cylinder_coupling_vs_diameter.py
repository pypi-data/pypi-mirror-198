"""
====================
coupling vs diameter
====================

"""


import numpy
from PyMieSim.experiment import CylinderSet, SourceSet, Setup, PhotodiodeSet
from PyMieSim import measure
from PyMieSim.materials import BK7

scatterer_set = CylinderSet(
    diameter=numpy.linspace(100e-9, 3000e-9, 200),
    material=BK7,
    n_medium=1.0
)

source_set = SourceSet(
    wavelength=1200e-9,
    polarization=90,
    amplitude=1
)

detector_set = PhotodiodeSet(
    NA=[0.1, 0.05],
    phi_offset=-180.0,
    gamma_offset=0.0,
    sampling=600,
    filter=None
)

experiment = Setup(
    scatterer_set=scatterer_set,
    source_set=source_set,
    detector_set=detector_set
)

data = experiment.Get([measure.coupling])

figure = data.plot(
    y=measure.coupling,
    x=scatterer_set.diameter,
    y_scale='linear',
    normalize=True
)

figure.show()
