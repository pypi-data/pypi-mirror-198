"""
=========================
a1 scattering coefficient
=========================

"""

import numpy as np
from PyMieSim.experiment import SphereSet, SourceSet, Setup
from PyMieSim import measure

scatterer_set = SphereSet(
    diameter=np.linspace(100e-9, 10000e-9, 1000),
    index=1.4,
    n_medium=1
)

source_set = SourceSet(
    wavelength=400e-9,
    polarization=0,
    amplitude=1
)

experiment = Setup(scatterer_set=scatterer_set, source_set=source_set)

Data = experiment.Get(Input=[measure.a1])

Data.plot(y=measure.a1, x=scatterer_set.diameter).show()



