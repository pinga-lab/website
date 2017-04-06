---
title: "Processamento e Inversão de Dados de Campos Potenciais: Novas Abordagens"
date: 2013-01-16
period: 2011-2013
author: oliveira-jr
advisor: barbosa
institution: Observatório Nacional
pdf: oliveira-jr-phd.pdf
level: PhD
sucupira: 314927
layout: publication
---

# About

Papers produced from this research:

* [/papers/paper-polynomial-eqlayer-2013]
* [/papers/paper-radial3d-gradients-2013]


# Abstract

This thesis has developed two new methodologies for processing and interpreting
potential field data. The first one is the Polynomial Equivalent Layer, which
is a new cost-effective method for processing large potential-field data sets
via the equivalent-layer technique.  In this approach, the equivalent layer is
divided into a regular grid of equivalent-source windows. Inside each window,
the physical-property distribution is described by a bivariate polynomial.
While the classical approach directly estimates the physical-property
distribution within the equivalent layer, the method Polynomial Equivalent
Layer deals with a linear system of equations with dimension based on the total
number of polynomial coefficients within all equivalent-source windows. This
new method drastically reduces the number of parameters to be estimated in the
inverse problem if compared with the classical approach. By comparing the total
number of floating-point operations required to estimate an equivalent layer
via our method with the classical approach, both formulated with Cholesky's
decomposition, we verify that the computation time required for building the
linear system and for solving the linear inverse problem can be reduced by as
many as three and four orders of magnitude, respectively.  Applications to both
synthetic and real data show that our method performs the standard linear
transformations of potential-field data accurately.  The second new methodology
developed in this thesis is a non-linear method for inverting gravity-gradient
data to estimate the shape of an isolated 3-D geological body located in
subsurface. This method assumes the knowledge about the depth to the top and
density contrast of the source. The geologic body is approximated by an
ensemble of vertically juxtaposed 3-D right prisms, each one with known
thickness and density contrast. All prisms have a polygonal horizontal
cross-section whose vertices are equally spaced from 0<sup>o</sup> to
360<sup>o</sup> and have their horizontal locations described in polar
coordinates referred to an origin inside the polygon. The method recovers the
geometry of the geological body by estimating the radii of all vertices and the
horizontal Cartesian coordinates of all origins defining the horizontal
cross-sections of all prisms.  This problem is formulated as a constrained
non-linear optimization and we also used a preconditioning strategy in order to
improve the convergence. Although the proposed inverse method can obtain a
stable estimate that fits the observed data, different estimates with different
maximum depths can produce equally acceptable data fits. To deal with this
ambiguity, we produced a set of estimates with different maximum depths and
used a criterion based on the L1 norm of the residuals and the estimated volume
for choosing the estimate with optimum maximum depth. This criterion allows the
analysis of the in-depth resolution of the observed gravity-gradient data. We
confirmed the ability of our method to recover the source geometry entirely if
the data have sufficient in-depth resolution. If not, our method is able to
recover only the upper part of the source. By inverting the data from a survey
over the Vinton salt dome (Louisiana, USA) with a density contrast of 0.55
g/cm<sup>3</sup>, we estimated a massive cap rock whose maximum depth attains
460 ± 10 m and its shallowest portion is elongated in the northeast-southwest
direction, according to the direction of the main geological fault in the study
area.

