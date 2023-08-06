"""
=========================
a1 scattering coefficient
=========================

"""


import numpy as np
from PyMieSim.experiment import CylinderSet, SourceSet, Setup
from PyMieSim import measure

scatterer_set = CylinderSet(
    diameter=np.linspace(100e-9, 10000e-9, 800),
    index=1.4,
    n_medium=1
)

source_set = SourceSet(
    wavelength=400e-9,
    polarization=90,
    amplitude=1
)

experiment = Setup(scatterer_set=scatterer_set, source_set=source_set)

data = experiment.Get(Input=[measure.a11])

data.plot(y=measure.a11, x=scatterer_set.diameter).show()
