---
title: "Fast 3D magnetic inversion of a surface relief in the space domain"
date: 2019-10-01
author: marlon, barbosa
journal: Geophysics
doi: 10.1190/geo2018-0712.1
citation: "Hidalgo-Gato, M., and V. Barbosa (2019), Fast 3D magnetic inversion of a surface relief in the space domain, Geophysics, 84(5), J57-J67, doi:10.1190/geo2018-0712.1."
layout: publication
---

# Abstract

We have developed a fast 3D regularized magnetic inversion algorithm for
depth-to-basement estimation based on an efficient way to compute the total-field
anomaly produced by an arbitrary interface separating nonmagnetic sediments from
a magnetic basement. We approximate the basement layer by a grid of 3D vertical
prisms juxtaposed in the horizontal directions, in which the prisms’ tops represent
the depths to the magnetic basement. To compute the total-field anomaly produced
by the basement relief, the 3D integral of the total-field anomaly of a prism is
simplified by a 1D integral along the prism thickness, which in turn is multiplied
by the horizontal area of the prism. The 1D integral is calculated numerically
using the Gauss-Legendre quadrature produced by dipoles located along the vertical
axis passing through the prism center. This new magnetic forward modeling overcomes
one of the main drawbacks of the nonlinear inverse problem for estimating the
basement depths from magnetic data: the intense computational cost to calculate
the total-field anomaly of prisms. The new sensitivity matrix is simpler and
computationally faster than the one using classic magnetic forward modeling based
on the 3D integrals of a set of prisms that parameterize the earth’s subsurface.
To speed up the inversion at each iteration, we used the Gauss-Newton approximation
for the Hessian matrix keeping the main diagonal only and adding the first-order
Tikhonov regularization function. The large sparseness of the Hessian matrix allows
us to construct and solve a linear system iteratively that is faster and demands
less memory than the classic nonlinear inversion with prism-based modeling using
3D integrals. We successfully inverted the total-field anomaly of a simulated
smoothing basement relief with a constant magnetization vector. Tests on field
data from a portion of the Pará-Maranhão Basin, Brazil, retrieved a first
depth-to-basement estimate that was geologically plausible.
