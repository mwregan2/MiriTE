#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""

An extension to the standard STScI data model, which defines the MIRI
transmission correction model.

:Reference:

The STScI jwst.datamodels documentation.

:History:

26 Jun 2015: Created
30 Jun 2015: CHANNEL column added.
09 Jul 2015: Removed duplication of table units between schema and metadata.
             Units are now only defined in the metadata.
             Use of the fieldnames class variable removed from the code and
             deprecated. It is now used only by a few conversion scripts.
11 Sep 2015: Removed duplicated plot method.
15 Jun 2017: meta.reffile schema level removed to match changes in the
             JWST build 7.1 data models release. meta.reffile.type also
             changed to meta.reftype. TYPE keyword replaced by DATAMODL.
12 Jul 2017: Replaced "clobber" parameter with "overwrite".

@author: Steven Beard (UKATC), Vincent Geers (UKATC)

"""
# For consistency, import the same Python V3 features as the STScI data model.
from __future__ import absolute_import, unicode_literals, division, print_function

import warnings
#import numpy as np

# Import the MIRI base data model and utilities.
from miri.datamodels.miri_model_base import MiriDataModel

# List all classes and global functions here.
__all__ = ['MiriMrsTransmissionCorrectionModel']


class MiriMrsTransmissionCorrectionModel(MiriDataModel):
    """
    
    A generic data model for a MIRI transmission correction table,
    based on the STScI base model, DataModel.
    
    :Parameters:
    
    init: shape tuple, file path, file object, pyfits.HDUList, numpy array
        An optional initializer for the data model, which can have one
        of the following forms:
        
        * None: A default data model with no shape.
        * Shape tuple: Initialize with empty data of the given shape.
        * File path: Initialize from the given file.
        * Readable file object: Initialize from the given file object.
        * pyfits.HDUList: Initialize from the given pyfits.HDUList.
        
    tracorr_table: list of tuples or numpy record array (optional)
        Either: A list of tuples containing columns in the transmission
        correction table;
        Or: A numpy record array containing the same information as above.
        A transmission correction table must either be defined in the
        initializer or in this parameter. A blank table is not allowed.
    \*\*kwargs:
        All other keyword arguments are passed to the DataModel initialiser.
        See the jwst.datamodels documentation for the meaning of these keywords.
        
    """
    schema_url = "miri_transmission_correction_mrs.schema.yaml"
    fieldnames = ('CHANNEL', 'WAVE_MIN', 'WAVE_MAX', 'T_WMIN_CENTRE',
                  'T_WMIN_EDGE', 'T_WMAX_CENTRE', 'T_WMAX_EDGE')
    
    def __init__(self, init=None, tracorr_table=None, **kwargs):
        """
        
        Initialises the MiriMrsTransmissionCorrectionModel class.
        
        Parameters: See class doc string.

        """
        super(MiriMrsTransmissionCorrectionModel, self).__init__(init=init, **kwargs)

        # Data type is transmission correction.
        self.meta.model_type = 'TRACORR'
        self.meta.reftype = 'TRACORR'
        
        # The default pedigree is 'GROUND'
        if not self.meta.pedigree:
            self.meta.pedigree = 'GROUND'
            
        # A USEAFTER date must exist. If not relevant, set it to an
        # impossibly early date.
        if not self.meta.useafter:
            self.meta.useafter = '2000-01-01T00:00:00'
        
        if tracorr_table is not None:
            try:
                self.tracorr_table = tracorr_table
            except (ValueError, TypeError) as e:
                strg = "tracorr_table must be a numpy record array or list of records."
                strg += "\n   %s" % str(e)
                raise TypeError(strg)
#         
#         # Copy the table column units, if defined.
#         tracorr_units = self.set_table_units('tracorr_table')
        
    def __str__(self):
        """
        
        Display the contents of the transmission correction object
        as a readable string.
        
        """
        # Start with the data object title and metadata
        strg = self.get_title(underline=True, underchar="=") + "\n"
        strg += self.get_meta_str(underline=True, underchar='-')

        # Describe the transmission correction table
        if self.tracorr_table is not None:
            strg += self.get_data_str('tracorr_table', underline=True, underchar="-")
        return strg


#
# A minimal test is run when this file is run as a main program.
# For a more substantial test see miri/datamodels/tests.
#
if __name__ == '__main__':
    print("Testing the MiriMrsTransmissionCorrectionModel module.")
    
    PLOTTING = False
    SAVE_FILES = False

    tracorrdata = [(1, 4.87, 7.76, 96.7, 93.3, 91.0, 91.6),
                   (2, 7.45, 11.87, 96.2, 92.2, 91.9, 90.5)]

    print("\nTransmission correction with factors derived from list of tuples:")
    with MiriMrsTransmissionCorrectionModel( tracorr_table=tracorrdata ) as testtracorr1:
        print(testtracorr1)
        if PLOTTING:
            testtracorr1.plot(description="testtracorr1")
        if SAVE_FILES:
            testtracorr1.save("test_tracorr_model1.fits", overwrite=True)
        del testtracorr1
        
    print("Test finished.")