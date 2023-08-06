"""
================
Qsca vs diameter
================

"""


import numpy as np
from PyMieSim.experiment import SphereSet, SourceSet, Setup
from PyMieSim.materials import Gold, Silver, Aluminium
from PyMieSim import measure

scatterer_set = SphereSet(
    diameter=np.linspace(1e-09, 800e-9, 300),
    material=[Silver, Gold, Aluminium],
    n_medium=1
)

source_set = SourceSet(
    wavelength=400e-9,
    polarization=0,
    amplitude=1
)

experiment = Setup(
    scatterer_set=scatterer_set,
    source_set=source_set
)

data = experiment.Get(Input=[measure.Qabs])

figure = data.plot(
    y=measure.Qabs,
    x=scatterer_set.diameter,
    y_scale="log"
)

figure.show()

# -
