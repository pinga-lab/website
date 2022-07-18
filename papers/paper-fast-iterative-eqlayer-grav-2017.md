---
title: "Fast iterative equivalent-layer technique for gravity data processing: A method grounded on excess mass constraint"
author: siqueira, oliveira-jr, barbosa
layout: publication
alm: true
date: 2017-05-05
journal: Geophysics
pdf: paper-fast-iterative-eqlayer-grav-2017.pdf
doi: 10.1190/geo2016-0332.1
citation: "Siqueira, F. C. L., Oliveira Jr., V. C., and V. C. F. Barbosa (2017). Fast iterative equivalent-layer technique for gravity data processing: A method grounded on excess mass constraint. GEOPHYSICS, 82(4), G57-G69. https://doi.org/10.1190/geo2016-0332.1"
related_thesis: oliveira-jr-phd, siqueira-phd
related_papers: paper-polynomial-eqlayer-2013
---

# About

This paper describes a fast iterative equivalent layer
technique designed to gravity data processing. Our approach
consists in estimating the density distribution by using
the excess of mass and the positive correlation between the observed
gravity data and the masses on the equivalent layer.


# Abstract

We have developed a new iterative scheme for processing
gravity data using a fast equivalent-layer technique. This
scheme estimates a 2D mass distribution on a fictitious layer
located below the observation surface and with finite horizontal
dimensions composed by a set of point masses, one directly beneath
each gravity station. Our method starts from an initial
mass distribution that is proportional to the observed gravity
data. Iteratively, our approach updates the mass distribution
by adding mass corrections that are proportional to the gravity
residuals. At each iteration, the computation of the residual is
accomplished by the forward modeling of the vertical component
of the gravitational attraction produced by all point masses
setting up the equivalent layer. Our method is grounded on the
excess of mass and on the positive correlation between the observed
gravity data and the masses on the equivalent layer.
Mathematically, the algorithm is formulated as an iterative least-squares
method that requires neither matrix multiplications nor
the solution of linear systems, leading to the processing of large
data sets. The time spent on the forward modeling accounts for
much of the total computation time, but this modeling demands
a small computational effort. We numerically prove the stability
of our method by comparing our solution with the one obtained
via the classic equivalent-layer technique with the zeroth-order
Tikhonov regularization. After estimating the mass distribution,
we obtain a desired processed data by multiplying the matrix of
the Green’s functions associated with the desired processing by
the estimated mass distribution. We have applied the proposed
method to interpolate, calculate the horizontal components, and
continue gravity data upward (or downward). Testing on field
data from the Vinton salt dome, Louisiana, USA, confirms
the potential of our approach in processing large gravity data
set over on undulating surface.
