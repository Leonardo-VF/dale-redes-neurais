"""Creates sparse neural weight matrices."""

import numpy as np
import scipy.stats as st


def _generate_weights(N, Ne, muE, sigmaE, muI, sigmaI):
    """Generates a dense weight matrix with the given parameters."""
    norm = np.sqrt(N)
    muEnorm = muE / norm
    muInorm = muI / norm
    sigmaEnorm = sigmaE / norm
    sigmaInorm = sigmaI / norm
    w = np.zeros((N, N))
    w[:, :Ne] = np.random.normal(muEnorm, sigmaEnorm, size=(N, Ne))
    w[:, Ne:] = np.random.normal(muInorm, sigmaInorm, size=(N, N-Ne))
    return w


def _generate_connection_homogeneous(N, density):
    """Generates a sparse homogenous connection matrix with the given density."""
    return (np.random.random(size=(N, N)) < density) * 1


def generate_homogeneous(N, density, Ne, muE, sigmaE, muI, sigmaI):
    """Generates a homogeneous sparse weight matrix with the given density and weight parameters."""
    w = _generate_weights(N, Ne, muE, sigmaE, muI, sigmaI)
    c = _generate_connection_homogeneous(N, density)
    return w * c


def _generate_connection_heterogeneous(N, gamma, k0, *, outdegree=True):
    """Generates a connection matrix with power-law distribution of connections with coefficient gamma and minimum value k0"""
    ks = np.round(st.pareto.rvs(gamma-1, scale=k0, size=N)).astype(int)
    ks[ks >= N] = N
    c = np.zeros((N, N))
    for j in range(N):
        active = np.random.choice(N, ks[j], replace=False)
        if outdegree:
            c[active, j] = 1
        else:
            c[j, active] = 1
    return c


def generate_heterogeneous(N, gamma, k0, Ne, muE, sigmaE, muI, sigmaI, *, outdegree=True):
    """Generates a heterogenous sparse weight matrix with the given weight parameters and a power-law connection distribution with coefficent gamma and minimum value k0"""
    w = _generate_weights(N, Ne, muE, sigmaE, muI, sigmaI)
    c = _generate_connection_heterogeneous(N, gamma, k0, outdegree=outdegree)
    return w * c


