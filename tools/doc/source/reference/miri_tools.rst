Common tools for MIRI Software (:mod:`miri.tools`)
==================================================

:Release: |release|
:Date: |today|


LICENCE
~~~~~~~

Copyright
^^^^^^^^^
Copyright (c) 2010-2017 The JWST MIRI European Consortium software team. 
All rights reserved.

The miri.tools software has been developed by the MIRI EC software team 
as part of the JWST/MIRI consortium, which includes the following 
organisations: Ames Research Center, USA; Netherlands Foundation for 
Research in Astronomy; CEA Service d'Astrophysique, Saclay, France; 
Centre Spatial de Liege, Belgium; Consejo Superior de Investigacones 
Cientificas, Spain; Danish Space Research Institute; Dublin Institute 
for Advanced Studies, Ireland; EADS Astrium, Ltd., European Space 
Agency, Netherlands; UK; Institute d'Astrophysique Spatiale, France; 
Instituto Nacional de Tecnica Aerospacial, Spain; Institute of 
Astronomy, Zurich, Switzerland; Jet Propulsion Laboratory, USA; 
Laboratoire d'Astrophysique de Marseille (LAM), France; Lockheed 
Advanced Technology Center, USA; Max-Planck-Insitut fur Astronomie 
(MPIA), Heidelberg, Germany; Observatoire de Paris, France; Observatory 
of Geneva, Switzerland; Paul Scherrer Institut, Switzerland; 
Physikalishes Institut, Bern, Switzerland; Raytheon Vision Systems, USA; 
Rutherford Appleton Laboratory (RAL), UK; Space Telescope Science 
Institute, USA; Toegepast-Natuurwetenschappelijk Ondeszoek (TNOTPD), 
Netherlands; UK Astronomy Technology Centre (UKATC); University College, 
London, UK; University of Amsterdam, Netherlands; University of Arizona, 
USA; University of Cardiff, UK; University of Cologne, Germany; 
University of Groningen, Netherlands; University of Leicester, UK; 
University of Leiden, Netherlands; University of Leuven, Belgium; 
University of Stockholm, Sweden, Utah State University USA.

Terms and Conditions of Use
^^^^^^^^^^^^^^^^^^^^^^^^^^^
This software may be used and copied free of charge only for 
non-commercial research purposes. All copies of this software must 
contain this copyright statement and disclaimer. The MIRI consortium 
must be acknowledged in any publications arising from use of this 
software. If you make modifications to this software, you must clearly 
mark the software as having been changed and you must also retain this 
copyright and disclaimer.

Where this software uses facilities developed by other members of the 
MIRI consortium (e.g. its use of JWST infrastructure) it is also bound
by the licences issued with those facilities (see the LICENCE files
contained in the JWST software repository).

Disclaimer
^^^^^^^^^^
This software is available "as is", without warranty of any kind, either 
expressed or implied, including the implied warranties of 
merchantability and fitness for a specific purpose. By using this 
software you are assuming all risks and costs. In no event is the MIRI 
EC software team or the MIRI consortium liable for any damages or losses 
that might result from the use of this software.

Introduction
~~~~~~~~~~~~
This document describes the implementation details for the MIRI general 
purpose tools and utilities package (miri.tools). Tools may be found 
within the top level miri.tools module, or they may be categorized into 
subpackages, such as miri.datamodels.

Modules
~~~~~~~
General purpose miri.tools modules may be found in the miri/tools/lib 
directory

.. module:: miri.tools

.. toctree::
   :maxdepth: 1

   filesearching
   miriplot

Unit tests corresponding to these modules may be found in the 
miri/tools/tests directory.

Scripts
~~~~~~~
General purpose miri.tools scripts may be found in the miri/tools/scripts 
directory.

At the moment there are no top level scripts. The scripts associated 
with each subpackage may be found in the miri/tools/subpackage/scripts 
directory.

Data
~~~~
General purpose miri.tools data may be found in the miri/tools/data
directory.

At the moment there are no top level data. The data associated with
each subpackage may be found in the miri/tools/subpackage/data directory.
