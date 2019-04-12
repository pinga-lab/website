---
title: Efficient 3D large-scale forward-modeling and inversion of gravitational fields in spherical coordinates with application to lunar mascons
author: guangdong, bo, uieda, jliu, mkaban, lchen, rguo
layout: publication
date: 2019-03-30
journal: "Journal of Geophysical Research: Solid Earth"
doi: 10.1029/2019JB017691
preprint: 10.31223/osf.io/dzf9j
supplement: 10.6084/m9.figshare.7300523
citation: "Zhao, G., Chen, B., Uieda, L., Liu, J., Kaban, M. K., Chen, L., & Guo, R. (2019). Efficient 3D large-scale forward-modeling and inversion of gravitational fields in spherical coordinates with application to lunar mascons. Journal of Geophysical Research: Solid Earth. doi:10.1029/2019JB017691."
related_papers: paper-tesseroids-2016,paper-moho-inversion-tesseroids-2016
alm: true
---

# About

The paper introduces a method for accelerating 3D gravity inversion using
[tesseroids][/papers/paper-tesseroids-2016].
It's fast due to the clever use of symmetry relations when computing the
sensitivity/Jacobian matrix. This requires data laid out on a regular grid and a regular
tesseroid mesh that aligns with the data grid. So there is a sacrifice of flexibility
for performance. Nonetheless, the results are impressive.

# Abstract

An efficient forward modeling algorithm for calculation of gravitational fields in
spherical coordinates is developed for 3D large‐scale gravity inversion problems. 3D
Gauss‐Legendre quadrature (GLQ) is used to calculate the gravitational fields of mass
distributions discretized into tesseroids. Equivalence relations in the kernel matrix of
the forward‐modeling are exploited to decrease storage and computation time. The
numerical tests demonstrate that the computation time of the proposed algorithm is
reduced by approximately two orders of magnitude, and the memory requirement is reduced
by N'λ times compared with the traditional GLQ method, where N'λ is the number of the
model elements in the longitudinal direction. These significant improvements in
computational efficiency and storage make it possible to calculate and store the dense
Jacobian matrix in 3D large‐scale gravity inversions. The equivalence relations can be
applied to the Taylor series method or combined with the adaptive discretization to
ensure high accuracy. To further illustrate the capability of the algorithm, we present
a regional synthetic example. The inverted results show density distributions consistent
with the actual model. The computation took about 6.3 hours and 0.88 GB of memory
compared with about a dozen days and 245.86 GB for the traditional 3D GLQ method.
Finally, the proposed algorithm is applied to the gravity field derived from the latest
lunar gravity model GL1500E. 3D density distributions of the Imbrium and Serenitatis
basins are obtained, and high‐density bodies are found at the depths 10‐60 km, likely
indicating a significant uplift of the high‐density mantle beneath the two mascon
basins.
