---
title: "Forward modeling and inversion of gravitational fields in spherical coordinates"
date: 2016-04-29
period: 2011-2016
author: uieda
advisor: barbosa
repository: leouieda/phd-thesis
institution: Observatório Nacional
pdf: uieda-phd.pdf
level: PhD
sucupira: 3627205
layout: publication
---

# About

This thesis is a collection of the papers:

* [/papers/paper-tesseroids-2016]
* [Modeling the Earth with Fatiando a Terra](http://www.leouieda.com/talks/scipy2013.html)
* [/papers/paper-moho-inversion-tesseroids-2016]

# Defense slides

<script async class="speakerdeck-embed"
data-id="db1324af5ddc4183b5961497fd87b057" data-ratio="1.33333333333333"
src="//speakerdeck.com/assets/embed.js"></script>

# Abstract

We present methodological improvements to forward modeling and regional
inversion of satellite gravity data. For this purpose, we developed two
open-source software projects. The first is a C language suite of command-line
programs called Tesseroids. The programs calculate the gravitational potential,
acceleration, and gradient tensor of a spherical prism, or tesseroid.
Tesseroids implements and extends an adaptive discretization algorithm to
automatically ensure the accuracy of the computations. Our numerical
experiments show that, to achieve the same level of accuracy, the gravitational
acceleration components require finner discretization than the potential. In
turn, the gradient tensor requires finner discretization still than the
acceleration. The second open-source project is Fatiando a Terra, a Python
language library for inversion, forward modeling, data processing, and
visualization. The library allows the user to combine the forward modeling and
inversion tools to implement new inversion methods. The gravity forward
modeling tools include an implementation of the algorithm used in the
Tesseroids software. We combined the inversion and tesseroid forward modeling
utilities of Fatiando a Terra to develop a new method for fast non-linear
gravity inversion. The method estimates the depth of the crust-mantle interface
(the Moho) based on observed gravity data using a spherical Earth
approximation. We extended the computationally efficient Bott's method to
include smoothness regularization and use tesseroids instead right rectangular
prisms. The inversion is controlled by three hyper-parameters: the
regularization parameter, the density-contrast between the real Earth and the
reference model (the Normal Earth), and the depth of the Moho of the Normal
Earth. We employ two cross-validation procedures to automatically estimate
these parameters. Tests on synthetic data confirm the capability of the
proposed method to estimate smoothly varying Moho depths and the three
hyper-parameters. Finally, we applied the inversion method developed to produce
a Moho depth model for South America. The estimated Moho depth model fits the
gravity data and seismological Moho depth estimates in the oceanic areas and
the central and eastern portions of the continent. We observe large misfits in
the Andes region, where Moho depth is largest. In Amazon, Solimões, and Paraná
Basins, the model fits the observed gravity but disagrees with seismological
estimates. These discrepancies suggest the existence of density-anomalies in
the crust or upper mantle, as has been suggested in the literature.
