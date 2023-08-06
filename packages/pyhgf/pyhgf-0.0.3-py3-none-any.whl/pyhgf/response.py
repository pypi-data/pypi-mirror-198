# Author: Nicolas Legrand <nicolas.legrand@cas.au.dk>

from typing import TYPE_CHECKING

import jax.numpy as jnp

from pyhgf.continuous import gaussian_surprise

if TYPE_CHECKING:
    from pyhgf.model import HGF


def first_level_gaussian_surprise(hgf: "HGF", response_function_parameters=None):
    """Gaussian surprise at the first level of a probabilistic network.

    .. note::
      The Gaussian surprise at the first level is the default method to compute surprise
      for continuous models. The function returns `jnp.inf` if the model could not fit
      at a given time point.

    Parameters
    ----------
    hgf :
        Instance of the HGF model.
    response_function_parameters :
        No additional parameters are required to compute the Gaussian surprise.

    Returns
    -------
    surprise :
        The model surprise given the input data.

    """
    # compute the sum of Gaussian surprise at the first level
    # the input value at time t is compared to the gaussian prediction at t-1
    surprise = jnp.sum(
        gaussian_surprise(
            x=hgf.node_trajectories[0]["value"][1:],
            muhat=hgf.node_trajectories[1]["muhat"][:-1],
            pihat=hgf.node_trajectories[1]["pihat"][:-1],
        )
    )

    # Return an infinite surprise if the model could not fit at any point
    return jnp.where(
        jnp.any(jnp.isnan(hgf.node_trajectories[1]["mu"])), jnp.inf, surprise
    )


def first_level_binary_surprise(hgf: "HGF", response_function_parameters=None):
    """Sum of the binary surprise along the time series (binary HGF).

    .. note::
      The binary surprise is the default method to compute surprise when
      `model_type=="binary"`, therefore this method will only return the sum of
      valid time points, and `jnp.inf` if the model could not fit.

    Parameters
    ----------
    hgf :
        Instance of the HGF model.
    response_function_parameters :
        No additional parameters are required to compute the binary surprise.

    Returns
    -------
    surprise :
        The model surprise given the input data.

    """
    # Return an infinite surprise if the model cannot fit
    this_surprise = jnp.where(
        jnp.isnan(hgf.node_trajectories[0]["surprise"]),
        jnp.inf,
        hgf.node_trajectories[0]["surprise"],
    )

    # Sum the surprise for this model
    surprise = jnp.sum(this_surprise)

    return surprise
