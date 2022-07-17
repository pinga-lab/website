---
title: "Convolutional equivalent layer for magnetic data processing"
author: takahashi, oliveira-jr, barbosa
date: 2022-06-12
layout: publication
journal: Geophysics
repository: pinga-lab/Eq_Layer_Mag-Toeplitz
doi: 10.1190/geo2021-0599.1
citation: "Diego Takahashi, Vanderlei C. Oliveira Jr., and Valéria C. F. Barbosa, (2022). Convolutional equivalent layer for magnetic data processing. Geophysics, XX(X) ja, XXXX. doi: 10.1190/geo2021-0599.1"
related_thesis: oliveira-jr-phd, siqueira-phd, takahashi-phd
related_papers: paper-polynomial-eqlayer-2013, paper-fast-iterative-eqlayer-grav-2017, convolutional-eql-grav
oa: false
---

# Abstract

We demonstrate that the sensitivity matrix associated with an equivalent layer
of dipoles can be arranged to a Block-Toeplitz Toeplitz-Block (BTTB) structure
for the case where observations and dipoles are aligned on a horizontal and
regularly-spaced grid. The product of a BTTB matrix and an arbitrary vector
represents a discrete convolution and can be efficiently computed via 2D Fast
Fourier Transform. In this case, the matrix-vector product uses only the
elements forming the first column of the BTTB matrix, saving computational time
and memory. Our convolutional equivalent layer method uses this approach to
compute the matrix-vector products in the iterative conjugate gradient algorithm
with the purpose of estimating the physical-property distribution over the
equivalent layer for large data sets. Synthetic tests of total-field anomaly
data show a decrease in both floating-point operations and computation runtime
of our method compared to the classical approach of solving the least-squares
normal equations via Cholesky decomposition. Faster results are obtained for
millions of data, showing drastic decreases in computer memory usage and
runtime, allowing to perform magnetic data processing of large data sets on
regular desktop computers. Our results also show that, compared to the classical
Fourier approach, the magnetic data processing with our method requires similar
computation time, but produces significantly smaller border effects without
using any padding scheme and is also more robust to deal with data on
irregularly spaced points or on irregularly observation surfaces. A test with
irregularly spaced field data over the Carajás Province, Brazil, confirms the
efficiency of our method by estimating the physical-property distribution over
the equivalent layer and computing the upward-continuation.
