"""
====================
coupling vs diameter
====================

"""


import numpy
from PyMieSim.experiment import CoreShellSet, SourceSet, Setup, PhotodiodeSet
from PyMieSim import measure
from PyMieSim.materials import BK7, Silver

scatterer_set = CoreShellSet(
    core_diameter=numpy.geomspace(100e-09, 600e-9, 400),
    shell_diameter=800e-9,
    core_material=Silver,
    shell_material=BK7,
    n_medium=1
)

sourceSet = SourceSet(
    wavelength=1200e-9,
    polarization=90,
    amplitude=1
)

detecSet = PhotodiodeSet(
    NA=[0.1, 0.05],
    phi_offset=-180.0,
    gamma_offset=0.0,
    sampling=600,
    filter=None
)

experiment = Setup(scatterer_set, sourceSet, detecSet)

data = experiment.Get([measure.coupling])

figure = data.plot(
    y=measure.coupling,
    x=scatterer_set.core_diameter,
    y_scale='linear',
    normalize=True
)

figure.show()
