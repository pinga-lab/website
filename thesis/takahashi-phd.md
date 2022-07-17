---
title: "Camada equivalente convolucional para processamento de dados potenciais"
date: 2021-09-27
period: 2017-2021
author: takahashi
advisor: oliveira-jr
coadvisor: barbosa
institution: Observatório Nacional
pdf: takahashi-phd.pdf
level: PhD
sucupira: 11422970
related_papers: paper-polynomial-eqlayer-2013, paper-fast-iterative-eqlayer-grav-2017, convolutional-eql-grav, convolutional-eql-mag
related_thesis: oliveira-jr-phd, siqueira-phd
layout: publication
---

# Resumo

Neste trabalho foi desenvolvida uma eficiente e rápida técnica de camada
equivalente para o processamento de dados de campos potenciais usando um método
de convolução discreta que modifica o cálculo do problema direto dos métodos
iterativos baseado em um vínculo de excesso de massa para o caso gravimétrico e
o algoritmo do gradiente conjugado por mínimos quadrados para o caso magnético.
Aproveitando das estruturas block-Toeplitz Toeplitz-block (BTTB) da matriz de
sensibilidade, que surge quando grids de observações e de fontes equivalentes
(pontos de massa ou dipolos) são regulares, desenvolvemos um algoritmo que
reduz drasticamente o número de cálculos de pontos flutuantes (flops) e de
memória RAM necessária para estimar a distribuição de propriedade física 2D
sobre a camada equivalente. A estrutura da matriz BTTB pode ser escrita usando
somente a primeira coluna da matriz de sensibilidade, que pode ser transformada
em uma matriz block-circulant circulant-block (BCCB). Similarmente, somente a
primeira coluna da matriz BCCB é necessária para reconstrui- la. Usando a
primeira coluna da BCCB também é possível calcular seus autovalores por uma
transformada de Fourier 2D (2D FFT), que pode ser usada para calcular
rapidamente o problema direto da camada equivalente. Como resultado, este método
pode ser usado para processar grandes conjuntos de dados de forma eficiente.
Testes com dados sintéticos mostram que o método estima as fontes equivalentes
de forma satisfatória para técnicas de processamento, como por exemplo, a
continuação para cima de dados gravimétricos e magnéticos. Os resultados mostram
efeitos de borda e de ruído muito reduzidos comparados ao método tradicional no
domínio de Fourier. Para o caso gravimétrico, os testes sintéticos mostram que
para processar 1.000.000 de observações, este método precisou de aproximadamente
30,9 segundos, enquanto que o método iterativo com vínculo de massa levou
aproximadamente 46,8 segundos com apenas 22.500 observações. Um teste com o dado
real da Província de Carajás, Brasil, mostra o baixo custo computacional deste
método para processar grandes volumes de dados, usando 250.000 observações.
Testes sintéticos com dados magnéticos mostram uma diminuição da ordem de
aproximadamente 10.000 vezes em flops e aproximadamente 25 vezes em tempo
computacional com um grid de tamanho médio de 100 × 50 se comparado o método
clássico da solução de sistemas lineares das equações normais por mínimos
quadrados usando o método da decomposição de Cholesky. Resultados ainda melhores
são obtidos usando milhões de dados, mostrando um decréscimo exponencial no uso
de memória RAM e de custo computacional, permitindo o uso deste método em
computadores pessoais. Os resultados mostram, comparado ao método de Fourier,
que o processamento magnético requer tempo computacional similar, mas produz
menores efeitos de borda sem usar nenhum tipo de padding e também se mostrando
muito mais robusta para lidar com dados irregulares ou superfícies onduladas.
Um teste com 1.310.000 dados irregularmente espaçados da Província de Carajás,
Brasil, confirma com sucesso este método levando aproximadamente 385,56 segundos
para estimar a distribuição de propriedade física e aproximadamente 2,64
segundos para calcular a continuação para cima.

# Abstract

We have developed an efficient and very fast equivalent-layer technique for
gravity and magnetic data processing by modifying the forward problem
calculation of an iterative method grounded on excess mass constraint that does
not require the solution of linear systems and of the conjugate gradient least
squares algorithm, respectively, using a discrete convolutional method. Taking
advantage of the Block- Toeplitz Toeplitz-block (BTTB) structure of the
sensitivity matrix, that raises when regular grids of observation points and
equivalent sources (point masses or dipoles) are used to set up a fictitious
equivalent layer, we have developed an algorithm which greatly reduces the
number of floating-point operations (flops) and computer memory necessary to
estimate a 2D physical property distribution over the equivalent layer. The
structure of the BTTB matrix can be written by using only the elements of the
first column of the sensitivity matrix, which in turn can be transformed into a
block-circulant circulant-block (BCCB) matrix. Likewise, only the first column
of the BCCB matrix is needed to reconstruct the full sensitivity matrix
completely. Also, from the first column of BCCB matrix, its eigenvalues can be
calculated using the 2D Fast Fourier Transform (2D FFT), which can be used to
readily compute the matrix-vector product of the forward modeling in the fast
equivalent-layer technique. As a result, our method is efficient to process very
large datasets. Tests with synthetic data demonstrate the ability of our method
to satisfactorily use the estimated equivalent sources for data processing, for
example, upward-continuing the gravity and magnetic data. Our results show very
small border effects and noise amplification compared to those produced by the
classical approach in the Fourier domain. For the gravity case, our synthetic
results show that while the running time of our method is ≈ 30.9 seconds for
processing N = 1, 000, 000 observations, the iterative method grounded on excess
mass constrain spent ≈ 46.8 seconds with N = 22, 500. A test with field data
from Caraj ́as Province, Brazil, illustrates the low computational cost of our
method to process a large data set composed of N = 250, 000 observations.
Synthetic tests for magnetic data with a mid-size 100×50 grid of total field
anomaly data show a decrease of ≈ 104 in floating-point operations and ≈ 25x in
computation runtime of our method compared to the classical approach of solving
the least-squares normal equations via Cholesky decomposition. Faster results
are obtained for millions of data, showing drastic decreases in computer memory
usage and runtime, allowing to perform magnetic data processing of large data
sets on regular desktop computers. Our results also show that, compared to the
classical Fourier approach, the magnetic data processing with our method
requires similar computation time, but produces significantly smaller border
effects without using any padding scheme and also is more robust to deal with
data on irregularly spaced points or on undulating observation surfaces. A test
with 1, 310, 000 irregularly spaced field data over the Caraj ́as Province,
Brazil, confirms the efficiency of our method by taking ≈ 385.56 seconds to
estimate the physical-property distribution over the equivalent layer
and ≈ 2.64 seconds to compute the upward-continuation.
