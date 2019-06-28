.. _README:

======
README
======

stream_depletion is a Python package that can be used to evaluate the stream depleting effects of pumping
a well at a rate :math:`Q(t)`.
d that allows for the calculation of the stream depletion effects  


Theis (1941) obtained solutions that describe a fully penetrating stream (acting as a flow boundary)
with a perfect hydraulic connection to an unconfined aquifer (Figure 4-1)



Installation
------------

stream_depletion can be installed via conda::

   conda install stream_depletion -c WilcoTerink

or via pip::

   pip install stream_depletion
   
   
Using stream_depletion
----------------------

After installation, the python package can be executed by::

   from stream_depletion.sd_calc import *
   
Copyright
---------
   
Copyright (C) 2019 Wilco Terink & Matt Smith. stream_depletion is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see `http://www.gnu.org/licenses/ <http://www.gnu.org/licenses/>`__.      