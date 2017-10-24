---
title: "Ellipsoids (v1.0): 3D Magnetic modelling of ellipsoidal bodies"
author: takahashi, oliveira-jr
layout: publication
date: 2017-09-28
journal: Geoscientific Model Development (GMD)
repository: pinga-lab/magnetic-ellipsoid
pdf: magnetic-ellipsoid.pdf
doi: 10.5194/gmd-10-3591-2017
related_thesis: takahashi-msc
citation: "Takahashi, D. and Oliveira Jr., V. C.: Ellipsoids (v1.0): 3-D magnetic modelling of ellipsoidal bodies, Geosci. Model Dev., 10, 3591-3608, https://doi.org/10.5194/gmd-10-3591-2017, 2017."
inreview: false
oa: true
---

# About

Ellipsoids are the only bodies for which the self-demagnetization can be
treated analytically. This property is particularly useful for modelling
compact ore bodies having high susceptibility. Here, we present a review of the
magnetic modelling of ellipsoids, propose an alternative way of determining the
isotropic susceptibility above which the self-demagnetization must be taken
into consideration, as well as provide a set of routines to model the magnetic
field produced by ellipsoids.

All the code developed for generating the results presented in the paper, as
well as the code developed for generating additional numerical simulations, can
be found at the online
[Github repository](https://github.com/pinga-lab/magnetic-ellipsoid).

The paper has been published on the journal Geoscientific Model Development (GMD)
and can be freely accessed at
[the journal website](https://www.geosci-model-dev.net/10/3591/2017/gmd-10-3591-2017.html).


# Abstract

A considerable amount of literature has been published on the magnetic
modelling of uniformly magnetized ellipsoids since the second half of
the nineteenth century. Ellipsoids have flexibility to represent a wide
range of geometrical forms, are the only known bodies which can be
uniformly magnetized in the presence of a uniform inducing field and
are the only finite bodies for which the self-demagnetization can be treated
analytically. This property makes ellipsoids particularly useful for
modelling compact orebodies having high susceptibility. In this case,
neglecting the self-demagnetization may strongly mislead the interpretation
of these bodies by using magnetic methods. A number of previous studies
consider that the self-demagnetization can be neglected for the case in
which the geological body has an isotropic susceptibility lower than or
equal to 0.1 SI. This limiting value, however, seems to be determined
empirically and there has been no discussion about how this value was
determined. Besides, the geoscientific community lacks an easy-to-use
tool to simulate the magnetic field produced by uniformly magnetized
ellipsoids. Here, we present an integrated review of the magnetic
modelling of arbitrarily oriented triaxial, prolate and oblate
ellipsoids. Our review includes ellipsoids with both induced and
remanent magnetization, as well as with isotropic or anisotropic
susceptibility. We also discuss the ambiguity between confocal ellipsoids
with the same magnetic moment and propose a
way of determining the isotropic susceptibility above which the
self-demagnetization must be taken into consideration. Tests with
synthetic data validate our approach. Finally, we provide a set
of routines to model the magnetic field produced
by ellipsoids. The routines are written in Python language as
part of the Fatiando a Terra, which is an open-source library
for modelling and inversion in geophysics.
