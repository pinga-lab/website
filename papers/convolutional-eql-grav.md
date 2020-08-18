---
title: "Convolutional equivalent layer for gravity data processing"
author: takahashi, oliveira-jr, barbosa
date: 2020-08-18
layout: publication
journal: Geophysics
repository: pinga-lab/Eq_Layer-Toeplitz
doi: XXXXXX
citation: "Diego Takahashi, Vanderlei C. Oliveira Jr., and Valéria C. F. Barbosa, (2020). Convolutional equivalent layer for gravity data processing. Geophysics, ja, X-X. doi: XXXXXX"
related_thesis: siqueira-phd
inreview: true
oa: false
---

# Abstract

We develop an efficient and very fast equivalent-layer technique for gravity data processing by modifying an iterative method grounded on an excess mass constraint that does not require the solution of linear systems. Taking advantage of the symmetric Block-Toeplitz Toeplitz-Block (BTTB) structure of the sensitivity matrix, that arises when regular grids of observation points and equivalent sources (point masses) are used to set up a fictitious equivalent layer, we develop an algorithm that greatly reduces the computational complexity and RAM memory necessary to estimate a 2D mass distribution over the equivalent layer. The structure of symmetric BTTB matrix consists of the elements of the first column of the sensitivity matrix, which in turn can be embedded into a symmetric Block-Circulant Circulant-Block (BCCB) matrix. Likewise, only the first column of the BCCB matrix is needed to reconstruct the full sensitivity matrix completely. From the first column of BCCB matrix, its eigenvalues can be calculated using the 2D Fast Fourier Transform (2D FFT), which can be used to readily compute the matrix-vector product of the forward modeling in the fast equivalent-layer technique. As a result, our method is eficient for processing 1 very large datasets. Tests with synthetic data demonstrate the ability of our method to satisfactorily upward- and downward-continuing gravity data. Our results show very small border effects and noise amplification compared to those produced by the classical approach in the Fourier domain. Besides, they show that while the running time of our method is nearly 30.9 seconds for processing N = 1,000,000 observations, the fast equivalent-layer technique spent approximately 46.8 seconds with N = 22,500. A test with field data from Carajás Province, Brazil, illustrates the low computational cost of our method to process a large data set composed of N = 250,000 observations.
