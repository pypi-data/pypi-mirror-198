Ray-tracing
============
.. _ray_tracing:

There are two distinct uses of the ray-tracing code: to create redistribution matrices for the matrix framework,
and to define and calculate structures which are treated in their entirety by ray-tracing (so the matrix framework is not used).
Both of these methods can be used in combination with TMM lookup tables to calculate realistic reflection, transmission
and absorption probabilities.
The function :literal:`RT` is used to create redistribution matrices, while the class :literal:`rt_structure` is used to define
structures for ray-tracing.

.. automodule:: rayflare.ray_tracing.rt
    :members:
    :undoc-members:
