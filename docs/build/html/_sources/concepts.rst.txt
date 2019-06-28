.. _concepts:

========
Concepts
========

Analytical solutions for constant pumping rate
----------------------------------------------

This package is entirely based on the analytical solutions as described by
:cite:`Theis1940`, that describe a fully penetrating stream with a perfect hydraulic connection to an
unconfined aquifer (:numref:`fig_theis_concept`).

.. _fig_theis_concept:

.. figure:: images/theis_concept.png
   :alt: The conceptual model considered by Theis :cite:`Theis1940`.
   :figwidth: 70% 
   
   The conceptual model considered by Theis :cite:`Theis1940`.

A generalised solution in terms of the complementary error function was developed by :cite:`Glover1954`; however, the two
solutions are identical. The generalised solution as provided by :cite:`Glover1954` for estimating stream depletion is:

.. math::
   :label: eq_glover
   
   \Delta{Q} = erfc\left(\sqrt\frac{S\cdot L^2}{4\cdot T\cdot t}\right) \cdot Q_w
   
with:

.. math::
   :nowrap:
   
   \begin{eqnarray}
   \Delta{Q}& =& \text{stream depletion rate}\ [L^3T^{-1}]\\
   L& =& \text{shortest distance between the pumped bore and the stream}\ [L]\\
   Q_w& =& \text{constant flow rate from the pumped bore}\ [L^3T^{-1}]\\
   T& =& \text{aquifer transmissivity}\ [L^2T^{-1}]\\
   S& =& \text{aquifer storativity, specific yield, or effective porosity}\ [-]\\
   t& = & \text{time since pumping began}\ [T]
   \end{eqnarray}
   
   
Superposition principle
-----------------------

As all the equations used are linear and consist of coefficients that do not depend upon time, superposition and time translation can be used.
That is, the superposition principle allows the solutions for differing time periods to be subtracted to obtain a solution that models both depletion
due to abstraction and a reducing in depletion due to pumping ceasing (abstraction and recovery) phases of well pumping :cite:`Reilly1984`.

