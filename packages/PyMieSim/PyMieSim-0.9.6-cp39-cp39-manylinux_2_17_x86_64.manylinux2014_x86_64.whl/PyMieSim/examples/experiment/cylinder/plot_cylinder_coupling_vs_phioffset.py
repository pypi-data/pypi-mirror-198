"""
==========
goniometer
==========

"""

import numpy as np
from PyMieSim.experiment import CylinderSet, SourceSet, Setup, PhotodiodeSet
from PyMieSim.materials import BK7
from PyMieSim import measure

detector_set = PhotodiodeSet(
    NA=[0.5, 0.3, 0.1, 0.05],
    phi_offset=np.linspace(-180, 180, 400),
    gamma_offset=0,
    sampling=400,
    filter=None
)

scatterer_set = CylinderSet(
    diameter=2000e-9,
    material=BK7,
    n_medium=1
)

source_set = SourceSet(
    wavelength=1200e-9,
    polarization=90,
    amplitude=1e3
)

experiment = Setup(
    scatterer_set=scatterer_set,
    source_set=source_set,
    detector_set=detector_set
)

data = experiment.Get(measure.coupling)

figure = data.plot(
    y=measure.coupling, 
    x=detector_set.phi_offset, 
    y_scale='log', 
    normalize=True
)

figure.show()

