"""
======================
Qsca vs wavelength std
======================

"""


import numpy as np
from PyMieSim.experiment import CylinderSet, SourceSet, Setup
from PyMieSim.materials import Silver
from PyMieSim import measure

scatterer_set = CylinderSet(
    diameter=np.linspace(400e-9, 1400e-9, 10),
    material=Silver,
    n_medium=1
)

source_set = SourceSet(
    wavelength=np.linspace(200e-9, 1800e-9, 300),
    polarization=[0],
    amplitude=1
)

experiment = Setup(scatterer_set, source_set)

data = experiment.Get(measure.Qsca)

figure = data.plot(
    y=measure.Qsca,
    x=source_set.wavelength,
    y_scale='log',
    std=scatterer_set.diameter
)

figure.show()
