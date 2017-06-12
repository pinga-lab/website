---
title: "Otimização Computacional do Método da Camada Equivalente"
date: 2016-10-21
period: 2013-2016
author: siqueira
advisor: barbosa
coadvisor: oliveira-jr
institution: Observatório Nacional
pdf: siqueira-phd.pdf
level: PhD
sucupira: 4216876
layout: publication
related_papers: paper-fast-iterative-eqlayer-grav-2017
---


# Abstract

We have developed an iterative scheme for processing gravity data using a fast
equivalent-layer technique. This scheme estimates a 2D mass distribution on a
fictitious layer located below the observation surface and with finite horizontal
dimensions composed by a set of point masses, one directly beneath each gravity
station. Our method starts from an initial approximation to a mass distribution
that is proportional to the measured vertical component of gravity attraction.
Iteratively, our approach updates the mass distribution by adding mass corrections
that is proportional to the gravity residual. At each iteration, the computation
of the residual is accomplished by the forward modelling of the vertical component
of the gravity attraction produced by the set of point masses. Our method is
grounded on the Gauss's theorem and on the positive correlation between the
vertical component of the gravity attraction and the masses on the equivalent
layer. Mathematically, the algorithm can be formulated as an iteratively
least-squares method. However, in practice, it requires neither matrix
multiplications nor the solution of linear systems, leading to a computational
efficiency that allows a rapid processing of large data sets. The time spent
on forward modelling accounts for the much of the total computation time; but
this modelling demands a low computational effort. We numerically prove the
stability of our method by comparing our solution with the one obtained via
the classical equivalent-layer technique with the zeroth-order Tikhonov
regularization. After estimating the mass distribution, we obtain a desired
processed data by multiplying the matrix of Green's functions associated with
the desired processed by the estimated mass distribution. We have applied
the proposed method to interpolate, to calculate the horizontal components
and to continue the gravity data upward (or downward). Furthermore, we
calculate the six components of Full Tensor Gradiometry (FTG) by the product
of the Green matrix associated with each component to the estimated mass
distribution on the layer. We test our method with synthetic data and real
data from the Vinton salt dome, LA, USA, confirm the potential of our
approach in processing large gravity data set over on undulating surface.
